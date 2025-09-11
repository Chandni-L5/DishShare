# Bug Fixes and Issues Resolved
During the development of this project, I encountered several bugs and issues that required attention. Below is a summary of the key problems I faced and how I resolved them:

## Rendering of the Ingredients List and Method
 Initially, I faced challenges with rendering the ingredients list and method correctly on the recipe detail page. The issue was that the ingredients and method were not displaying as intended in ordered and unordered lists, which affected the user experience.

 When I initially created the model the fields for ingredients and method were set to `TextField` however this did not allow for proper formatting of lists. In addition the text entered via Django admin was not being rendered correctly in the template. 

 ![screenshot of admin interface for entering ingredients and method](/documentation/images/bugs/recipe-bug2.webp)
 
 ![screenshot of ingredients and method not rendering correctly](/documentation/images/bugs/recipe-bug3.webp)

 To resolve this, I decided to remove the `ingredients = models.TextField()` and `method = models.TextField()` fields from the original `RecipePost` model. 

 Instead I created two new models: `Ingredient` and `MethodStep`. Each of these models has a ForeignKey relationship to the `RecipePost` model, allowing for multiple ingredients and method steps to be associated with a single recipe. An invisible `order` field was also added to both models to ensure that the ingredients and method steps are displayed in the order they were added. This field is automatically managed and does not require user input.

 ![screenshot of change to Django admin interface showing ingredients and method steps as separate entries](/documentation/images/bugs/recipe-bug.webp)

 Then in the recipe submission form, I updated the form to allow users to add multiple ingredients and method steps dynamically. This was achieved using JavaScript to append new input fields as needed.       

In the recipe detail template, I updated the rendering logic to iterate over the related `Ingredient` and `MethodStep` objects, displaying them in ordered and unordered lists respectively. This ensured that the ingredients and method steps were presented clearly and in a user-friendly format.

Over on the users side, I updated the submission form to use `inline formsets` for both ingredients and method steps. This allowed users to add, edit, and delete ingredients and method steps directly within the recipe submission form. When it came to creating the edit and delete functionality for the ingredients and method steps within the submissions app, I created separate views and templates to handle these actions. This allowed users to manage the ingredients and method steps associated with their recipes effectively using the `django.forms formset_factory`.

I consulted the following resources to help implement these changes:
- [Django formsets documentation](https://docs.djangoproject.com/en/4.2/topics/forms/formsets/)
- [Stack Overflow - Django inline formsets](https://stackoverflow.com/questions/29758558/inlineformset-factory-create-new-objects-and-edit-objects-after-created)
- [Dennis Ivy - How to use Django inline formsets tutorial](https://www.youtube.com/watch?v=MRWFg30FmZQ)
- [dev.to blog](https://dev.to/zxenia/django-inline-formsets-with-class-based-views-and-crispy-forms-14o6)

## 404 errors and other common error codes
 when accessing certain pages - resolved by creating custom error pages and updating the `settings.py` file to point to these templates. I have updated and tidied up `urls.py` to ensure that all paths are correctly defined and that any undefined paths are properly handled by the custom error pages.

This issue was created by users trying to access pages that did not exist or were restricted, resulting in a poor user experience. By creating custom error pages, I was able to provide a more user-friendly message and guide users back to the main site, whilst incorporating helpful links and styling to match the rest of the application.

## Mixed content warnings
![screenshot of mixed content warning](/documentation/images/bugs/image-bug2.webp)

  These warnings were identified in the Chrome dev tools console. In addition it was reducing the lighthouse scores as a result:

  ![screenshot of lighthouse score with mixed content warning](/documentation/images/bugs/html-bug.webp)
  ![screenshot of lighthouse score with mixed content warning](/documentation/images/bugs/image-bug3.webp)

   This was due to some images being sourced from http rather than https. I have resolved this by ensuring that all images are sourced from secure https links.

I consulted the following resources to help resolve these issues:
- [kinsta.com/blog/mixed-content-errors/](https://kinsta.com/blog/mixed-content-errors/)
- [stackoverflow.com/what-is-mixed-content](https://stackoverflow.com/questions/20646822/what-is-mixed-content)

However was unable to resolve this issue myself. I consulted with [chatgpt](https://chatgpt.com/) which helped me to identify that the issue was caused by the cloudinary image urls which contained plain `http://` instead of `https://`. I have not encountered this issue before and so proceeded to follow the chatgpt guidance to resolve the issue. 

 It was suggested to secure the [Cloudinary](https://cloudinary.com/documentation/secure_delivery) URLs in the settings.py file as well as creating an alternative placeholder image in case any images fail to load. The image was also created using chatgpt.

## Cloudinary image URLs
On updating the cloudinary image URLs to be secure, I encountered issues with images not loading correctly in the templates.

Again I used chatgpt guidance to understand this issue better. Following the guidance I was able to create a `safe_url` filter to ensure that all image URLs are properly secured before being rendered in the templates.

A filter was applied in views.py to try to get the cloudinary image url created by the submission in the `image_field` from the model. If anything goes wrong, an empty string is returned. 

If this occurs, the template checks if the `safe_url` is available. If it is, it uses that URL to display the image. If not, it falls back to a default placeholder image stored in the static files.

## Slug Uniqueness
 I encountered issues with duplicate slugs being created when users submitted recipes with the same title. This caused conflicts when trying to access individual recipe pages, as the URL relies on the slug to identify the specific recipe.

To resolve this, I implemented an additional function, during the event a recipe had the same title, a number would be appended to the slug to ensure its uniqueness. If the title already existed, the function would increment the number until a unique slug was found.

## Allauth messages

I wanted to customize the messages displayed to users during the authentication process. This involved disabling the default allauth messages and replacing them with custom JavaScript popup messages.

To achieve this, I followed these steps:

1. Disabled allauth's default messages by overriding the `messages` context processor in the settings.py file.
2. Implemented custom JavaScript code to display popup messages based on specific authentication events such as login, logout, registration, submission of recipes and comments, and editing and deleting users own content.
Other than the `you are not logged in` message, all other messages are only displayed when the user is logged in.
3. Ensured that the custom messages were triggered at the appropriate times during the authentication process.

I consulted the following resources to help with this implementation:
- [stackoverflow.com](https://stackoverflow.com/questions/25744425/how-to-clean-up-django-login-message-from-framework?utm_source=chatgpt.com) - to manipulate the messages in Django
- [allauth documentation](https://pypi.org/project/django-allauth/0.17.0/?utm_source=chatgpt.com)
- [geeksforgeeks.org](https://www.geeksforgeeks.org/python/python-extending-and-customizing-django-allauth/)
- [stackoverflow.com](https://stackoverflow.com/questions/45225384/django-messages-how-to-hide-specific-ones?utm_source=chatgpt.com) - to hide specific messages

