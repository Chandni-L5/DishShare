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
<!--  -->

### Imagery
<!--  -->

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

 ![screenshot of colour contrast comparison - 1](/documentation/images/colour-contrast-1.webp)
![screenshot of colour contrast comparison - 2](/documentation/images/colour-contrast-2.webp)
![screenshot of colour contrast comparison - 3](/documentation/images/color-contrast-3.webp) 
![screenshot of colour contrast comparison - 4](/documentation/images/colour-contrast-4.webp)
![screenshot of colour contrast comparison - 5](/documentation/images/color-contrast-5.webp)

- - - 

## Technologies Used

### Languages Used 
<!--  -->

### Frameworks, Libraries & Programs Used
<!--  -->

- - - 

## Deployment
<!--  -->

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
<!--  -->

### Media 
<!--  -->

### Documentation and Testing 
<!--  -->

### Acknowledgements
<!--  -->
