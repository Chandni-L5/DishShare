// Dynamically add and remove form rows for ingredients and steps
(function () {
  function addRow(prefix) {
    const container = document.getElementById(`${prefix}-forms`);
    const template  = document.getElementById(`${prefix}-empty-form`);
    if (!container || !template) return;
    const formEl = container.closest('form');
    const totalInput =
      formEl?.querySelector(`#id_${prefix}-TOTAL_FORMS`) ||
      formEl?.querySelector(`input[name="${prefix}-TOTAL_FORMS"]`);
    if (!totalInput) return;
    const index = parseInt(totalInput.value, 10);
    const html  = template.innerHTML.replace(/__prefix__/g, index);
    const tmp = document.createElement('div');
    tmp.innerHTML = html.trim();
    const row = tmp.firstElementChild;
    if (row && !row.classList.contains(`${prefix}-row`)) {
      row.classList.add(`${prefix}-row`);
    }
    container.appendChild(row);
    totalInput.value = index + 1;
  }

  // Re-index form rows after addition or removal to maintain correct ordering.
  function reindex(prefix) {
    const container = document.getElementById(`${prefix}-forms`);
    const rows = container ? Array.from(container.querySelectorAll(`.${prefix}-row`)) : [];
    const totalInput = document.getElementById(`id_${prefix}-TOTAL_FORMS`);
    if (!container || !totalInput) return;
    rows.forEach((row, i) => {
      row.querySelectorAll('[name],[id],[for]').forEach(el => {
        ['name','id','for'].forEach(attr => {
          const val = el.getAttribute(attr);
          if (!val) return;
          const re = new RegExp(`(${prefix}-)\\d+(-)`);
          if (re.test(val)) el.setAttribute(attr, val.replace(re, `$1${i}$2`));
        });
      });
    });
    totalInput.value = rows.length;
  }

  // Remove a form row and mark it for deletion if applicable. Then re-index remaining rows.
  function removeRow(btn) {
    const row = btn.closest('.ing-row, .step-row');
    if (!row) return;
    const prefix = row.classList.contains('ing-row') ? 'ing' : 'step';
    const del = row.querySelector('input[type="checkbox"][name$="-DELETE"]');
    if (del) {
      del.checked = true;
      row.style.display = 'none';
      return;
    }
    row.remove();
    reindex(prefix);
  }

  // Set up event listeners for adding and removing rows for the given prefix (ing or step).
  function wire(prefix) {
    document.getElementById(`add-${prefix}`)?.addEventListener('click', () => addRow(prefix));
  }

  function init() {
    wire('ing');
    wire('step');

    document.addEventListener('click', (e) => {
      if (e.target.matches('.remove-row')) {
        e.preventDefault();
        removeRow(e.target);
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
