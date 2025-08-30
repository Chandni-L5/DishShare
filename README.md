# DishShare

[DishShare](https://dishshare-d8c892b46f87.herokuapp.com/) is a Django based website designed to bring together a community of homecooks and amateur chefs. This platform provides users with the ability to create, share and discover new recipes whilst engaging with other users through comments, likes and dislikes. 

Whether you are seeking inspiration for your next meal or want to showcase your culinary creativity, DishShare makes it easier to connect with food lovers across the world at your fingertips. 

<!-- Insert AmIResponsive image here -->

- - -

## User Experience (UX) & Agile Planning and Development

### Goals and Objectives 
The aim of this website is to provide an intuitive, responsive and rich community focussed platform to connect, share and discover content. 

Users are able to log in and create a personalized list of their favorite item, submit their own content, and interact with other user's contents through the format of likes, dislikes and comments.

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

📚 The epics can be viewed [here](/documentation/epics.md)

📓 The user stories can be viewed [here](/documentation/user-stories.md)

 The implementation and prioritization of user stories as well as the acceptance criteria is recorded and tracked dynamically through the use of GitHub Projects Kanban board. The Kanban board records the user story, acceptance criteria and tasks. These are checked off as we progress through the project.

📊 The board can be viewed [here](https://github.com/users/Chandni-L5/projects/11/views/3)

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

- - -

## Design

### Colour Scheme 
I used [coolors.co](https://coolors.co/) to create a colour palette to apply to the site. 

These colours have been selected with the concept of 'farm fresh' in mind. They are vibrant, lively, and are reminiscent of the natural hues commonly seen in a greengrocer’s display, creating an inviting and warm experience for the user.

![colour-palette 1](/documentation/images/colour-palette-1.webp)
![colour-palette 2](/documentation/images/colour-palette-2.webp)

The colours have also been assessed using a contrast checker to ensure they pass all visibility checks and improve user experience. Please see the [Accessibility](#accessibility) section of of this document for results of the contrast checks.

### Typography 
[Google Fonts](https://fonts.google.com/) are used to apply the following fonts:

#### Montserrat 
<!-- insert images of examples and text to explain why this one has been selected -->

#### Montserrat Alternates
<!-- insert images of examples and text to explain why this one has been selected -->

### Imagery
Some of the images used throughout the site were sourced from [pexels.com](https://www.pexels.com/). Images from this source are licensed for free use.

I also used [befunky.com](https://www.befunky.com/) to resize the images.

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

### Data Model
#### ERD

### General Features
#### All Pages
<!--  -->

### Future Implementations
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

- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Backend:** Python, Django 
- **Database:** PostgreSQL
- **Development Tools:**
    - [GitHub](https://github.com/) - for version control
    - [VS Code](https://code.visualstudio.com/) - for development
    - [Canva](https://www.canva.com/) - for wireframes
    - [Heroku](https://dashboard.heroku.com/) - for deployment 
    - [Favicon.io](https://favicon.io/) - for favicon creation
    - [Google Fonts](https://fonts.google.com/)
    - [Code Institute Pep8 linter](https://pep8ci.herokuapp.com/) for Python validation
    - [W3C HTML Validator](https://validator.w3.org/) for HTML validation
    - [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) for CSS validation
    - Chrome Dev Tools for debugging
    - Chrome Lighthouse for performance testing
- **Django Packages**
    - django-allauth
    - django-crispy-forms
    - Cloudinary storage
    - WhiteNoise
    - Gunicorn

- - - 

## Deployment

### Deploy to GitHub

1. Log in to GitHub and navigate to the [DishShare repository](https://github.com/Chandni-L5/DishShare)
2. Click the settings button.
3. Select pages in the left hand navigation menu. 
4. From the source dropdown select 'Deploy from a branch' and in the branch dropdown select 'main' and press save.
5. The site has now been deployed.
6. When returning to the code page in the repository a Deployments section will appear in the right side column - this process may take a few minutes before the site goes live. The deployed sight can be accessed via this link.

### Deploy to Heroku 
Deployed to Heroku:

1. Create a new Heroku app.
2. Connect the app to this GitHub repo.
3. Set Config Vars (see below).
4. Push to main to trigger a build & deploy.

This site is deployed via Heroku with PostgreSQL database, Cloudinary for media storage, and Whitenoise for static files.

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

- - - 

## Testing

### Testing User Stories
<!--  -->

### Fixing Bugs
<!--  -->

### Manual Testing 
<!--  -->

### Lighthouse
<!--  -->

### Validation 
<!--  -->

### W3C HTML and CSS Testing 
<!--  -->

### Autoprefixer CSS 
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
- [Cloudconvert](https://cloudconvert.com/jpg-to-webp) - to convert images to different file types. 

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
- [Canva](https://www.canva.com/) - to create wireframes 

### Acknowledgements
<!--  -->
