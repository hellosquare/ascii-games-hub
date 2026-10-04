(async function buildGameGrid() {
  const grid = document.getElementById('game-grid');
  try {
    const response = await fetch('games.json', { cache: 'no-store' });
    if (!response.ok) throw new Error('Could not load games.json');
    const games = await response.json();

    grid.innerHTML = games.map(game =>
      `<a class="game-card" href="play.html?game=${encodeURIComponent(game.id)}">${escapeHtml(game.title)}</a>`
    ).join('');
  } catch (error) {
    grid.innerHTML = '<p>Unable to load the game list.</p>';
    console.error(error);
  }
})();

function escapeHtml(value) {
  return String(value).replace(/[&<>'"]/g, char => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;'
  }[char]));
}
