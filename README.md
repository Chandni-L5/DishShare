# DishShare

[DishShare](https://dishshare-d8c892b46f87.herokuapp.com/) is a full-stack recipe sharing platform built with Django, designed to bring together a community of homecooks and amateur chefs. This platform provides users with the ability discover, submit, and manage their own recipes whilst engaging with other users through comments, likes and dislikes. 

Whether you are seeking inspiration for your next meal or want to showcase your culinary creativity, DishShare makes it easier to connect with food lovers across the world at your fingertips. 

![amiresponsive screenshot](/documentation/images/amiresponsive.webp)

[Click here to view the deployed site.](https://dishshare-d8c892b46f87.herokuapp.com/)
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

During planning, the MoSCoW priorities were distributed as 46% Must have, 34% Should have, and 20% Could have.

[Please see 'Testing User Stories' section for the results and completion of the user stories.](#testing-user-stories)

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
| 🟦 Should have| **Comment on a post** | AC1, AC2, AC3 | 3 | 🟡 Medium |
||||||
| 🟩 Could have | **Comment String** | AC1, AC2, AC3 | 3-5 | 🟡 Medium |
| 🟩 Could have | **Favorite recipes** | AC1, AC2 | 3-5 | 🟡 Medium |
| 🟩 Could have| **Like and dislike posts** | AC1, AC2, AC3 | 5-8 | 🟠 Large |

### Database Design

#### ERD
![Image of the ERD](/documentation/images/erd.webp)

The application is built around four main entities: 
- **User** - A user can submit recipes, leave comments & favorite recipes and upvote or downvote once on many recipes.
- **Recipe** - A Recipe belongs to one user but can receive many comments, favorites and upvotes/downvotes.
- **Comment** - A comment belongs to one user and can be entered on a single recipe.
- **Favorite** A favorite acts a bridge between User and Recipes. All the favorites will result in a personalized display for each user.

As the project has progressed the above ERD has been deprecated as further explained in the [testing bugs section](/documentation/bugs.md) and the [final summary](#final-summary--future-implementations). The updated ERD is shown below:

![Image of the updated ERD model](/documentation/images/final-erd.webp)

The current version of the application is built around three main entities:
- **User** - A user can submit recipes, leave comments.
- **Recipe** - A Recipe belongs to one user but can receive many comments.
- **Comment** - A comment belongs to one user and can be entered on a single recipe.

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

### All Pages
- Consistent navbar and footer across all pages 
- Navbar contains links to the main pages of the site and changes depending on logged in status
- Footer contains links to social media
- Responsive design across different devices and screen sizes
- Use of Bootstrap framework to ensure responsive design across different devices and screen sizes.
- Use of legible fonts and appropriate font sizes to enhance readability.

#### Navbar

All pages contain a consistent navbar and footer. The navbar contains links to the main pages of the site and changes depending on logged in status and also includes some personalization specific to that user. The nav-links available to a logged in user ensures that users can only access pages that are specific to them as well as the universal pages available to all. The navbar is responsive and collapses into a burger menu on smaller screens.

The navbar aligns with the overall colour scheme of the site and uses hover effects to enhance user experience.

The user account & authentication Epic and the User Engagement Epic are both considered in the design of the navbar.

<details>
<summary>Click to expand</summary>

##### Navbar as a logged out user
<u>Larger screens</u>

![screenshot of navbar on larger screens](/documentation/images/features/lg-nav-lo.png)

<u>Smaller screens</u>  

![screenshot of navbar on smaller screens](/documentation/images/features/sm-nav-lo.webp)
![gif of dropdown from navbar on smaller screens](/documentation/images/features/brg-lo.gif)

#### Navbar as a logged in user
<u>Larger screens</u>

![screenshot of navbar on larger screens](/documentation/images/features/lg-nav.webp)
![gif of dropdown from navbar on larger screens](/documentation/images/features/nav-drop.gif)

<u>Smaller screens</u>  

![screenshot of navbar on smaller screens](/documentation/images/features/brg-sm.webp)
</details>

#### Footer
The footer is consistent across all pages and contains links to social media. The footer aligns with the overall colour scheme of the site and uses hover effects to enhance user experience.

<details>
<summary>Click to expand</summary>

![screenshot of footer](/documentation/images/features/lg-footer.png)
![screenshot of footer on smaller screens](/documentation/images/features/sm-footer.webp)
</details>

### Account Management
The account management functionality is provided by the Django Allauth package. This package provides a robust and secure authentication system that includes features such as login, logout and registration.

The account management Epic is considered in the design of the account management functionality.

The user is able to access the registration and login pages from the navbar when logged out. Once logged in the user is able to log out from the navbar. There are also some additional buttons displayed on the homepage to direct a user to the appropriate page depending on their logged in status.

The system will also display a status message in the top right of the screen which displays for 5 seconds every time a page loads throughout the application. 

<details>
<summary>Click to expand</summary>

![screenshot of registration page](/documentation/images/features/registration.webp)
</details>

All of the fields in the registration form are required. The password field has a minimum length of 8 characters and the email field must be a valid email address. The form will not be submitted if any of the fields are invalid or empty and an appropriate error message will be displayed.

The user is redirected to the homepage upon successful registration and a success message is displayed. 

<details>
<summary>Click to expand</summary>

![screenshot of login page](/documentation/images/features/login.webp)
</details>

The login form requires the user to enter their username and password. If the credentials are incorrect an appropriate error message is displayed. The user is redirected to the homepage upon successful login and a success message is displayed.

![screenshot of login message](/documentation/images/features/li-msg.webp)

<details>
<summary>Click to expand</summary>

![screenshot of logout confirmation page](/documentation/images/features/logout.webp)
</details>

When the user clicks on the logout button in the navbar they are redirected to a logout confirmation page. The user is logged out when they click the logout button on this page and a success message is displayed.
![screenshot of logout message](/documentation/images/features/lo-msg.webp)

#### Homepage

The homepage displays different content depending on the logged in status of the user. 

When logged out the homepage displays a welcome message and buttons to direct the user to the login or registration pages.

![gif of homepage when logged out and displaying the random selection on refresh](/documentation/images/features/hm-rdm.gif)

An additional feature implemented on the home page is the random recipe selection that is displayed and updated each time the page is refreshed. This feature encourages user engagement and exploration of the site. This was a last minute addition as I was unable to implement the like and dislike feature as originally intended which would in turn display the most liked recipes on the homepage.

When logged in the homepage displays a welcome message with the user's username and buttons to direct the user to the recipes hub or to the submit recipe page.

<details>
<summary>Click to expand</summary>

![gif of homepage when logged in](/documentation/images/features/li-hm.webp)

<u> Medium and smaller screens</u>

![screenshot of homepage when logged out on medium screen](/documentation/images/features/lo-tab-hm.webp) ![screenshot of homepage when logged out on medium screen](/documentation/images/features/li-tab-hm.webp) ![screenshot of homepage when logged in on smaller screen](/documentation/images/features/lo-mob-hm.webp) ![screenshot of homepage when logged in on smaller screen](/documentation/images/features/li-mob-hm.webp)

</details>

#### Recipe Hub 
The recipe hub displays all published recipes in a card format. Each card displays the recipe title, image and a short description. The user is able to click on the card to view the full recipe.

This is a universal page that can be accessed by all users regardless of their logged in status.

<details>
<summary>Click to expand</summary>

![screenshot of recipe hub on larger screens](/documentation/images/features/rp-lg.webp)![screenshot of recipe hub on medium screens](/documentation/images/features/rp-tab.webp) ![screenshot of recipe hub on smaller screens](/documentation/images/features/rp-mob.webp)
</details>


#### Individual Recipe Page
The individual recipe page displays the full recipe including the title, image, description, ingredients and method. The page also displays comments from other users and a form to submit a new comment.

If the user is the author of the recipe, they will see buttons to edit and delete the recipe.

<details>
<summary>Click to expand</summary>

![screenshot of recipe page on larger screen 1](/documentation/images/features/rp-pg.webp)
![screenshot of recipe page on larger screen 2](/documentation/images/features/rp-web.webp) ![screenshot of recipe page on medium screen 1](/documentation/images/features/rp-tab1.webp) ![screenshot of recipe page on medium screen 2](/documentation/images/features/rp-tab2.webp) ![screenshot of recipe page on smaller screen 1](/documentation/images/features/rp-mob1.webp) ![screenshot of recipe page on smaller screen 2](/documentation/images/features/rp-mob2.webp)
</details>

#### Comments 
The comments section allows users to leave comments on a recipe. The comments are displayed in reverse chronological order with the most recent comment at the top. There is also a count of the total number of comments displayed at the top of the section.

If the user is the author of the comment, they will see buttons to edit and delete the comment. When selecting the edit button, the comment text is replaced with a form to edit the comment. The user is redirected to the same page upon successful edit and a success message is displayed.

<details>
<summary>Click to expand</summary>

![screenshot of comments section 1](/documentation/images/features/comment.webp) ![screenshot of comments section 2](/documentation/images/features/comment-edit.webp)
</details>

#### Submission Form 

The submission form allows logged in users to submit their own recipes. The form includes fields for the recipe title, description, image, ingredients and method. The ingredients and method fields are implemented using Django formsets to allow the user to add multiple ingredients and steps.

The form includes validation to ensure that all fields are filled out correctly. The user is redirected to the recipe hub upon successful submission and a success message is displayed.

<details>
<summary>Click to expand</summary>

![gif of submission form on a mobile screen](/documentation/images/features/form.gif)
![screenshot of submission form on medium screens](/documentation/images/features/sub-tab.webp) ![screenshot of submission form on larger screens](/documentation/images/features/sub-web.webp)
</details>

The user also has the ability to edit and delete their own recipes from the 'my submissions' page. The edit form is pre-populated with the existing data and includes the same validation as the submission form. The user is redirected to the recipe detail page upon successful edit and a success message is displayed. 

<details>
<summary>Click to expand</summary>

![screenshot of edit form on larger screen](/documentation/images/features/edit1.webp) ![screenshot of edit form on larger screen](/documentation/images/features/edit2.webp)
</details>

#### Modal
A custom modal is displayed to confirm deletion of a recipe and comments to prevent accidental deletions. The modal includes buttons to confirm or cancel the deletion. On confirmation the user is redirected to the recipe hub and a success message is displayed.

<details>
<summary>Click to expand</summary>

![screenshot of deletion modal](/documentation/images/features/rp-mod.webp) ![screenshot of comment modal](/documentation/images/features/cmt-mod.webp)
</details>

#### Success Messages
The application uses Django messages to provide feedback to the user on the success or failure of actions such as submission, edit and deletion of posts and comments. 

This has been enhanced with custom styling and some JavaScript functionality to match the overall design of the site and improve user experience.

<details>
<summary>Click to expand</summary>

![screenshot of success message1](/documentation/images/features/cm-del-msg.webp) ![screenshot of success message2](/documentation/images/features/cm-suc-msg.webp) ![screenshot of success message3](/documentation/images/features/sub-msg.webp) ![screenshot of success message4](/documentation/images/features/up-msg.webp)
</details>

#### Admin Interface
The admin interface allows admin users to manage the content of the site. Admin users can view, edit and delete recipes and comments, as well as keep track of the users. The admin interface is protected by Django's built-in authentication system to ensure that only authorized users can access it. 

The layout of the recipe and comment models have been customized to improve usability for admin users. Particularly the recipe model which includes inline display of the ingredients and method steps similarly to the front end interface.

When I initially embarked on this project the ingredients and method steps were set as `TextField`'s in the recipe model. However, as the project progressed and I began testing the functionality, I realized that this approach was not optimal for user experience. Find out more about this and the changes made to produce this current version of the application in the [Testing Bugs](/documentation/bugs.md) section.

<details>
<summary>Click to expand</summary>

![screenshot of admin interface landing page](/documentation/images/features/ad-lp.webp) 
![screenshot of admin interface users](/documentation/images/features/ad-user.webp) 
![screenshot of admin interface recipe model 1](/documentation/images/features/ad-rp.webp) 
![screenshot of admin interface recipe model 2](/documentation/images/features/ad-rp2.webp) 
![screenshot of admin interface recipe model 3](/documentation/images/features/ad-rp3.webp) 
![screenshot of admin interface comment model 1](/documentation/images/features/ad-cmt.webp) 
![screenshot of admin interface comment model 2](/documentation/images/features/ad-cmt2.webp)
</details>

### Defensive Design & Permissions

#### Allauth-gated actions
- Only logged in users can submit, edit, delete posts and comments.
- Admin users can delete inappropriate posts and comments from the admin interface.

#### Ownership-based permissions
- Only the author of a recipe or comment can edit or delete it.
- Only the author of a recipe or comment can see the edit and delete buttons.
- Users can access a personal list of their own submitted recipes. 
- The application uses Django messages to provide feedback to the user on the success or failure of actions such as login, logout, submission, edit and deletion of posts and comments.

#### Deletion confirmation
- A custom modal is displayed to confirm deletion of a recipe or comment to prevent accidental deletions, on confirmation the user is redirected to an appropriate page and a success message is displayed.

#### UX extras
- A custom success message is displayed on login and logout to confirm the action has been successful.
- When logged in the navbar displays the user's username to add an additional confirmation of the logged in status.
- The navbar displays different options depending on the logged in status of the user.
    - When logged out the options are: Home, Recipes, Login, Register
    - When logged in the options are: Home, Recipes, Submit Recipe, Your Recipes, Logout

### Accessibility 

During the designing and styling process of the website, I have kept in mind to aim to make the page as user friendly and accessible as possible. I have achieved this by:

* Semantic HTML -Use of descriptive alt attributes on the images used throughout the site. 
* Use of ARIA labels to improve accessibility for screen readers.
* Use of Bootstrap framework to ensure responsive design across different devices and screen sizes.
* Use of legible fonts and appropriate font sizes to enhance readability.
* Consistent navigation structure across all pages.
* Alt text for all images.
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

| Requirement | User Story | Test Result |
|------------|-------------------|------------|
| 🟥 Must have | **Open a post** | 	✅ Pass |
| 🟥 Must have | **Navbar and Footer** | 	✅ Pass |
| 🟥 Must have | **Account registration** | ✅ Pass |
| 🟥 Must have | **Responsive design** | 	✅ Pass |
| 🟥 Must have | **Submit recipe posts** | 	✅ Pass |
| 🟥 Must have | **Manage recipe posts** | 	✅ Pass |
||||||
| 🟦 Should have| **User submissions control** | ✅ Pass |
| 🟦 Should have | **Modify/Delete comment** | 	✅ Pass |
| 🟦 Should have| **Approve comments (Admin)** | 	✅ Pass |
| 🟦 Should have| **Comment on a post** | ✅ Pass |
||||||
| 🟩 Could have | **Favorite recipes** | Not Implemented |
| 🟩 Could have| **Like and dislike posts** | Not Implemented |
| 🟩 Could have | **Comment String** | Not Implemented |

The user stories are all complete apart from the 'like and dislike posts' and 'favorite recipes' features which have not been implemented due to time constraints. 

In addition the acceptance criteria for the 'comment on a post' user story has only been partially met. The user is able to comment on a post and the comment is displayed once approved by an admin user. However, the user not able to reply to others comments as originally intended. 

### [Fixing Bugs](/documentation/bugs.md)

A number of bugs were encountered and resolved during the development of this project. The most significant bugs are outlined below along with the steps taken to resolve them.

You can view the full list of bugs encountered and resolved during the development of this project [here](/documentation/bugs.md).


### [Lighthouse](/documentation/lighthouse.md)
Lighthouse has been used to test the performance, accessibility and best practices. The results of the tests have been used to identify areas for improvement and optimize the overall user experience.

Please click here to view the [Lighthouse reports](/documentation/lighthouse.md).

### [Validation](/documentation/validation.md) 

The code has been validated using the following tools:
- [W3C Markup Validation Service](https://validator.w3.org/) - to ensure HTML validity
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - to ensure CSS validity
- [PEP8 Online](http://pep8online.com/) - to ensure Python code follows PEP8 standards
- [Django Linter](https://pep8ci.herokuapp.com/) - to ensure Python

[Please click here to view the validation checks and results.](/documentation/validation.md)

--- 
## Final Summary & Future Implementations

This project has been a valuable learning experience, allowing me to apply and expand my skills in Django and full-stack web development. I have gained a deeper understanding of database design, user authentication, and responsive design principles.

I have successfully met its primary objectives, providing a functional and user-friendly platform for recipe sharing. However the criteria of the planned user stories have not been fully met due to time constraints.

In future iterations, I would like to implement the following features:
- Improve the commenting system to allow users to reply to others comments.
- Implement the 'like and dislike' feature for posts.
- Implement the 'favorite recipes' feature.
- Add user profile pages to allow users to manage their account and view their activity.
- Enhance the search and filtering capabilities to improve content discovery.

--- 

## Credits
### Content
- [Chatgpt](https://chatgpt.com/) 
- [Google fonts](https://fonts.google.com/) 
- [Favicon.io](https://favicon.io/emoji-favicons/) - to create an emoji favicon


### Media
- [Font Awesome](https://fontawesome.com/)
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
- [stackoverflow.com](https://stackoverflow.com/questions/25744425/how-to-clean-up-django-login-message-from-framework?utm_source=chatgpt.com) 
- [allauth documentation](https://pypi.org/project/django-allauth/0.17.0/?utm_source=chatgpt.com)
- [geeksforgeeks.org](https://www.geeksforgeeks.org/python/python-extending-and-customizing-django-allauth/)
- [stackoverflow.com](https://stackoverflow.com/questions/45225384/django-messages-how-to-hide-specific-ones?utm_source=chatgpt.com)
- [Django formsets documentation](https://docs.djangoproject.com/en/4.2/topics/forms/formsets/)
- [Stack Overflow - Django inline formsets](https://stackoverflow.com/questions/29758558/inlineformset-factory-create-new-objects-and-edit-objects-after-created)
- [Dennis Ivy - How to use Django inline formsets tutorial](https://www.youtube.com/watch?v=MRWFg30FmZQ)
- [dev.to blog](https://dev.to/zxenia/django-inline-formsets-with-class-based-views-and-crispy-forms-14o6)
- [crispy forms documentation](https://django-crispy-forms.readthedocs.io/en/latest/crispy_tag_formsets.html#formset-forms-with-different-layouts)

### Acknowledgements
Special thanks to mentors and peers who provided valuable feedback and guidance during development.
