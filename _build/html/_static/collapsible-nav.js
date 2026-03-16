/* Collapsible sidebar sections for Gradient Dynamics docs */
(function () {
  function initCollapsibleNav() {
    var captions = document.querySelectorAll('.bd-docs-nav .caption');

    captions.forEach(function (caption) {
      var ul = caption.nextElementSibling;
      if (!ul || !ul.classList.contains('bd-sidenav')) return;

      // Check if this section contains the active page
      var isActive = ul.querySelector('.current, .active') !== null;

      // Collapse by default unless this section is active
      if (!isActive) {
        ul.style.display = 'none';
        caption.classList.add('nav-section-collapsed');
      } else {
        caption.classList.add('nav-section-expanded');
      }

      caption.style.cursor = 'pointer';
      caption.setAttribute('role', 'button');

      caption.addEventListener('click', function () {
        var isHidden = ul.style.display === 'none';
        ul.style.display = isHidden ? '' : 'none';
        caption.classList.toggle('nav-section-collapsed', !isHidden);
        caption.classList.toggle('nav-section-expanded', isHidden);
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCollapsibleNav);
  } else {
    initCollapsibleNav();
  }
})();
