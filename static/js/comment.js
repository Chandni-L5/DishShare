document.addEventListener('DOMContentLoaded', function () {
  const editButtons = document.getElementsByClassName("btn-edit");
  const commentText = document.getElementById("id_content");
  const commentForm = document.getElementById("commentForm");
  const submitButton = document.getElementById("submitButton");
  const deleteModalEl = document.getElementById('deleteModal');
  const slug = document.body.getAttribute('data-slug');

  /**
   * Initializes edit functionality for the provided edit buttons.
   * 
   * For each button in the `editButtons` collection:
   * - Retrieves the associated comment's ID upon click.
   * - Fetches the content of the corresponding comment.
   * - Populates the `commentText` input/textarea with the comment's content for editing.
   * - Updates the submit button's text to "Update".
   * - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
   */
  for (let button of editButtons) {
    button.addEventListener("click", (e) => {
      const commentId = button.getAttribute("data-comment-id");
      const commentContentElem = document.getElementById(`comment${commentId}`);
      if (commentContentElem) {
        commentText.value = commentContentElem.innerText.trim();
        submitButton.innerText = "Update";
  commentForm.setAttribute("action", `/recipes-hub/${slug}/edit_comment/${commentId}/`);
      } else {
        alert("Comment content not found for editing.");
      }
    });
  }

  /**
   * Initializes deletion functionality for the provided delete buttons.
   * 
   * For each button in the `deleteButtons` collection:
   * - Retrieves the associated comment's ID upon click.
   * - Updates the `deleteConfirm` link's href to point to the 
   * deletion endpoint for the specific comment.
   * - Displays a confirmation modal (`deleteModal`) to prompt 
   * the user for confirmation before deletion.
   */
  if (deleteModalEl) {
    deleteModalEl.addEventListener('show.bs.modal', (event) => {
      const triggerBtn = event.relatedTarget;
      const url = triggerBtn.getAttribute('data-delete-url');
      deleteModalEl.querySelector('#deleteConfirm').setAttribute('href', url);
    });
  }
});