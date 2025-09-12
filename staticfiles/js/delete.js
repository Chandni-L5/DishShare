(() => {
  let formSelector = null;

  const deleteModal = document.getElementById('deleteRecipeModal');
  if (deleteModal) {
    deleteModal.addEventListener('show.bs.modal', (event) => {
      const trigger = event.relatedTarget;
      formSelector = trigger ? trigger.dataset.form : null;
    });
  }

  const confirmBtn = document.getElementById('confirmDeleteBtn');
  if (confirmBtn) {
    confirmBtn.addEventListener('click', () => {
      const form = formSelector ? document.querySelector(formSelector) : null;
      if (!form) { console.warn('[DeleteModal] Form not found:', formSelector); return; }
      confirmBtn.setAttribute('disabled', 'disabled');
      if (form.requestSubmit) form.requestSubmit(); else form.submit();
      formSelector = null;
      });
    }
  })();
