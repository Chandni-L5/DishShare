document.addEventListener('DOMContentLoaded', function () {
  const editButtons = document.getElementsByClassName("btn-edit");
  const commentText = document.getElementById("id_content");
  const commentForm = document.getElementById("commentForm");
  const submitButton = document.getElementById("submitButton");
  const deleteModalEl = document.getElementById('deleteModal');

  /**
   * Initializes edit functionality for the provided edit buttons.
   */
  for (let button of editButtons) {
    button.addEventListener("click", () => {
      const commentId = button.getAttribute("data-comment-id");
      const editUrl = button.getAttribute("data-edit-url");
      const commentContentElem = document.getElementById(`comment${commentId}`);
      if (!commentContentElem || !editUrl) {
        alert("Comment content not found for editing.");
        return;
      }
      commentText.value = commentContentElem.innerText.trim();
      submitButton.innerText = "Update";
      commentForm.setAttribute("action", editUrl);
    });
  }

  /**
   * Initializes deletion functionality for the provided delete buttons.
   */
  if (deleteModalEl) {
    deleteModalEl.addEventListener('show.bs.modal', (event) => {
      const triggerBtn = event.relatedTarget;
      const url = triggerBtn.getAttribute('data-delete-url');
      deleteModalEl.querySelector('#deleteConfirm').setAttribute('href', url);
    });
  }
});