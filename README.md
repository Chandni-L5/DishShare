# DishShare

[DishShare](https://dishshare-d8c892b46f87.herokuapp.com/) is a Django based website designed to bring together a community of homecooks and amateur chefs. This platform provides users with the ability to create, share and discover new recipes whilst engaging with other users through comments, likes and dislikes. 

Whether you are seeking inspiration for your next meal or want to showcase your culinary creativity, DishShare makes it easier to connect with food lovers across the world at your fingertips. 

![amiresponsive screenshot](/documentation/images/amiresponsive.webp)

- - -

## User Experience (UX) & Agile Planning and Development

### Goals and Objectives 
The aim of this website is to provide an intuitive, responsive and rich community focussed platform to connect, share and discover content. 

Users are able to log in and create a personalized list of their favorite item, submit their own content, and interact with other user's contents through the format of likes, dislikes and comments.

The target audience for this application ranges from newbies to cooking, seasoned home-cooks seeking inspiration to seasoned chefs looking to share their expertise. There are no limitations such as age groups or experience and the idea is to bring together people with the common interest of food and cooking.

### Scope 

#### User Features:
- Responsive design across different devices 
- CRUD functionality for the recipe posts, comments and favorites section
- Authentication and account management 

Only owners of data such as recipe posts or comments can access CRUD functionality related to their own content. 

#### Admin Features: 
- Manage user posts and comments
- Monitor and remove inappropriate content from the admin interface

### Agile Development and Planning

#### User Stories
The development and the planning of this project has been created with the Agile methodologies in mind throughout. 

Epics have been condensed to bitesize user stories.

📚 [The epics can be viewed here](/documentation/epics.md)

📓 [The user stories can be viewed here](/documentation/user-stories.md)

 The implementation and prioritization of user stories as well as the acceptance criteria is recorded and tracked dynamically through the use of GitHub Projects Kanban board. The Kanban board records the user story, acceptance criteria and tasks. These are checked off as we progress through the project.

📊 [The board can be viewed here](https://github.com/users/Chandni-L5/projects/11/views/3)

#### Estimation

I have used the MoSCoW prioritization method to categorize each user story according to the project requirements. These categories are also represented on the Kanban board with colored labels for easy reference by the development team. At the start of the project, 'Won’t have' items will not be applied, but this will be reassessed as progress is made.

During planning, the MoSCoW priorities were distributed as 50% Must have, 33% Should have, and 17% Could have.

<!-- Update if any of the user stories have been moved to won't have -->

To support estimation, I have assigned story points based on a Fibonacci methodology, reflecting the relative complexity of each story. This scale will guide the prioritization and ordering of tasks during development.

| Requirement | User Story | AC Numbers | Story Points | Complexity |
|------------|------------|------------|--------------|------------|
| 🟥 Must have | **Open a post** | AC1 | 2 | 🟢 Small |
| 🟥 Must have | **Navbar and Footer** | AC1, AC2, AC3 | 2 | 🟢 Small |
| 🟥 Must have | **Account registration** | AC1, AC2, AC3 | 5 | 🟡 Medium |
| 🟥 Must have | **Responsive design** | AC1 | 3-5 | 🟡 Medium |
| 🟥 Must have | **Submit recipe posts** | AC1 | 5 | 🟡 Medium |
| 🟥 Must have | **Manage recipe posts** | AC1, AC2, AC3, AC4, AC5 | 8-13 | 🟠 Large |
||||||
| 🟦 Should have| **User submissions control** | AC1, AC2, AC3 | 5 | 🟡 Medium |
| 🟦 Should have | **Modify/Delete comment** | AC1, AC2 | 3 | 🟡 Medium |
| 🟦 Should have| **Approve comments (Admin)** | AC1, AC2 | 3-5 | 🟡 Medium |
| 🟦 Should have| **Comment on a post** | AC1, AC2, AC3 | 8 | 🟠 Large |
||||||
| 🟩 Could have | **Favorite recipes** | AC1, AC2 | 3-5 | 🟡 Medium |
| 🟩 Could have| **Like and dislike posts** | AC1, AC2, AC3 | 5-8 | 🟠 Large |

#### Velocity
<!-- To be completed after the first few iterations -->

### Database Design

#### ERD
![Image of the ERD](/documentation/images/erd.webp)
<!-- replace above image with the final up to date version -->
The application is built around four main entities: 
- **User** - A user can submit recipes, leave comments & favorite recipes and upvote or downvote once on many recipes.
- **Recipe** - A Recipe belongs to one user but can receive many comments, favorites and upvotes/downvotes.
- **Comment** - A comment belongs to one user and can be entered on a single recipe.
- **Favorite** A favorite acts a bridge between User and Recipes. All the favorites will result in a personalized display for each user.

#### Relational Data Model
- Each entity will be stored as a table in the relational CI database PostgreSQL.
- Each record row will represent a single instance of that entity
- Each attribute column will store the data about that record 
- The relationships between the models will be linked using `ForeignKey`'s

#### Database Schema
The application applies a relational scheme which is managed by Django's ORM.
- **Conceptual** - 4 main entities 
- **Logical** - Database tables with relationships between primary keys and foreign keys
- **Physical** - the resulting database created by Django migration

The schema ensures that all the data has a clear and defined structure, which is consistent and simple to query whilst reducing the need to duplicate data requests.

- - -

## UI Design

### Colour Scheme 
I used [coolors.co](https://coolors.co/) to create a colour palette to apply to the site. 

These colours have been selected with the concept of 'farm fresh' in mind. They are vibrant, lively, and are reminiscent of the natural hues commonly seen in a greengrocer’s display, creating an inviting and warm experience for the user.

![colour-palette 1](/documentation/images/colour-palette-1.webp)
![colour-palette 2](/documentation/images/colour-palette-2.webp)

The colours have also been assessed using a contrast checker to ensure they pass all visibility checks and improve user experience. Please see the [Accessibility](#accessibility) section of of this document for results of the contrast checks.

### Typography 
[Google Fonts](https://fonts.google.com/) are used to apply Montserrat for page headings and Montserrat Alternates for body text. These fonts were chosen for their modern and clean appearance, which enhances readability and user experience.

![Image of fonts used](/documentation/images/bugs/font.webp)

### Imagery
Some of the images used throughout the site were sourced from [pexels.com](https://www.pexels.com/). Images from this source are licensed for free use. I have also used [Sora](https://sora.chatgpt.com/explore) to create some AI images.

 [befunky.com](https://www.befunky.com/) has been used to resize the images.

### Wireframes
Wireframes have been created with desktop, tablet and mobile viewports in mind. I have used [Canva](https://www.canva.com/) to plan the layout and user flow of the application.

<details>
<summary>🏡 Homepage when not logged in</summary>

![Wireframe of homepage -  website - when not logged in](/documentation/images/wireframes/website/wireframe-homepage-loggedout-website.webp)
![Wireframe of homepage - tablet - when not logged in](/documentation/images/wireframes/tablet/wireframe-homepage-loggedout-tablet.webp)
![Wireframe of homepage - mobile - when not logged in](/documentation/images/wireframes/mobile/wireframe-homepage-loggedout-mobile.webp)
</details>

<details>
<summary> 🏡 Homepage when logged in</summary>

![Wireframe of homepage -  website - when logged in](/documentation/images/wireframes/website/wireframe-homepage-loggedin-website.webp)
![Wireframe of homepage - tablet - when logged in](/documentation/images/wireframes/tablet/wireframe-homepage-loggedin-tablet.webp)
![Wireframe of homepage - mobile - when logged in](/documentation/images/wireframes/mobile/wireframe-homepage-loggedin-mobile.webp)
</details>

<details>
<summary> 🔐 Login page and Registration page</summary>

![Wireframe of the login page -  website](/documentation/images/wireframes/website/wireframe-loginreg1-website.webp)
![Wireframe of the registration/sign-up page -  website](/documentation/images/wireframes/website/wireframe-loginreg2-website.webp)
![Wireframes of the login page and registration/sign-up page - tablet](/documentation/images/wireframes/tablet/wireframe-loginreg-tablet.webp)
![Wireframes of the login page and registration/sign-up page - mobile](/documentation/images/wireframes/mobile/wireframe-loginreg-mobile.webp)
</details>

<details>
<summary> 🍔 Navigation dropdown </summary>

![Wireframe of the dropdown navigation menu from the burger button - tablet](/documentation/images/wireframes/tablet/wireframe-brgmenu-tablet.webp)
![Wireframe of the dropdown navigation menu from the burger button - mobile](/documentation/images/wireframes/mobile/wireframe-brgmenu-mobile.webp)
</details>

<details>
<summary> 📚 Recipes Hub </summary>

![Wireframe of the recipes hub page -  website](/documentation/images/wireframes/website/wireframe-recipehub-website.webp)
![Wireframe of the recipes hub page - tablet](/documentation/images/wireframes/tablet/wireframe-recipehub-tablet.webp)
![Wireframe of the recipes hub page - mobile](/documentation/images/wireframes/mobile/wireframe-recipehub-mobile.webp)
</details>

<details>
<summary> 📕 Recipe template </summary>

![Wireframe of a template of a recipe page -  website](/documentation/images/wireframes/website/wireframe-recipetemplate-website.webp)
![Wireframe of a template of a recipe page - part 1 - tablet](/documentation/images/wireframes/tablet/wireframe-recipetemplate1-tablet.webp)
![Wireframe of a template of a recipe page - part 2 - tablet](/documentation/images/wireframes/tablet/wireframe-recipetemplate2-tablet.webp)
![Wireframe of a template of a recipe page - part 1 - mobile](/documentation/images/wireframes/mobile/wireframe-recipetemplate-mobile.webp)
![Wireframe of a template of a recipe page - part 2 - mobile](/documentation/images/wireframes/mobile/wireframe-recipetemplate2-mobile.webp)
</details>

<details>
<summary> 📋 Recipe submission form </summary>

![Wireframe of the recipe submission form -  website](/documentation/images/wireframes/website/wireframe-submitrecipe-website.webp)
![Wireframe of the recipe submission form - tablet](/documentation/images/wireframes/tablet/wireframe-submitrecipe-tablet.webp)
![Wireframe of the recipe submission form - part 1 - mobile](/documentation/images/wireframes/mobile/wireframe-submitrecipe-mobile.webp)
![Wireframe of the recipe submission form - part 2 - mobile](/documentation/images/wireframes/mobile/wireframe-submitrecipe2-mobile.webp)
</details>

<details>
<summary> 💁🏽 Your recipes page </summary>

![Wireframe of the personalized your recipes page -  website](/documentation/images/wireframes/website/wireframe-yourrecipes-website.webp)
![Wireframes of the personalized your recipes page - tablet](/documentation/images/wireframes/tablet/wireframe-yourrecipes-tablet.webp)
![Wireframe of the personalized your recipes page - part 1 - mobile](/documentation/images/wireframes/mobile/wireframe-yourrecipes1-mobile.webp)
![Wireframe of the personalized your recipes page - part 2 - mobile](/documentation/images/wireframes/mobile/wireframe-yourrecipes2-mobile.webp)
</details>

- - - 

## Features
### General Features
#### All Pages
<!--  -->

### Accessibility 

During the designing and styling process of the website, I have kept in mind to aim to make the page as user friendly and accessible as possible. I have achieved this by:

* Semantic HTML -Use of descriptive alt attributes on the images used throughout the site. 

* I have checked the colour scheme used on the application using [coolors.co](https://coolors.co/contrast-checker/112a46-acc8e5) to assess the contrast of the colours used. 

<details>
<summary> Click to view results of colour contrast comparison</summary>

![screenshot of colour contrast comparison - 1](/documentation/images/colour-contrast-1.webp)
![screenshot of colour contrast comparison - 2](/documentation/images/colour-contrast-2.webp)
![screenshot of colour contrast comparison - 3](/documentation/images/color-contrast-3.webp) 
![screenshot of colour contrast comparison - 4](/documentation/images/colour-contrast-4.webp)
![screenshot of colour contrast comparison - 5](/documentation/images/color-contrast-5.webp)
</details>

- - - 

## Technologies Used

- **Frontend:** HTML, CSS, Bootstrap, Poppers
- **Backend:** Python, Django, JavaScript
- **Database:** PostgreSQL

![Image of languages used](/documentation/images/languages.webp)
- **Development Tools:**
    - [GitHub](https://github.com/) - for version control
    - [VS Code](https://code.visualstudio.com/) - for development
    - [Canva](https://www.canva.com/) - for wireframes and ERD
    - [Heroku](https://dashboard.heroku.com/) - for deployment 
    - [Favicon.io](https://favicon.io/) - for favicon creation
    - [Google Fonts](https://fonts.google.com/)
    - [Code Institute Pep8 linter](https://pep8ci.herokuapp.com/) for Python validation
    - [W3C HTML Validator](https://validator.w3.org/) for HTML validation
    - [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) for CSS validation
    - Chrome Dev Tools for debugging
    - Chrome Lighthouse for performance testing
    - Node Modules - poppers
    - sqlite3
- **Django Packages**
    - django-allauth
    - django-crispy-forms
    - django-summernote
    - crispy-bootstrap5
    - widgets-tweaks
    - Cloudinary
    - Cloudinary storage
    - WhiteNoise
    - Gunicorn

- - - 

## Deployment

### Fork the Repository
To create your own copy of this project:
1. Log in to GitHub and navigate to the [DishShare repository](https://github.com/Chandni-L5/DishShare)
2. Click the "Fork" button in the top right corner of the page
3. Make your desired changes to your copy of the repository

### Clone the Repository
To create a local copy on your machine:
```bash
git clone https://github.com/Chandni-L5/DishShare
cd DishShare
```

### Deploy to Heroku 

To deploy this project to Heroku, follow these steps:
1. If you don't have one already, create a [Heroku](https://www.heroku.com/) account.
2. Go to the [Heroku dashboard](https://dashboard.heroku.com/apps) and log in.
3. Click the "New" button in the top right corner and select "Create new app".
4. Enter a unique name for your app and select your preferred region.
5. Click "Create app".

6. Please ensure you have completed the following steps before deploying to Heroku:
    1. Install a production ready web server such as Gunicorn by running the following command in your terminal:  
   `pip install gunicorn`
    2. Create a `requirements.txt` file by running the following command in your terminal:  
   `pip freeze --local > requirements.txt`
    3. Create a `Procfile` in the root directory of your project and add the following line:  
   `web: gunicorn dishshare.wsgi`
    5. Ensure your `settings.py` file is configured for production, including setting `DEBUG = False` and add your Heroku app to `ALLOWED_HOSTS = ['.herokuapp.com']`.
    6. Commit and push your changes to your GitHub repository.
7. Return to the Heroku dashboard and navigate to the "Deploy" tab of your app.
8. Under "Deployment method", select "GitHub" and connect your GitHub account if you haven't already.
9. Search for your repository and click "Connect".
10. Go to settings tab and click 'Reveal Config Vars' and add the following:
    - `DATABASE_URL` - your database URL from Heroku Postgres
    - `CLOUDINARY_URL` - your Cloudinary URL for media storage
    - `SECRET_KEY` - a secret key for your Django application

These details will need to be stored in a `.env` file in your local environment.

11. Scroll to the bottom of the page and click 'Deploy Branch' to start a manual deployment of the main branch.
12. Open the Resources tab and ensure that the eco dynos is enabled.
13. Once the deployment is complete, click "View" or "Open app" to see your live application.

This site is deployed via Heroku with PostgreSQL database, Cloudinary for media storage, and Whitenoise for static files.

- - - 

## Testing

### Automated testing 
The automated testing carried out in this project was executed using the SQLite test database which automatically creates and wipes during each run to ensure a fresh and isolated testing environment and specifically verifies the Django based functionality.

The tests cover multiple layers of the application:

1.  Error Handling
    - verified that the custom error templates are displayed correctly when triggered
2. Model classes

    RecipePost
    - successfully creates recipes with valid inputs
    - duration validation - input must be more than 1
    - enforce unique slugs

    Ingredients & Method
    - Automatically increments `order` as items are added 
    - Deletion cascades, when a recipe is removed
    - prevent duplicate combinations

    Comment
    - default to 'draft'
    - returns the correct string representation
    - comments ordered by creation date

3. Views
    - homepage and hub only displays published recipes
    - invalid slugs render 404 error response
    - `edit`/`delete`/`comment`/`submission` functionality is only accessible to logged in users 

4. Forms
    - `RecipePostForm` validate models, forms, views and error handling as expected 
    - invalid data rejected - resulting in appropriate error message 

The code to display the tests is presented within the respective directories and can be identified with the prefix test. 

```
dishshare/
├── accounts/
│ └── tests/
│ ├── test_forms.py
│ └── test_views.py
├── recipe_post/
│ └── tests/
│ ├── test_models.py
│ ├── test_forms.py
│ └── test_errors.py
├── submissions/
│ └── tests/
│ └── test_views.py
```

To run the full test suite, use the following command from the root of the project:

`python manage.py test`

All automated tests have produced a positive result.


### [Manual testing](/documentation/manual_testing.md)

Manual testing was implemented throughout the whole development process of this project. Each item was built incrementally and tested before moving on to the next.

 This iterative approach helped to identify issues early and resolve them along the way. This has resulted in a more stable application as a whole. 

 Nearing the conclusion of the project I have implemented a more structured approach to the manual testing to verify that all the features have achieved the intended requirements and behave as expected under different conditions. The tests are based on the expected outcome of each feature and  the full breakdown of the manual tests are displayed [here](/documentation/manual_testing.md). 

### Testing User Stories
<!--  -->

### Fixing Bugs

A number of bugs were encountered and resolved during the development of this project. The most significant bugs are outlined below along with the steps taken to resolve them.

You can view the full list of bugs encountered and resolved during the development of this project [here](/documentation/bugs.md).


### Lighthouse
<!--  -->

### Validation 
<!--  -->

### W3C HTML and CSS Testing 
<!--  -->

### Autoprefixer CSS 
<!--  -->

--- 
## Future Implementations
<!--  -->
--- 

## Credits

### Code Used
<!--  -->

### Content
- [Chatgpt](https://chatgpt.com/) 
- [Google fonts](https://fonts.google.com/) 
- [Favicon.io](https://favicon.io/emoji-favicons/) - to create an emoji favicon


### Media
<!-- - [Font Awesome](https://fontawesome.com/) -->
- [befunky.com](https://www.befunky.com/dashboard/) - to resize images
- [pexels.com](https://www.pexels.com/) - to source images
- [Sora](https://sora.chatgpt.com/explore) - to create AI images
- [Cloudconvert](https://cloudconvert.com/jpg-to-webp) - to convert images to different file types. 
- [toWebP](https://towebp.io/) - to convert different file types

### Documentation and testing
I have used the following sources to help guide and structure the documentation of this project.
- [The love running readme template](https://github.com/Code-Institute-Solutions/readme-template?tab=readme-ov-file) 
- [A markdown cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#tables)
- [Kera Cudmore's readme template](https://github.com/kera-cudmore/readme-examples/blob/main/milestone1-readme.md) - shared on slack
- [Diffchecker](https://www.diffchecker.com/)
- [W3C](https://validator.w3.org/)
-[Autoprefixer](https://autoprefixer.github.io/)
- [Gyazo](https://gyazo.com/en) plugin- to create gifs to use in the testing documentation
- [Web Disability Simulator](https://chromewebstore.google.com/detail/web-disability-simulator/olioanlbgbpmdlgjnnampnnlohigkjla) 
- [Amiresponsive](https://ui.dev/amiresponsive) - to show the website on a range of device screens
- [coolors.co](https://coolors.co/contrast-checker/112a46-acc8e5) - to compare colour contrast
- [Canva](https://www.canva.com/) - to create wireframes and ERD

#### Resources
- [stackoverflow.com](https://stackoverflow.com/questions/25744425/how-to-clean-up-django-login-message-from-framework?utm_source=chatgpt.com) - to manipulate the messages in Django
- [allauth documentation](https://pypi.org/project/django-allauth/0.17.0/?utm_source=chatgpt.com)
- [geeksforgeeks.org](https://www.geeksforgeeks.org/python/python-extending-and-customizing-django-allauth/)
- [stackoverflow.com](https://stackoverflow.com/questions/45225384/django-messages-how-to-hide-specific-ones?utm_source=chatgpt.com) - to hide specific messages
- [Django formsets documentation](https://docs.djangoproject.com/en/4.2/topics/forms/formsets/)
- [Stack Overflow - Django inline formsets](https://stackoverflow.com/questions/29758558/inlineformset-factory-create-new-objects-and-edit-objects-after-created)
- [Dennis Ivy - How to use Django inline formsets tutorial](https://www.youtube.com/watch?v=MRWFg30FmZQ)
- [dev.to blog](https://dev.to/zxenia/django-inline-formsets-with-class-based-views-and-crispy-forms-14o6)

### Acknowledgements
<!--  -->
