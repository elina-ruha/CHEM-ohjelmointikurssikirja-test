document.addEventListener('DOMContentLoaded', function () {
  // Remove beforeunload dialog triggered by Thebe/JupyterLite
  window.onbeforeunload = null;

  // Also catch any listeners added after page load
  const originalAddEventListener = window.addEventListener.bind(window);
  window.addEventListener = function (type, listener, options) {
    if (type === 'beforeunload') return; // Block all beforeunload registrations
    return originalAddEventListener(type, listener, options);
  };
});
