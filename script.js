// DeskRange Journal Client Script
let allArticles = [];
let currentCategory = 'all';

async function initJournal() {
  try {
    const res = await fetch('search-index.json');
    if (!res.ok) return;
    allArticles = await res.json();
    renderArticles();
  } catch (err) {
    console.error('Failed to load search index:', err);
  }
}

function filterArticles() {
  const query = (document.getElementById('searchInput')?.value || '').toLowerCase().trim();
  
  return allArticles.filter(art => {
    const matchesCat = currentCategory === 'all' || art.category === currentCategory;
    const matchesQuery = !query || 
      art.title.toLowerCase().includes(query) || 
      art.description.toLowerCase().includes(query) ||
      (art.tags && art.tags.some(t => t.toLowerCase().includes(query)));
    return matchesCat && matchesQuery;
  });
}

function renderArticles() {
  const container = document.getElementById('articlesGrid');
  const countEl = document.getElementById('resultsCount');
  if (!container) return;

  const filtered = filterArticles();
  if (countEl) {
    countEl.textContent = `Showing ${filtered.length} of ${allArticles.length} research-backed articles`;
  }

  if (filtered.length === 0) {
    container.innerHTML = '<div style="grid-column: 1/-1; text-align: center; padding: 3rem; color: var(--text-muted);">No matching articles found. Try adjusting your search query.</div>';
    return;
  }

  container.innerHTML = filtered.map(art => `
    <article class="article-card">
      <div class="card-category">${art.category}</div>
      <h3 class="card-title"><a href="${art.url}">${art.title}</a></h3>
      <p class="card-desc">${art.description}</p>
      <div class="card-footer">
        <span>5 min read</span>
        <a href="${art.url}">Read Article &rarr;</a>
      </div>
    </article>
  `).join('');
}

function selectCategory(cat) {
  currentCategory = cat;
  document.querySelectorAll('.cat-pill').forEach(pill => {
    pill.classList.toggle('active', pill.dataset.category === cat);
  });
  renderArticles();
}

document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    searchInput.addEventListener('input', () => renderArticles());
  }

  document.querySelectorAll('.cat-pill').forEach(pill => {
    pill.addEventListener('click', () => {
      selectCategory(pill.dataset.category);
    });
  });

  initJournal();
});
