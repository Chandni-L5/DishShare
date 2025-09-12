# Validation 

The DishShare application has undergone thorough validation to ensure its functionality, usability, and overall quality. 

## HTML Validation
### [w3c validator](https://validator.w3.org/)
The HTML code of the DishShare application has been validated using the [W3C Markup Validation Service](https://validator.w3.org/). The validation process ensures that the HTML code adheres to web standards and best practices. The validation results indicate that the HTML code is free from errors and warnings, ensuring a high level of code quality and compatibility across different browsers and devices.

| HTML page | Validation Result| 
|------------|-------------------|
| base.html/homepage | ✅ Pass |
| Recipe Hub | ✅ Pass |
| Recipe Page | ✅ Pass |
| Submission Form | ✅ Pass |
| Edit submission | ✅ Pass |
| My submissions | ✅ Pass |
| Login | ✅ Pass |
| Register | ✅ Pass |
| Error pages | ✅ Pass |

![W3C Validation Result](/documentation/images/w3c.webp)

## CSS Validation
### [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
The CSS code of the DishShare application has been validated using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). The validation process ensures that the CSS code adheres to web standards and best practices. The validation results indicate that the CSS code is free from errors and warnings, ensuring a high level of code quality and compatibility across different browsers and devices.

| CSS file | Validation Result |
|----------|-------------------|
| base.css | ✅ Pass |
| comment.css | ✅ Pass |
| delete.css | ✅ Pass |
| signup.css | ✅ Pass |
| submit.css | ✅ Pass |

![W3C CSS Validation Result](/documentation/images/w3c-css.webp)

## JavaScript Validation
### [JSHint](https://jshint.com/)
The JavaScript code of the DishShare application has been validated using [JSHint](https://jshint.com/). The validation process ensures that the JavaScript code adheres to best practices and is free from common coding errors. The validation results indicate that the JavaScript code is free from errors and warnings, ensuring a high level of code quality and maintainability.

| JavaScript file | Validation Result |
|-----------------|-------------------|
| comment.js | ✅ Pass |
| flash.js | ✅ Pass |
| delete.js | ✅ Pass |
| recipe.js | ✅ Pass |

![JSHint Validation Result of comment.js](/documentation/images/js-comment.webp)

A warning is highlighted in the validation result for comment.js, indicating that I've declared a function inside a loop and the loop variable is a button, however as I'm using `let`, each loops has it's own scoped `button`, so this is not an issue.

## Python Validation
### [CI Pep8 Linter](https://pep8ci.herokuapp.com/)
The Python code of the DishShare application has been validated using the [CI Pep8 Linter](https://pep8ci.herokuapp.com/). The validation process ensures that the Python code adheres to the PEP 8 style guide and is free from common coding errors. The validation results indicate that the Python code is free from errors and warnings, ensuring a high level of code quality and maintainability.

|Directory| Python file | Validation Result |
|-------------|-------------|-------------------|
|accounts| apps.py | ✅ Pass |
|| forms.py | ✅ Pass |
|| tests.py | ✅ Pass |
|dishshare| settings.py | ✅ Pass |
|| urls.py | ✅ Pass |
|| wsgi.py | ✅ Pass |
|| views.py | ✅ Pass |
|recipes_post| admin.py | ✅ Pass |
|| test_errors.py | ✅ Pass |
|| test_models.py | ✅ Pass |
|| test_views.py | ✅ Pass |
|| admin.py | ✅ Pass |
|| apps.py | ✅ Pass |
|| forms.py | ✅ Pass |
|| models.py | ✅ Pass |
|| urls.py | ✅ Pass |
|| views.py | ✅ Pass | 
| submissions | apps.py | ✅ Pass |
|| forms.py | ✅ Pass |
|| tests.py | ✅ Pass |
|| urls.py | ✅ Pass |
|| views.py | ✅ Pass |

![CI Pep8 Linter Validation Result of app.py](/documentation/images/pep8.webp)
