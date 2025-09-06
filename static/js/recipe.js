// This function handles adding a new form row for ingredients and method entries in the recipe submission form.
(function () {
  function addRow(prefix) {
    const container = document.getElementById(`${prefix}-forms`);
    const template  = document.getElementById(`${prefix}-empty-form`);
    if (!container || !template) {
      console.warn(`[${prefix}] Missing container/template`, { container, template });
      return;
    }

    const formEl = container.closest('form');
    let totalInput =
      formEl?.querySelector(`#id_${prefix}-TOTAL_FORMS`) ||
      formEl?.querySelector(`input[name="${prefix}-TOTAL_FORMS"]`);

    if (!totalInput) {
      console.warn(`[${prefix}] Missing management form (TOTAL_FORMS)`, { formEl, totalInput });
      return;
    }

    const index = parseInt(totalInput.value, 10);

    const html = template.innerHTML.replace(/__prefix__/g, index);
    container.insertAdjacentHTML('beforeend', html);

    totalInput.value = index + 1;
  }

  function wire(prefix) {
    const btn = document.getElementById(`add-${prefix}`);
    if (btn) btn.addEventListener('click', () => addRow(prefix));
  }

  function init() {
    console.log('recipe.js loaded');
    wire('ing');
    wire('step');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

