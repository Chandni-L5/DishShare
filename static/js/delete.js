(() => {
  let formSelector = null;

  document.addEventListener('click', (e) => {
    const trigger = e.target.closest('.js-delete-trigger[data-form]');
    if (trigger) {
      formSelector = trigger.getAttribute('data-form');
    }
  });

  document.addEventListener('click', (e) => {
    if (e.target.closest('#confirmDeleteBtn')) {
      const form = formSelector ? document.querySelector(formSelector) : null;
      if (!form) { console.warn('[DeleteModal] Form not found:', formSelector); return; }
      e.target.setAttribute('disabled', 'disabled');
      if (form.requestSubmit) form.requestSubmit(); else form.submit();
      formSelector = null;
    }
  });
})();
