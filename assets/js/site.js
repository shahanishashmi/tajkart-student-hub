(() => {
  document.documentElement.classList.add('js');
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#primary-nav');
  if (toggle && nav) {
    const setMenuOpen = (open) => {
      toggle.setAttribute('aria-expanded', String(open));
      nav.classList.toggle('is-open', open);
    };
    toggle.addEventListener('click', () => {
      const open = toggle.getAttribute('aria-expanded') === 'true';
      setMenuOpen(!open);
    });
    nav.addEventListener('click', (event) => {
      if (event.target.closest && event.target.closest('a')) setMenuOpen(false);
    });
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        setMenuOpen(false);
        toggle.focus();
      }
    });
  }

  const answer = document.querySelector('#loop-answer');
  const checkAnswer = document.querySelector('#check-loop-answer');
  const feedback = document.querySelector('#loop-feedback');
  if (answer && checkAnswer && feedback) {
    checkAnswer.addEventListener('click', () => {
      if (answer.value === '') {
        feedback.textContent = 'Enter a number, then check your answer.';
        answer.focus();
      } else if (Number(answer.value) === 3) {
        feedback.textContent = 'Correct. The body runs once for each of the three list items.';
      } else {
        feedback.textContent = 'Try again. Count the items in the list; each one gets one loop pass.';
      }
    });
  }

  for (const quiz of document.querySelectorAll('[data-quiz]')) {
    const questions = Array.from(quiz.querySelectorAll('[data-question]'));
    const progress = quiz.querySelector('[data-quiz-progress]');
    const tools = typeof window !== 'undefined' ? window.TajkartLearningTools : null;
    const sessionId = `${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 10)}`;
    let learningState = tools ? tools.loadState() : null;
    const updateProgress = () => {
      const answered = questions.filter((question) => {
        return Boolean(question.querySelector('input[type="radio"]:checked'))
          || Array.from(question.querySelectorAll('input[type="text"], input[type="number"]')).some((input) => input.value.trim());
      }).length;
      if (progress) progress.textContent = `${answered} of ${questions.length} questions answered.`;
    };
    quiz.addEventListener('change', updateProgress);
    quiz.addEventListener('input', updateProgress);
    quiz.addEventListener('submit', (event) => {
      event.preventDefault();
      let score = 0;
      let answered = 0;
      const practicedSkills = new Set();
      let firstUnanswered = null;
      for (const question of questions) {
        const selected = question.querySelector('input[type="radio"]:checked');
        const textInput = question.querySelector('input[type="text"], input[type="number"]');
        const value = selected ? selected.value : (textInput ? textInput.value.trim() : '');
        const result = question.querySelector('[data-feedback]');
        const solution = question.querySelector('[data-solution]');
        if (!value) {
          if (result) result.textContent = 'Enter an answer before checking this question.';
          if (!firstUnanswered) firstUnanswered = textInput || question.querySelector('input[type="radio"]');
          continue;
        }
        answered++;
        const accepted = (question.dataset.acceptedAnswers || question.dataset.answer || '').split('|').filter(Boolean);
        const format = question.dataset.answerFormat || 'text';
        const formatValid = tools ? tools.normalizeAnswer(value, format) !== null : true;
        const correct = tools ? tools.answerIsAccepted(value, accepted, format)
          : value.trim().toLocaleLowerCase() === String(question.dataset.answer || '').trim().toLocaleLowerCase();
        if (correct) score++;
        const hint = question.querySelector('details p');
        if (result) {
          result.replaceChildren();
          result.textContent = correct
            ? 'Correct. Compare your steps with the worked method.'
            : !formatValid
              ? `This input does not match the expected ${format} answer format. ${hint ? hint.textContent : 'Review the linked lesson, then try again.'}`
              : `Not yet. ${hint ? hint.textContent : 'Review the linked lesson, then try again.'}`;
          if (!correct && question.dataset.resourceUrl) {
            const link = document.createElement('a');
            link.href = question.dataset.resourceUrl;
            link.textContent = ` Review ${question.dataset.resourceId || 'the linked resource'}.`;
            result.append(link);
          }
        }
        if (solution) solution.hidden = false;
        const skillIds = (question.dataset.skillIds || '').split(',').map((item) => item.trim()).filter(Boolean);
        for (const skillId of skillIds) practicedSkills.add(skillId);
        if (tools && question.dataset.questionId && skillIds.length) {
          learningState = tools.recordAttempt(learningState, {
            questionId: question.dataset.questionId,
            skillIds,
            correct,
            sessionId,
            at: new Date().toISOString()
          });
        }
      }
      if (firstUnanswered && firstUnanswered.focus) firstUnanswered.focus();
      const status = quiz.querySelector('[data-quiz-status]');
      if (status) status.textContent = answered
        ? `You got ${score} of ${answered} answered correctly. ${questions.length - answered} unanswered. This is practice feedback, not a grade.`
        : 'No answers were checked yet. Enter at least one answer and try again.';
      const progressSaved = tools && answered ? tools.saveState(learningState) : null;
      const mastery = quiz.querySelector('[data-mastery-summary]');
      if (mastery && tools && practicedSkills.size) {
        mastery.replaceChildren();
        const heading = document.createElement('h2');
        heading.textContent = 'Practice evidence by skill';
        mastery.append(heading);
        const list = document.createElement('ul');
        for (const skillId of practicedSkills) {
          const evidence = tools.skillEvidence(learningState, skillId);
          const item = document.createElement('li');
          const recentPercent = evidence.recentAccuracy === null ? 'no recent score' : `${Math.round(evidence.recentAccuracy * 100)}% across the latest ${evidence.recentAttempts}`;
          const summary = evidence.status === 'insufficient-evidence'
            ? `${evidence.attempts} attempt(s), ${evidence.sessions} practice session(s), ${recentPercent}. At least 5 attempts across 2 sessions are required before this simple threshold can be considered.`
            : evidence.status === 'evidence-threshold-met'
              ? `${recentPercent} across ${evidence.sessions} sessions; the local evidence threshold is met. This is not permanent mastery or a validated educational measure.`
              : `${recentPercent} across ${evidence.sessions} sessions; review this skill and practise again.`;
          item.textContent = `${skillId}: ${summary}`;
          list.append(item);
        }
        mastery.append(list);
        if (!progressSaved) {
          const warning = document.createElement('p');
          warning.textContent = 'This browser could not save progress locally. Your lessons and practice remain usable.';
          mastery.append(warning);
        }
      }
    });
  }

  const planner = document.querySelector('[data-study-planner]');
  if (planner) {
    const tools = typeof window !== 'undefined' ? window.TajkartLearningTools : null;
    const catalogueNode = planner.querySelector('#study-plan-catalogue');
    const goal = planner.querySelector('#study-goal');
    const sessions = planner.querySelector('#study-plan-sessions');
    const summary = planner.querySelector('#study-plan-summary');
    const recommendation = planner.querySelector('#study-plan-recommendation');
    const storageMessage = planner.querySelector('#study-plan-storage-message');
    const reset = planner.querySelector('[data-reset-plan]');
    let catalogue = [];
    try { catalogue = JSON.parse(catalogueNode ? catalogueNode.textContent : '[]'); } catch { catalogue = []; }
    if (!tools || !goal || !sessions || !summary || !recommendation || !storageMessage) {
      if (summary) summary.textContent = 'The planner controls are unavailable. Use the course links on this page to study without saved progress.';
    } else {
      const validCourses = catalogue.filter((course) => course && course.id && course.title && Array.isArray(course.steps) && course.steps.length);
      for (const course of validCourses) {
        const option = document.createElement('option');
        option.value = course.id;
        option.textContent = course.title;
        goal.append(option);
      }
      const stateNow = () => tools.loadState();
      const save = (state) => {
        if (tools.saveState(state)) storageMessage.textContent = 'Study checkmarks and quiz attempts are saved only in this browser. They are not synced.';
        else storageMessage.textContent = 'This browser did not allow local storage. You can still use every lesson and mark work on paper.';
      };
      const renderRecommendation = (course, state) => {
        recommendation.replaceChildren();
        const chosen = course ? tools.recommendStudyStep(course.steps, state) : null;
        if (!chosen) {
          recommendation.textContent = 'Choose a course to see its sessions and next step.';
          return;
        }
        const explanation = document.createElement('p');
        explanation.textContent = chosen.reason;
        recommendation.append(explanation);
        if (chosen.step && chosen.step.url) {
          const link = document.createElement('a');
          link.href = chosen.step.url;
          link.textContent = chosen.kind === 'review' ? `Review: ${chosen.step.title}` : `Continue: ${chosen.step.title}`;
          recommendation.append(link);
        }
      };
      const render = () => {
        const course = validCourses.find((item) => item.id === goal.value);
        const state = stateNow();
        sessions.replaceChildren();
        if (!course) {
          summary.textContent = 'Choose one of the course paths that has explicit lesson metadata.';
          renderRecommendation(null, state);
          return;
        }
        const completed = new Set([...state.completedSteps, ...state.completedLessons]);
        const doneCount = course.steps.filter((step) => completed.has(step.id)).length;
        summary.textContent = `${doneCount} of ${course.steps.length} planned sessions marked complete. Lesson completion, quiz results, and mastery evidence are recorded separately.`;
        for (const [index, step] of course.steps.entries()) {
          const item = document.createElement('li');
          const heading = document.createElement('h3');
          const link = document.createElement('a');
          link.href = step.url;
          link.textContent = `${index + 1}. ${step.title}`;
          heading.append(link);
          item.append(heading);
          const detail = document.createElement('p');
          detail.textContent = `${step.kind || 'Study'} · planning estimate ${Number(step.minutes) || 30} minutes`;
          item.append(detail);
          const missing = (step.prerequisites || []).filter((prerequisite) => !state.completedLessons.includes(prerequisite.id));
          if (missing.length) {
            const prerequisiteHeading = document.createElement('p');
            prerequisiteHeading.textContent = 'Prerequisites to review or mark complete after studying:';
            item.append(prerequisiteHeading);
            const prereqList = document.createElement('ul');
            for (const prerequisite of missing) {
              const prereqItem = document.createElement('li');
              const prereqLink = document.createElement('a');
              prereqLink.href = prerequisite.url;
              prereqLink.textContent = prerequisite.title;
              prereqItem.append(prereqLink);
              const markPrereq = document.createElement('button');
              markPrereq.type = 'button';
              markPrereq.dataset.completeId = prerequisite.id;
              markPrereq.dataset.isLesson = prerequisite.kind === 'lesson' ? 'true' : 'false';
              markPrereq.textContent = 'Mark prerequisite studied';
              prereqItem.append(markPrereq);
              prereqList.append(prereqItem);
            }
            item.append(prereqList);
          }
          const mark = document.createElement('button');
          mark.type = 'button';
          mark.dataset.completeId = step.id;
          mark.dataset.isLesson = step.kind === 'lesson' ? 'true' : 'false';
          mark.setAttribute('aria-pressed', String(completed.has(step.id)));
          mark.textContent = completed.has(step.id) ? 'Mark session incomplete' : 'Mark session complete';
          item.append(mark);
          sessions.append(item);
        }
        renderRecommendation(course, state);
      };
      goal.addEventListener('change', render);
      sessions.addEventListener('click', (event) => {
        const button = event.target.closest && event.target.closest('button[data-complete-id]');
        if (!button) return;
        const state = stateNow();
        const id = button.dataset.completeId;
        const complete = button.dataset.isLesson === 'true' ? !state.completedLessons.includes(id) : !state.completedSteps.includes(id);
        save(tools.setStepCompleted(state, id, complete, button.dataset.isLesson === 'true'));
        render();
      });
      if (reset) reset.addEventListener('click', () => {
        const course = validCourses.find((item) => item.id === goal.value);
        if (!course) return;
        let state = stateNow();
        for (const step of course.steps) state = tools.setStepCompleted(state, step.id, false, step.kind === 'lesson');
        for (const step of course.steps) {
          for (const prerequisite of step.prerequisites || []) state = tools.setStepCompleted(state, prerequisite.id, false, prerequisite.kind === 'lesson');
        }
        save(state);
        render();
      });
      render();
    }
  }

  const portfolio = document.querySelector('[data-local-portfolio]');
  if (portfolio) {
    const tools = typeof window !== 'undefined' ? window.TajkartLearningTools : null;
    const form = portfolio.querySelector('form');
    const list = portfolio.querySelector('[data-portfolio-list]');
    const status = portfolio.querySelector('[data-portfolio-status]');
    if (!tools || !form || !list || !status) {
      if (status) status.textContent = 'The local portfolio controls are unavailable. The project brief above remains usable.';
    } else {
      const render = () => {
        const state = tools.loadState();
        list.replaceChildren();
        if (!state.portfolio.length) {
          const empty = document.createElement('li');
          empty.textContent = 'No local project drafts yet. Add one when you are ready.';
          list.append(empty);
          return;
        }
        for (const record of state.portfolio) {
          const item = document.createElement('li');
          const heading = document.createElement('h3');
          heading.textContent = record.title;
          item.append(heading);
          const details = document.createElement('p');
          details.textContent = `${record.status.replace('-', ' ')}${record.skills.length ? ` · Skills: ${record.skills.join(', ')}` : ''}`;
          item.append(details);
          const description = document.createElement('p');
          description.textContent = record.summary;
          item.append(description);
          if (record.url) {
            const link = document.createElement('a');
            link.href = record.url;
            link.textContent = 'Open the project link';
            link.target = '_blank';
            link.rel = 'external noopener noreferrer';
            item.append(link);
          }
          const remove = document.createElement('button');
          remove.type = 'button';
          remove.dataset.deletePortfolioId = record.id;
          remove.textContent = `Delete ${record.title}`;
          item.append(remove);
          list.append(item);
        }
      };
      const saveButton = form.querySelector('[data-save-portfolio]');
      if (saveButton) saveButton.addEventListener('click', () => {
        if (!form.reportValidity()) return;
        const fields = new FormData(form);
        const checked = tools.validatePortfolioRecord({
          title: fields.get('project-title'),
          summary: fields.get('project-summary'),
          skills: fields.get('project-skills'),
          url: fields.get('project-url'),
          status: fields.get('project-status')
        });
        if (!checked.ok) {
          status.textContent = checked.error;
          return;
        }
        const token = typeof crypto !== 'undefined' && crypto.randomUUID ? crypto.randomUUID() : `${Date.now()}-${Math.random().toString(36).slice(2, 10)}`;
        const state = tools.loadState();
        const saved = tools.upsertPortfolioRecord(state, checked.value, `portfolio-${token}`, new Date().toISOString());
        if (!saved.ok || !tools.saveState(saved.state)) {
          status.textContent = saved.error || 'This browser could not save the draft. Copy your notes somewhere you control and try again.';
          return;
        }
        form.reset();
        status.textContent = 'Project draft saved in this browser only. It has not been published or verified.';
        render();
      });
      list.addEventListener('click', (event) => {
        const button = event.target.closest && event.target.closest('button[data-delete-portfolio-id]');
        if (!button) return;
        const state = tools.deletePortfolioRecord(tools.loadState(), button.dataset.deletePortfolioId);
        status.textContent = tools.saveState(state) ? 'Project draft deleted from this browser.' : 'This browser could not update local storage.';
        render();
      });
      render();
    }
  }

  const toolsForClear = typeof window !== 'undefined' ? window.TajkartLearningTools : null;
  for (const clearButton of document.querySelectorAll('[data-clear-local-data]')) {
    clearButton.addEventListener('click', () => {
      const confirmed = typeof window !== 'undefined' && typeof window.confirm === 'function'
        ? window.confirm('Clear saved lesson checkmarks, practice evidence, and portfolio drafts from this browser?')
        : true;
      if (!confirmed) return;
      const status = clearButton.parentElement.querySelector('[data-clear-local-status]');
      if (!toolsForClear || !toolsForClear.clearLocalData()) {
        if (status) status.textContent = 'This browser did not allow the saved learning data to be cleared.';
        return;
      }
      if (status) status.textContent = 'Saved Tajkart learning data was cleared from this browser.';
      if (typeof window !== 'undefined' && window.location && typeof window.location.reload === 'function') window.location.reload();
    });
  }

  const search = document.querySelector('.resource-search');
  if (!search) return;

  const query = search.querySelector('#resource-query');
  const resultList = search.querySelector('#search-results');
  const status = search.querySelector('#search-status');
  const sort = search.querySelector('#sort-results');
  const includeReference = search.querySelector('#include-reference-candidates');
  const controls = {
    type: search.querySelector('#filter-type'),
    category: search.querySelector('#filter-category'),
    tag: search.querySelector('#filter-tag'),
    language: search.querySelector('#filter-language'),
    sourceLocale: search.querySelector('#filter-source-locale'),
    difficulty: search.querySelector('#filter-difficulty'),
    origin: search.querySelector('#filter-origin')
  };
  if (!query || !resultList || !status) return;

  const normalize = (value) => String(value || '').normalize('NFKC').trim().toLocaleLowerCase();
  const tokenize = (value) => normalize(value).match(/[\p{L}\p{N}]+/gu) || [];
  const contentStates = {
    'not-started': 'Not started',
    'in-progress': 'In progress',
    drafted: 'Draft',
    'review-required': 'Review required',
    validated: 'Validated',
    complete: 'Complete'
  };
  const reviewStates = {
    'not-reviewed': 'not reviewed',
    pending: 'review pending',
    'technical-reviewed': 'technical review complete',
    'language-reviewed': 'language review complete',
    'accessibility-reviewed': 'accessibility review complete',
    approved: 'approved'
  };
  const fillOptions = (select, values, labels = {}) => {
    if (!select) return;
    const existing = new Set([...select.children].map((option) => option.value));
    for (const value of values) {
      if (existing.has(value)) continue;
      const option = document.createElement('option');
      option.value = value;
      option.textContent = labels[value] || value;
      select.append(option);
      existing.add(value);
    }
  };
  const addText = (parent, tag, text, className) => {
    const element = document.createElement(tag);
    if (className) element.className = className;
    element.textContent = text;
    parent.append(element);
    return element;
  };

  const prepareItems = (items, referenceCandidates = false, source = {}) => items.map((item) => {
    const tags = referenceCandidates
      ? (Array.isArray(item.topics) ? item.topics : [])
      : (Array.isArray(item.tags) ? item.tags : []);
    const resourceTypes = referenceCandidates
      ? (Array.isArray(item.resource_types) ? item.resource_types : [])
      : [item.type].filter(Boolean);
    const categories = referenceCandidates
      ? (Array.isArray(item.topics) ? item.topics : [])
      : [item.category].filter(Boolean);
    const locales = referenceCandidates
      ? (Array.isArray(item.source_list_locales) ? item.source_list_locales : [])
      : [];
    const sourceOccurrences = referenceCandidates ? (item.source_occurrences || []) : [];
    const occurrenceText = sourceOccurrences.flatMap((occurrence) => [
      occurrence.source_path,
      ...(occurrence.topic_path || []),
      occurrence.source_annotation
    ]);
    const firstOccurrence = sourceOccurrences[0];
    const sourceEntryUrl = firstOccurrence && source.repository && source.revision
      ? `${source.repository}/blob/${source.revision}/${firstOccurrence.source_path}#L${firstOccurrence.source_line}`
      : '';
    const normalized = {
      ...item,
      tags,
      categories,
      resource_types: resourceTypes,
      source_list_locales: locales,
      type: referenceCandidates ? (resourceTypes[0] || 'reference-resource') : item.type,
      category: referenceCandidates ? (categories[0] || 'uncategorized') : item.category,
      origin: referenceCandidates ? 'reference-candidate' : item.origin,
      source_entry_url: sourceEntryUrl,
      summary: referenceCandidates
        ? 'Unverified reference-list candidate. Tajkart has not checked availability, provider, suitability, access terms, or rights.'
        : item.summary
    };
    normalized.haystack = normalize([
      normalized.title,
      normalized.summary,
      normalized.category,
      normalized.type,
      normalized.language,
      normalized.difficulty,
      normalized.origin,
      normalized.content_status,
      normalized.review_status,
      normalized.creator,
      normalized.attribution,
      normalized.rights_status,
      normalized.rights_note,
      normalized.terms_or_license,
      ...tags,
      ...categories,
      ...locales,
      ...occurrenceText
    ].join(' '));
    return normalized;
  });

  const loadIndex = async () => {
    const url = search.dataset.indexUrl;
    if (!url) throw new Error('Search index path is missing.');
    const response = await fetch(url, { headers: { Accept: 'application/json' } });
    if (!response.ok) throw new Error(`Search index returned ${response.status}.`);
    const parsed = await response.json();
    if (!Array.isArray(parsed)) throw new Error('Search index has an unexpected format.');
    return prepareItems(parsed);
  };

  const loadReferenceIndex = async () => {
    const url = search.dataset.referenceIndexUrl;
    if (!url) throw new Error('Reference candidate index path is missing.');
    const response = await fetch(url, { headers: { Accept: 'application/json' } });
    if (!response.ok) throw new Error(`Reference candidate index returned ${response.status}.`);
    const parsed = await response.json();
    if (parsed?.dataset_kind !== 'unverified-reference-link-candidates' || !Array.isArray(parsed.records)) {
      throw new Error('Reference candidate index has an unexpected format.');
    }
    return prepareItems(parsed.records, true, parsed.source || {});
  };

  loadIndex().then((localItems) => {
    const languages = { en: 'English', hi: 'हिन्दी', ur: 'اردو' };
    const origins = {
      original: 'Tajkart original',
      translation: 'Translation draft',
      external: 'External reference',
      'reference-candidate': 'Unverified reference-list candidate'
    };
    let referenceItems = null;
    let referencePromise = null;
    let items = localItems;

    const addOptions = (collection) => {
      const unique = (key) => [...new Set(collection.map((item) => item[key]).filter(Boolean))].sort((a, b) => a.localeCompare(b));
      fillOptions(controls.type, [...new Set(collection.flatMap((item) => item.resource_types || [item.type]))].sort((a, b) => a.localeCompare(b)));
      fillOptions(controls.category, [...new Set(collection.flatMap((item) => item.categories || [item.category]))].sort((a, b) => a.localeCompare(b)));
      fillOptions(controls.tag, [...new Set(collection.flatMap((item) => item.tags))].sort((a, b) => a.localeCompare(b)));
      fillOptions(controls.language, unique('language'), languages);
      fillOptions(controls.sourceLocale, [...new Set(collection.flatMap((item) => item.source_list_locales || []))].sort((a, b) => a.localeCompare(b)));
      fillOptions(controls.difficulty, unique('difficulty'));
      fillOptions(controls.origin, unique('origin'), origins);
    };

    const render = () => {
      const term = normalize(query.value);
      const terms = tokenize(term);
      const selected = Object.fromEntries(Object.entries(controls).map(([key, control]) => [key, control ? control.value : '']));
      const matches = items.filter((item) => {
        return (!terms.length || terms.every((token) => item.haystack.includes(token)))
          && (!selected.type || item.resource_types.includes(selected.type))
          && (!selected.category || item.categories.includes(selected.category))
          && (!selected.tag || item.tags.includes(selected.tag))
          && (!selected.language || item.language === selected.language)
          && (!selected.sourceLocale || item.source_list_locales.includes(selected.sourceLocale))
          && (!selected.difficulty || item.difficulty === selected.difficulty)
          && (!selected.origin || item.origin === selected.origin);
      });
      const mode = sort ? sort.value : 'title';
      const relevance = (item) => {
        if (!terms.length) return 0;
        const title = normalize(item.title);
        const tags = item.tags.map(normalize);
        const summary = normalize(item.summary);
        const other = normalize([item.category, item.type, item.language, item.difficulty].join(' '));
        const tokenScore = terms.reduce((total, token) => {
          if (title.includes(token)) return total + 100 + (title.startsWith(token) ? 15 : 0);
          if (tags.some((tag) => tag.includes(token))) return total + 60;
          if (summary.includes(token)) return total + 35;
          return total + (other.includes(token) ? 10 : 0);
        }, 0);
        return tokenScore + (title === term ? 1000 : title.startsWith(term) ? 200 : 0);
      };
      matches.sort((a, b) => {
        if (mode === 'relevance' && terms.length) return relevance(b) - relevance(a) || a.title.localeCompare(b.title);
        const key = mode === 'relevance' ? 'title' : mode;
        return String(a[key] || '').localeCompare(String(b[key] || '')) || a.title.localeCompare(b.title);
      });
      resultList.replaceChildren();
      const displayed = matches.slice(0, 100);
      for (const item of displayed) {
        const row = document.createElement('li');
        row.className = 'search-result';
        const link = addText(row, 'a', item.title, 'search-result-title');
        const candidate = item.origin === 'reference-candidate';
        const external = candidate || (item.origin === 'external' && item.source_url);
        link.href = candidate ? item.url : external ? item.source_url : item.url;
        if (external) {
          link.target = '_blank';
          link.rel = 'external noopener noreferrer';
        }
        addText(row, 'p', item.summary || 'Open this learning resource.', 'search-result-summary');
        const origin = candidate
          ? 'Unverified candidate from Free Programming Books'
          : item.origin === 'translation'
          ? `${languages[item.language] || item.language} translation${item.translation_status === 'draft' ? ' draft' : ''}`
          : origins[item.origin] || origins.original;
        const state = contentStates[item.content_status] || '';
        const review = reviewStates[item.review_status] || '';
        const externalRights = item.origin === 'external'
          ? [item.verification_status, item.rights_status, item.source_checked ? `source checked ${item.source_checked}` : '']
          : [];
        const candidateMeta = candidate
          ? ['unverified', 'rights not assessed', 'access not checked', `${item.source_occurrences.length} source appearance${item.source_occurrences.length === 1 ? '' : 's'}`, ...item.source_list_locales.map((locale) => `source-list locale ${locale}`)]
          : [];
        const meta = [origin, item.creator ? `by ${item.creator}` : '', ...externalRights, ...candidateMeta, state, review, item.type, item.category, item.difficulty].filter(Boolean).join(' · ');
        addText(row, 'p', meta, 'search-result-meta');
        if (candidate && item.source_entry_url) {
          const sourceLink = addText(row, 'a', 'View source listing and attribution', 'search-result-source');
          sourceLink.href = item.source_entry_url;
          sourceLink.target = '_blank';
          sourceLink.rel = 'external noopener noreferrer';
        }
        resultList.append(row);
      }
      const candidatesIncluded = items.some((item) => item.origin === 'reference-candidate');
      status.textContent = matches.length
        ? `${candidatesIncluded ? `${matches.length} matching results` : `${matches.length} ${matches.length === 1 ? 'resource' : 'resources'} found`}.${matches.length > displayed.length ? ` Showing the first ${displayed.length}; narrow the search to see more.` : ''}${candidatesIncluded ? ' Reference-list candidates are unverified.' : ''}`
        : `No ${items.some((item) => item.origin === 'reference-candidate') ? 'results' : 'resources'} match those filters. Clear a filter or try another search.`;
    };

    [query, ...Object.values(controls), sort].filter(Boolean).forEach((control) => {
      control.addEventListener(control === query ? 'input' : 'change', render);
    });
    const refresh = async () => {
      if (!includeReference?.checked) {
        items = localItems;
        render();
        return;
      }
      if (!referencePromise) referencePromise = loadReferenceIndex();
      status.textContent = 'Loading unverified reference-list candidates…';
      try {
        if (!referenceItems) referenceItems = await referencePromise;
        items = [...localItems, ...referenceItems];
        addOptions(items);
        render();
      } catch (error) {
        includeReference.checked = false;
        items = localItems;
        render();
        status.textContent += ` Reference candidates could not load: ${error.message}`;
      }
    };
    includeReference?.addEventListener('change', refresh);
    addOptions(localItems);
    render();
  }).catch((error) => {
    status.textContent = `Search could not load. Browse the categories below instead. (${error.message})`;
  });
})();
