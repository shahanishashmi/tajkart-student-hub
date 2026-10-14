(() => {
  'use strict';

  const STORAGE_KEY = 'tajkart.student-tools.v1';
  const MAX_ATTEMPTS = 100;
  const MAX_PROJECTS = 50;
  const ID = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;
  const SKILL = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;
  const validId = (value) => typeof value === 'string' && ID.test(value);

  const emptyState = () => ({ version: 1, completedLessons: [], completedSteps: [], attempts: [], portfolio: [] });

  function cleanText(value, limit) {
    return typeof value === 'string' ? value.trim().slice(0, limit) : '';
  }

  function normalizeState(value) {
    let parsed = value;
    if (typeof parsed === 'string') {
      try { parsed = JSON.parse(parsed); } catch { return emptyState(); }
    }
    if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed) || parsed.version !== 1) return emptyState();
    const completedLessons = Array.isArray(parsed.completedLessons)
      ? [...new Set(parsed.completedLessons.filter(validId))].slice(0, 300)
      : [];
    const completedSteps = Array.isArray(parsed.completedSteps)
      ? [...new Set(parsed.completedSteps.filter(validId))].slice(0, 300)
      : [];
    const attempts = Array.isArray(parsed.attempts) ? parsed.attempts.slice(-MAX_ATTEMPTS).flatMap((item) => {
      if (!item || typeof item !== 'object' || !validId(item.questionId) || typeof item.correct !== 'boolean') return [];
      if (!Array.isArray(item.skillIds)) return [];
      const skillIds = [...new Set(item.skillIds.filter((id) => typeof id === 'string' && SKILL.test(id)))].slice(0, 8);
      if (!skillIds.length) return [];
      const sessionId = cleanText(item.sessionId, 80);
      const at = cleanText(item.at, 32);
      if (!sessionId || !Number.isFinite(Date.parse(at))) return [];
      return [{ questionId: item.questionId, skillIds, correct: item.correct, sessionId, at }];
    }) : [];
    const portfolio = Array.isArray(parsed.portfolio) ? parsed.portfolio.slice(-MAX_PROJECTS).flatMap((item) => {
      const record = validatePortfolioRecord(item);
      if (!record.ok || !validId(item.id)) return [];
      return [{ ...record.value, id: item.id, updatedAt: cleanText(item.updatedAt, 32) || new Date(0).toISOString() }];
    }) : [];
    return { version: 1, completedLessons, completedSteps, attempts, portfolio };
  }

  function loadState(storage) {
    try {
      const target = storage || (typeof window !== 'undefined' ? window.localStorage : null);
      if (!target) return emptyState();
      return normalizeState(target.getItem(STORAGE_KEY));
    } catch {
      return emptyState();
    }
  }

  function saveState(state, storage) {
    try {
      const target = storage || (typeof window !== 'undefined' ? window.localStorage : null);
      if (!target) return false;
      const normalized = normalizeState(state);
      const serialized = JSON.stringify(normalized);
      if (serialized.length > 100000) return false;
      target.setItem(STORAGE_KEY, serialized);
      return true;
    } catch {
      return false;
    }
  }

  function clearLocalData(storage) {
    try {
      const target = storage || (typeof window !== 'undefined' ? window.localStorage : null);
      if (!target || typeof target.removeItem !== 'function') return false;
      target.removeItem(STORAGE_KEY);
      return true;
    } catch {
      return false;
    }
  }

  function recordAttempt(state, attempt) {
    const current = normalizeState(state);
    if (!attempt || !validId(attempt.questionId) || typeof attempt.correct !== 'boolean') return current;
    if (!Array.isArray(attempt.skillIds)) return current;
    const skillIds = [...new Set(attempt.skillIds.filter((id) => typeof id === 'string' && SKILL.test(id)))].slice(0, 8);
    if (!skillIds.length) return current;
    const sessionId = cleanText(attempt.sessionId, 80);
    const at = cleanText(attempt.at, 32);
    if (!sessionId || !Number.isFinite(Date.parse(at))) return current;
    return {
      ...current,
      attempts: [...current.attempts, { questionId: attempt.questionId, skillIds, correct: attempt.correct, sessionId, at }].slice(-MAX_ATTEMPTS)
    };
  }

  function setLessonCompleted(state, lessonId, completed) {
    const current = normalizeState(state);
    if (!validId(lessonId)) return current;
    const completedLessons = new Set(current.completedLessons);
    if (completed) completedLessons.add(lessonId);
    else completedLessons.delete(lessonId);
    const completedSteps = new Set(current.completedSteps);
    if (completed) completedSteps.add(lessonId);
    else completedSteps.delete(lessonId);
    return { ...current, completedLessons: [...completedLessons].slice(0, 300), completedSteps: [...completedSteps].slice(0, 300) };
  }

  function setStepCompleted(state, stepId, completed, isLesson = false) {
    const current = normalizeState(state);
    if (!validId(stepId)) return current;
    const completedSteps = new Set(current.completedSteps);
    if (completed) completedSteps.add(stepId);
    else completedSteps.delete(stepId);
    const next = { ...current, completedSteps: [...completedSteps].slice(0, 300) };
    if (isLesson) return setLessonCompleted(next, stepId, completed);
    return next;
  }

  function normalizeAnswer(value, format) {
    const answer = typeof value === 'string' ? value.normalize('NFKC').trim().toLocaleLowerCase() : '';
    if (format === 'integer') {
      if (!/^[+-]?\d{1,30}$/.test(answer)) return null;
      try { return BigInt(answer).toString(); } catch { return null; }
    }
    if (format === 'decimal') {
      if (!/^[+-]?\d{1,24}(?:\.\d{1,12})?$/.test(answer)) return null;
      const [whole, fraction = ''] = answer.replace(/^\+/, '').split('.');
      const normalizedWhole = whole.startsWith('-') ? `-${whole.slice(1).replace(/^0+(?=\d)/, '')}` : whole.replace(/^0+(?=\d)/, '');
      const normalizedFraction = fraction.replace(/0+$/, '');
      const sign = normalizedWhole === '-0' && normalizedFraction ? '-' : '';
      const absoluteWhole = normalizedWhole.replace(/^-/, '') || '0';
      const isZero = /^0+$/.test(absoluteWhole) && !normalizedFraction;
      return isZero ? '0' : `${sign || (normalizedWhole.startsWith('-') ? '-' : '')}${absoluteWhole}${normalizedFraction ? `.${normalizedFraction}` : ''}`;
    }
    if (format === 'fraction') {
      if (/^-?\d{1,30}\/[1-9]\d{0,29}$/.test(answer)) return `fraction:${answer}`;
      const decimal = normalizeAnswer(answer, 'decimal');
      return decimal === null ? null : `decimal:${decimal}`;
    }
    if (format === 'text') return answer || null;
    return null;
  }

  function answerIsAccepted(value, acceptedAnswers, format) {
    if (!Array.isArray(acceptedAnswers) || !acceptedAnswers.length) return false;
    const candidate = normalizeAnswer(value, format);
    if (candidate === null) return false;
    return acceptedAnswers.some((answer) => normalizeAnswer(String(answer), format) === candidate);
  }

  function skillEvidence(state, skillId, options = {}) {
    const current = normalizeState(state);
    const requiredAttempts = Number.isInteger(options.requiredAttempts) ? options.requiredAttempts : 5;
    const recentWindow = Number.isInteger(options.recentWindow) ? options.recentWindow : 5;
    const requiredSessions = Number.isInteger(options.requiredSessions) ? options.requiredSessions : 2;
    const attempts = current.attempts.filter((item) => item.skillIds.includes(skillId));
    const recent = attempts.slice(-recentWindow);
    const correct = attempts.filter((item) => item.correct).length;
    const accuracy = recent.length ? recent.filter((item) => item.correct).length / recent.length : null;
    const sessions = new Set(attempts.map((item) => item.sessionId)).size;
    const enoughEvidence = attempts.length >= requiredAttempts && sessions >= requiredSessions && recent.length === recentWindow;
    const mastered = enoughEvidence && accuracy >= 0.8;
    return {
      skillId,
      attempts: attempts.length,
      correct,
      incorrect: attempts.length - correct,
      recentAttempts: recent.length,
      recentAccuracy: accuracy,
      sessions,
      status: !enoughEvidence ? 'insufficient-evidence' : mastered ? 'evidence-threshold-met' : 'practice-recommended'
    };
  }

  function recommendStudyStep(steps, state) {
    const current = normalizeState(state);
    const attempts = current.attempts;
    const latest = attempts.at(-1);
    if (latest && !latest.correct) {
      const related = steps.find((step) => Array.isArray(step.skills) && step.skills.some((skill) => latest.skillIds.includes(skill)));
      if (related) {
        const repeated = attempts.slice(-2).filter((item) => !item.correct && item.skillIds.some((skill) => latest.skillIds.includes(skill))).length >= 2;
        return {
          kind: 'review',
          step: related,
          reason: repeated
            ? 'Your two most recent attempts in this skill were incorrect. Revisit the explanation and prerequisite links, then try again.'
            : 'Your latest practice attempt was incorrect. Review this lesson’s explanation before continuing.'
        };
      }
    }
    const completed = new Set([...current.completedLessons, ...current.completedSteps]);
    for (const step of steps) {
      if (completed.has(step.id)) continue;
      const missing = (step.prerequisites || []).find((item) => !completed.has(item.id));
      if (missing) return { kind: 'prerequisite', step: missing, forStep: step, reason: `Complete this prerequisite before “${step.title}”.` };
      return { kind: 'next', step, reason: 'This is the next unfinished session in the selected path.' };
    }
    return { kind: 'complete', step: null, reason: 'All sessions in this path are marked complete. Choose another path or revisit any lesson.' };
  }

  function validatePortfolioRecord(input) {
    if (!input || typeof input !== 'object' || Array.isArray(input)) return { ok: false, error: 'Enter a project record.' };
    const title = cleanText(input.title, 120);
    const summary = cleanText(input.summary, 2000);
    const skills = Array.isArray(input.skills)
      ? [...new Set(input.skills.map((item) => cleanText(item, 48)).filter(Boolean))].slice(0, 12)
      : cleanText(input.skills, 500).split(',').map((item) => cleanText(item, 48)).filter(Boolean).slice(0, 12);
    const url = cleanText(input.url, 500);
    const status = input.status;
    if (!title) return { ok: false, error: 'Add a project title.' };
    if (!summary) return { ok: false, error: 'Describe what you built or plan to build.' };
    if (!['idea', 'in-progress', 'complete'].includes(status)) return { ok: false, error: 'Choose a valid project status.' };
    if (url) {
      try {
        const parsed = new URL(url);
        if (parsed.protocol !== 'https:' || !parsed.hostname || parsed.username || parsed.password) throw new Error('invalid');
      } catch {
        return { ok: false, error: 'Project links must be valid HTTPS URLs without embedded credentials.' };
      }
    }
    return { ok: true, value: { title, summary, skills, url, status } };
  }

  function upsertPortfolioRecord(state, record, id, at = new Date().toISOString()) {
    const current = normalizeState(state);
    const checked = validatePortfolioRecord(record);
    if (!checked.ok || !validId(id) || !Number.isFinite(Date.parse(at))) return { state: current, ok: false, error: checked.error || 'Invalid project record.' };
    const without = current.portfolio.filter((item) => item.id !== id);
    return {
      ok: true,
      state: { ...current, portfolio: [...without, { ...checked.value, id, updatedAt: at }].slice(-MAX_PROJECTS) }
    };
  }

  function deletePortfolioRecord(state, id) {
    const current = normalizeState(state);
    return { ...current, portfolio: current.portfolio.filter((item) => item.id !== id) };
  }

  const api = {
    STORAGE_KEY,
    emptyState,
    normalizeState,
    loadState,
    saveState,
    clearLocalData,
    recordAttempt,
    setLessonCompleted,
    setStepCompleted,
    normalizeAnswer,
    answerIsAccepted,
    skillEvidence,
    recommendStudyStep,
    validatePortfolioRecord,
    upsertPortfolioRecord,
    deletePortfolioRecord
  };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  if (typeof window !== 'undefined') window.TajkartLearningTools = api;
})();
