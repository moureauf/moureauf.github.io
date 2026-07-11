(function () {
  var root = document.documentElement;
  var colours = { light: '#EEECE4', dark: '#16140E' };

  function apply(theme) {
    root.setAttribute('data-theme', theme);
    document.querySelectorAll('meta[name="theme-color"]').forEach(function (m) {
      m.setAttribute('content', colours[theme]);
    });
  }

  // The head snippet sets data-theme before first paint; sync the
  // theme-color metas with it here.
  var stored = root.getAttribute('data-theme');
  if (stored) apply(stored);

  document.getElementById('themeToggle').addEventListener('click', function () {
    var cur = root.getAttribute('data-theme');
    if (!cur) {
      cur = matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }
    var next = cur === 'dark' ? 'light' : 'dark';
    apply(next);
    try { localStorage.setItem('theme', next); } catch (e) {}
  });
})();
