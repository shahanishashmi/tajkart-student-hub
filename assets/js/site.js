(() => {
  document.documentElement.classList.add('js');
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#primary-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!open));
      nav.classList.toggle('is-open', !open);
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
      for (const question of questions) {
        const selected = question.querySelector('input[type="radio"]:checked');
        const textInput = question.querySelector('input[type="text"], input[type="number"]');
        const value = selected ? selected.value : (textInput ? textInput.value : '');
        const expected = question.dataset.answer.trim().toLocaleLowerCase();
        const correct = value.trim().toLocaleLowerCase() === expected;
        const result = question.querySelector('[data-feedback]');
        if (correct) score++;
        if (result) result.textContent = correct ? 'Correct.' : 'Not yet. Review the hint and try again.';
      }
      const status = quiz.querySelector('[data-quiz-status]');
      if (status) status.textContent = `You got ${score} of ${questions.length} correct.`;
    });
  }

  const search = document.querySelector('.resource-search');
  if (!search) return;

  const query = search.querySelector('#resource-query');
  const resultList = search.querySelector('#search-results');
  const status = search.querySelector('#search-status');
  const sort = search.querySelector('#sort-results');
  const controls = {
    type: search.querySelector('#filter-type'),
    category: search.querySelector('#filter-category'),
    language: search.querySelector('#filter-language'),
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
    for (const value of values) {
      const option = document.createElement('option');
      option.value = value;
      option.textContent = labels[value] || value;
      select.append(option);
    }
  };
  const addText = (parent, tag, text, className) => {
    const element = document.createElement(tag);
    if (className) element.className = className;
    element.textContent = text;
    parent.append(element);
    return element;
  };

  const loadIndex = async () => {
    const url = search.dataset.indexUrl;
    if (!url) throw new Error('Search index path is missing.');
    const response = await fetch(url, { headers: { Accept: 'application/json' } });
    if (!response.ok) throw new Error(`Search index returned ${response.status}.`);
    const parsed = await response.json();
    if (!Array.isArray(parsed)) throw new Error('Search index has an unexpected format.');
    return parsed.map((item) => ({
      ...item,
      tags: Array.isArray(item.tags) ? item.tags : [],
      haystack: normalize([item.title, item.summary, item.category, item.type, item.language, item.difficulty, item.origin, item.content_status, item.review_status, item.creator, item.attribution, item.rights_status, item.rights_note, item.terms_or_license, ...(Array.isArray(item.tags) ? item.tags : [])].join(' '))
    }));
  };

  loadIndex().then((items) => {
    const languages = { en: 'English', hi: 'हिन्दी', ur: 'اردو' };
    const origins = { original: 'Tajkart original', translation: 'Translation draft', external: 'External reference' };
    const unique = (key) => [...new Set(items.map((item) => item[key]).filter(Boolean))].sort((a, b) => a.localeCompare(b));
    fillOptions(controls.type, unique('type'));
    fillOptions(controls.category, unique('category'));
    fillOptions(controls.language, unique('language'), languages);
    fillOptions(controls.difficulty, unique('difficulty'));
    fillOptions(controls.origin, unique('origin'), origins);

    const render = () => {
      const term = normalize(query.value);
      const terms = tokenize(term);
      const selected = Object.fromEntries(Object.entries(controls).map(([key, control]) => [key, control ? control.value : '']));
      const matches = items.filter((item) => {
        return (!terms.length || terms.every((token) => item.haystack.includes(token)))
          && (!selected.type || item.type === selected.type)
          && (!selected.category || item.category === selected.category)
          && (!selected.language || item.language === selected.language)
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
      for (const item of matches) {
        const row = document.createElement('li');
        row.className = 'search-result';
        const link = addText(row, 'a', item.title, 'search-result-title');
        const external = item.origin === 'external' && item.source_url;
        link.href = external ? item.source_url : item.url;
        if (external) {
          link.target = '_blank';
          link.rel = 'external noopener noreferrer';
        }
        addText(row, 'p', item.summary || 'Open this learning resource.', 'search-result-summary');
        const origin = item.origin === 'translation'
          ? `${languages[item.language] || item.language} translation${item.translation_status === 'draft' ? ' draft' : ''}`
          : origins[item.origin] || origins.original;
        const state = contentStates[item.content_status] || '';
        const review = reviewStates[item.review_status] || '';
        const externalRights = item.origin === 'external'
          ? [item.verification_status, item.rights_status, item.source_checked ? `source checked ${item.source_checked}` : '']
          : [];
        const meta = [origin, item.creator ? `by ${item.creator}` : '', ...externalRights, state, review, item.type, item.category, item.difficulty].filter(Boolean).join(' · ');
        addText(row, 'p', meta, 'search-result-meta');
        resultList.append(row);
      }
      status.textContent = matches.length
        ? `${matches.length} ${matches.length === 1 ? 'resource' : 'resources'} found.`
        : 'No resources match those filters. Clear a filter or try another search.';
    };

    [query, ...Object.values(controls), sort].filter(Boolean).forEach((control) => {
      control.addEventListener(control === query ? 'input' : 'change', render);
    });
    render();
  }).catch((error) => {
    status.textContent = `Search could not load. Browse the categories below instead. (${error.message})`;
  });
})();
