(() => {
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#primary-nav');
  if (toggle && nav) toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', String(!open));
    nav.classList.toggle('is-open', !open);
  });

  const answer = document.querySelector('#loop-answer');
  const checkAnswer = document.querySelector('#check-loop-answer');
  const feedback = document.querySelector('#loop-feedback');
  if (answer && checkAnswer && feedback) checkAnswer.addEventListener('click', () => {
    if (answer.value === '') {
      feedback.textContent = 'Enter a number, then check your answer.';
      answer.focus();
    } else if (Number(answer.value) === 3) {
      feedback.textContent = 'Correct. The body runs once for each of the three list items.';
    } else {
      feedback.textContent = 'Try again. Count the items in the list; each one gets one loop pass.';
    }
  });

  const input = document.querySelector('#lesson-search');
  const category = document.querySelector('#lesson-category');
  const results = document.querySelector('#search-results');
  const status = document.querySelector('#search-status');
  if (!input || !results || !status) return;
  const items = Array.from(results.querySelectorAll('.search-result'));
  const filter = () => {
    const query = input.value.trim().toLocaleLowerCase();
    const selectedCategory = category ? category.value : '';
    let count = 0;
    for (const item of items) {
      const matchesQuery = !query || item.textContent.toLocaleLowerCase().includes(query);
      const matchesCategory = !selectedCategory || item.dataset.category === selectedCategory;
      const matches = matchesQuery && matchesCategory;
      item.hidden = !matches;
      if (matches) count++;
    }
    status.textContent = query || selectedCategory ? `${count} ${count === 1 ? 'result' : 'results'} found.` : `${items.length} lessons available.`;
  };
  input.addEventListener('input', filter);
  if (category) category.addEventListener('change', filter);
  filter();
})();
