# Recipie 🥧

## Introduction 📜

Welcome to **Recipie**! Dive deep into a world exclusively crafted for pie enthusiasts, where every recipe, filling, crust, and comment is dressed in the most refined and user-friendly designs. With colors emanating warmth and typography exuding sophistication, we've ensured that our pie universe is baked to perfection!

[View the live website on Heroku](https://hannas-recipie-e418bd744fab.herokuapp.com/)

Please note: To open any links in this document in a new browser tab, please press CTRL + Click.

---

## Table of Contents 📖
[Recipie](#Recipie)
 * [Introduction](#introduction-)
 * [UX](#ux-)
   + [Overall Goals](#overall-goals)
   + [The Strategy Plane](#the-strategy-plane)
   + [The Site's Ideal User](#the-sites-ideal-user)
   + [Site Goals](#site-goals)
* [Strategy, Epics & User Stories](#strategy-epics-and-user-stories)
   + [Strategy](#strategy)
   + [Epics and User Stories](#epics-and-user-stories)
   + [The Scope Plane](#the-scope-plane)
   + [The Structure plane](#the-structure-plane)
   + [The Skeleton Plane](#the-skeleton-plane)
      + [Wireframe mock-ups](#wireframe-mock-ups)
   + [The Surface Plane](#the-surface-plane)
      + [Design](#design)
      + [Typography](#typography)
      + [Images](#images)
* [Features](#features-🛠️)
   + [Interactive Imagery](#interactive-imagery)
   + [Engaging Buttons](#engaging-buttons)
* [Future Enhancements](#future-enhancements-🚀)
* [Social Media Integration](#social-media-integration-🌐)
* [Testing Protocols](#testing-protocols-🧪)
* [Deployment Guidelines](#deployment-guidelines-🚀)

---

## UX 🖥️

### Overall Goals

- To create a centralized platform exclusively for pie recipes, catering to baking enthusiasts worldwide.
- To foster a community-driven approach where users can register, comment, and like existing recipes.
- To provide recipe authors acknowledgment through author highlights and recognition systems.
- To create an intuitive and visually appealing user interface, ensuring a seamless recipe discovery experience.

---

### The Strategy Plane

ReciPie serves as a dedicated platform for pie enthusiasts, both amateur bakers and professionals. For the user, it's an avenue to discover, appreciate, and interact with an array of pie recipes, leave feedback, and mark their favorites. As for recipe authors, it provides them with a platform to showcase their culinary skills and receive direct feedback from the community. The overall design and user experience have been meticulously crafted, ensuring that visitors find it both captivating and user-friendly. 

---

### The Site's Ideal User

- Baking hobbyists eager to try out new pie recipes.
- Professional bakers or culinary students looking for inspiration or innovative takes on classic pies.
- Users wanting to share their cherished family pie recipes with a broader audience.
- Visitors interested in providing feedback, sharing their baking experiences, or simply liking their favorite pie recipes.

---

### Site Goals

- To establish ReciPie as the go-to platform for discovering and sharing pie recipes.
- To nurture a vibrant community where bakers can exchange tips, feedback, and innovations.
- To promote user interactivity through features like comments, likes, and future provisions for recipe submissions.
- To gradually expand the recipe catalog, branching into broader dessert and baking categories, solidifying ReciPie's place in the culinary online world.

---

## Strategy, Epics and User Stories

### Strategy

ReciPie aims to be the go-to platform for pie enthusiasts everywhere. A space where users can not only view delicious pie recipes but also interact by commenting and liking. As the site grows, the vision is to allow users to upload their own recipes, expanding beyond pies to encompass a broader range of desserts and baked goods.

---

### Epics and User Stories Table

| Type  | Name                                      | Description                                                                                                                                                                 |
|-------|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Epic**     | Model development                    | As a developer, I want to design and implement a comprehensive and intuitive recipe model in the database.                                                                  |
| **Epic**     | Model management endpoints development | As a developer, I want to provide endpoints for CRUD operations on recipes.                                                                                                 |
| **Epic**     | View & Interact                      | As a User, I can view recipes and interact with the content.                                                                                                                |
| **User Story** | View a Recipe                       | As a Site User, I can click on a recipe to read the full text.                                                                                                              |
| **User Story** | Approve comments                    | As a Site Admin, I can approve or disapprove comments to filter out objectionable content.                                                                                   |
| **User Story** | View rating                         | Both Site Users and Admins can view the rating on each recipe to gauge popularity.                                                                                          |
| **User Story** | List recipes                        | As a Site Admin, I can list recipes from the database.                                                                                                                      |
| **User Story** | Account registration                | As a Site User, I can register an account to comment and like.                                                                                                              |
| **User Story** | View comments                       | Both Site Users and Admins can view comments on a post to engage in the conversation.                                                                                       |
| **User Story** | Get comment                         | As a Site Admin, I can retrieve a specific comment.                                                                                                                         |
| **User Story** | List comments                       | As a Site Admin, I can list all comments.                                                                                                                                   |
| **User Story** | Get recipe                          | As a Site Admin, I can retrieve a specific recipe from the database.                                                                                                        |
| **User Story** | Update recipe                       | As a Site Admin, I can update specific recipes in the database.                                                                                                             |
| **User Story** | Create recipe                       | As a Site Admin, I can add new recipes to the database.                                                                                                                     |
| **User Story** | Delete recipe                       | As a Site Admin, I can remove recipes from the database.                                                                                                                    |
| **User Story** | Create comment model                | As a developer, I want to design a comment model with fields like author, content, and creation date.                                                                       |
| **User Story** | Create a recipe model               | As a developer, I aim to design a Recipe model with fields such as title, description, ingredients, and more.                                                               |
| **User Story** | View recipes                        | As a Site User, I can browse through a list of recipes.                                                                                                                     |
| **User Story** | Like/unlike a recipe                | As a Site User, I can rate a recipe to express my appreciation or criticism.                                                                                                |

By addressing these epics and user stories, ReciPie aims to offer an engaging and interactive experience to users while ensuring robust backend functionality for administrators and developers.

---

### The Scope Plane

<br>

#### Opportunities
Arising from user stories
| Opportunities | Importance | Viability / Feasibility
| ------ | :------: | :------: |
| **Allow users to save their favorite recipes** | 5 | 5 |
| **Enable users to edit their profile** | 5 | 5 |
| **Allow users to delete their profile** | 5 | 5 |
| **Allow users to view recipe author profiles** | 4 | 5 |
| **Provide users the ability to access the site on any device** | 5 | 5 |
| **Enable users to post their own recipes** | 5 | 4 |
| **Allow site admins to highlight top-rated or featured recipes** | 4 | 5 |

**Features currently implemented:**
* User Profile - Create an account and log in/out
* Comment on Recipes - Users can already post comments
* Recipe Likes - Ability to like and unlike recipes
* View Detailed Recipe Information - Detailed views of individual recipes

**Features planned:**
* User Profile - Edit and Delete
* Favorite Recipes - Save, View, and Remove
* Users can post their own recipes
* Contact Form - Ability for all users to contact the website administrators or recipe authors.
* Responsive Design - Ensuring the site remains fully responsive to cater to a variety of devices users may access it from.


---

### The Structure Plane

ReciPie is designed with the end user's experience at its core. The platform aims to be intuitive and user-friendly, allowing visitors to effortlessly navigate through a rich repository of recipes. These are the defining aspects:

- **Organization and Hierarchy**: The site is structured to prioritize easy access to recipes. Recipes are categorized logically, allowing users to browse or dive straight into their desired cuisine or dish type.

- **Visual Appeal**: Incorporating elements like `.image-flash-likes` ensures that the most popular recipes get the spotlight they deserve. Through this dynamic visualization, recipes that garner more attention and likes from the community are immediately noticeable.

- **Feature Highlights**: Our `.masthead-featured-image` is strategically placed to spotlight the star recipes. This might be a dish that's currently trending, a seasonal favorite, or a timeless classic that's a must-try.

- **Interactivity**: While the platform focuses on the visual appeal and structured presentation of the recipes, it also integrates interactivity. Users are encouraged to engage with content, be it through liking a recipe or diving deep into the ingredient list and instructions.

By blending organization with captivating visuals and dynamic elements, ReciPie offers an immersive culinary journey for every visitor.

---

### The Skeleton Plane

#### Wireframe mock-ups

Wireframes were produced for most pages, excluding those primarily containing forms, like the add product page. A comprehensive PDF with all wireframes is available [here](/static/docs/wireframes.pdf).

Detailed attention was directed towards universal elements on each page, notably the header and the footer. The header incorporates multiple layers of navigation, ensuring users can quickly access account information while being distinct from primary navigation. For mobile and tablet, a horizontal bar in the main menu differentiates these, while on desktop the account-related navigation is positioned above the main site links.

---

## The Surface Plane

### Design

Once I was happy with the overall structure of the site, and the layout of the wireframes, I selected a colour scheme based on a desire for a simple and clean aesthetic. The site incorporates two main colours, blue and white, although specific shades were selected for various different areas, they all remained within the blue family. Blue was chosen due to the fictional business base location and the county colours are blue and white. The white or off white shades are tinted with a little blue to maintain consistency. The colour scheme was referenced using the [contrast grid](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%23FFFFFF%2C%20White%0D%0A%23000000%2C%20Black%0D%0A%2303045E%2C%20Primary%0D%0A%23f2f4f8%2C%20Primary-text%0D%0A%23c7ccdb%2C%20Secondary%0D%0A%23f7c59f%2C%20Accent%0D%0A%2370ae6e%2C%20Success%0D%0A%23ef626c%2C%20Error%0D%0A%231188a0%2C%20Info%0D%0A%23f3c178%2C%20Warning) which provides a grid of colour contrasts to ensure only those which would easily pass the AAA standard were selected to maximise accessibility for users.

![Colour Contrast Grid](/static/docs/img/contrast-grid.png)

### Typography 

Three different fonts were utilised for the site. The main heading font of Orbitron and the smaller subheading font of Economica were selected for their futuristic almost technical feeling whilst Montserrat was chosen as a complimentary font which allowed users the ability to read the text easily and clearly.

#### Images

Background images were acquired from free image sites [Pexels](https://www.pexels.com/) and [Unsplash](https://unsplash.com/), product photos were found on manufacturer media pages.

---

## Features 🛠️

### Interactive Imagery 🖼️
At ReciPie, visual appeal meets interactivity, making browsing pie recipes a delightful experience:

- **Title Hover Effect**: Every pie recipe comes with its unique story. As users navigate the site, hovering over the title of each recipe reveals an engaging effect, thanks to the `.image-flash` design. This slight animation not only piques curiosity but also provides a hint of the artistry and details baked into every pie.

- **Like Counter Hover Effect**: Gauging a pie's popularity has never been this fun! As users move their cursors over the like counter, they witness an alluring hover effect. This dynamic interaction, enabled by the `.image-flash-likes` styling, makes appreciating and liking each recipe a captivating affair.

---

### Engaging Buttons 🔘
Buttons on ReciPie are not just about actions; they play a crucial role in driving user engagement:

- **Sign-up Button**: Presented with the `.btn-signup` class, this button warmly welcomes potential members to be a part of the ReciPie community. The interactive hover design subtly hints at the exciting baking adventures awaiting them upon joining.

- **Like Button**: Showcasing a pie's magnificence is a click away. The `.btn-like` button allows users to pour their love for a recipe effortlessly. The hover feedback makes sure that every 'like' feels personal and interactive.

---

## Future Enhancements 📅

ReciPie's ambition is not just to remain a static pie repository but to evolve into a dynamic community-driven platform for all baking enthusiasts. Several exciting enhancements are on the horizon:

1. **User-Submitted Recipes**:
   - While users can currently comment and like recipes, a major upcoming feature will allow users to submit their own pie recipes. This will allow the community to showcase their culinary talents and expand the site's recipe collection.

2. **Favorites Feature**:
   - Soon, users will have the ability to save their favorite recipes for easy access. A 'My Favorites' section will be incorporated into user profiles, providing a personalized recipe collection for each user.

3. **Expansion to Other Desserts**:
   - While ReciPie's current focus is pies, we aim to expand our repertoire to include a diverse range of desserts and baked goods such as cakes, tarts, pastries, and cookies. This will transform ReciPie into the ultimate hub for all dessert aficionados.

4. **Advanced Search & Filters**:
   - Enhance the user search experience by introducing advanced search capabilities. Users will soon be able to filter recipes by various criteria including ingredients, prep time, and dietary restrictions.

5. **Interactive Tutorials**:
   - Video tutorials and step-by-step interactive guides are in the pipeline for selected recipes. This will cater to users who are visual learners and provide additional support in the baking process.

6. **Ingredient Shopping Lists**:
   - A feature that enables users to auto-generate shopping lists directly from recipes. This will simplify the preparation phase for users, ensuring they have all the necessary ingredients before they start baking.

7. **Integration with Smart Kitchen Appliances**:
   - As the world of tech continually melds with the culinary arts, we're eyeing the possibility of allowing users to sync recipes with smart kitchen devices.

8. **Seasonal and Festival Specials**:
   - Regularly updating our content to reflect the season or upcoming festivals, such as "Winter Delights", "Thanksgiving Treats", or "Summer Fruit Bakes", will ensure ReciPie remains timely and relevant throughout the year.

9. **Community Challenges & Events**:
   - Hosting monthly baking challenges or themed events where users can participate, submit their creations, and win rewards. This will foster a strong sense of community and engagement.

At ReciPie, we're committed to baking a better tomorrow, one feature at a time. We are always eager to hear from our community and welcome feedback and suggestions for new features and improvements.

---

## Social Media Integration 🌐

Allowing for easy sharing with our `.link` design, and possibly expanding into other platforms with similar brand aesthetics, ensuring they complement our `.footer-bg` and associated footer styles.

---

## Testing

### Testing Strategy

I utilised both automated and manual testing strategies during the development of the site. For a comprehensive breakdown of the testing methodologies and procedures, refer to the [testing.md file](TESTING.md).

In addition to the functionality testing of the site and the code testing, User Story tests were conducted to ensure that the acceptance criteria of the previously listed user stories were fulfilled. The commit that addressed the functionality requirements for each user story can be found in the issues section of the repository. It was applied to every issue before it was closed and marked as completed.

#### Testing Overview

Testing was categorized into distinct sections, ensuring individual testing with developed test cases for each segment.

[View the Testing Schedule Overview](/static/docs/testing-schedule.pdf)

For an in-depth analysis of the testing procedures and methods, consult the [testing.md file](TESTING.md).

#### Validator Testing

Every code file underwent validation using the appropriate validators for their specific language. Complete details are available in the testing.md file. All code passed validation. However, some issues arose from code produced by third parties:
- Django's built-in code in the settings file led to five line length errors.
- Bootstrap code yielded 260 warnings during CSS validation.
- Fontawesome CDN resulted in 6 HTML validation errors concerning CSS variables within the CDN CSS code.

#### Automated Testing

Automated tests have been meticulously constructed for the Django-based blog application to ensure its robustness and reliability. These tests cover a spectrum of functionalities, including model integrity, view behaviors, and URL routing.

**Models Testing**:
- **Recipe Model**: Tests have been designed to verify the default ordering of recipe instances, the uniqueness of the 'slug' field, and the functionality of the `number_of_likes` method.
- **Ingredient Model**: Two sets of tests were written to ensure the correct string representation of the Ingredient model.
- **Comment Model**: Tests have been composed to verify the string representation and default ordering of comments.

**Views Testing**:
- **RecipeListView**: Verifies the URL's existence at the desired location, accessibility through its name, and the correct template usage.
- **RecipeDetailView**: Ensures the detail view URL is correctly positioned, can be accessed via its name, and uses the appropriate template.
- **RecipeLikeView**: A test confirms the functionality of the "like" feature by simulating a user liking a recipe and ensuring the proper redirection.

**URLs Testing**:
Tests have been carried out to ensure that the URLs correctly resolve for the respective views, providing a seamless navigation experience.

To run these comprehensive tests, one would need to clone the repository. It's crucial to note that the project settings have been configured to connect to the designated database if a database URL is found in the config variables. For a safe testing environment, omit the database URL in the config variables; this will prompt Django to run the tests on a SQLite3 test database, thereby safeguarding your primary PostgreSQL database (especially relevant if hosted on platforms like Heroku).

![Automated testing results](/static/docs/img/features/tests.png)

By leveraging this expansive suite of 45 tests, potential issues can be preemptively identified and addressed, underscoring a commitment to delivering a high-quality application.


#### Lighthouse Testing

Google Lighthouse was employed to obtain a holistic assessment of the website's performance. Although every test area returned a green score surpassing 90, the aggregate performance score varied based on the internet connection speed during the test. Scores ranged between 92 and 100 upon multiple test runs. The accessibility score was slightly affected due to non-sequential usage of headings across the site. The best practice score was influenced by the included JavaScript files from Mailchimp and Stripe, alongside the use of Bootstrap and jQuery libraries.

![Google Lighthouse Results](/static/docs/img/features/lighthouse.png)

#### Notable Bugs

-

#### Technologies Used

- **Python**: The primary language for the project. Various modules were employed, including Django for the main framework and others such as Django AllAuth for enhanced user account management.
  
- **Heroku**: Served as the cloud platform for site deployment.
  
- **Heroku PostgreSQL**: The designated database for both development and production phases.

- **JavaScript**: Employed for several site functionalities.
  
- **Bootstrap 5.2**: Assisted in the general layout and spacing.
  
- **Font Awesome**: Provided access to multiple icons.
  
- **CSS**: Written customarily for the site's aesthetics and design.
  
- **HTML**: The foundational language for the created templates.

#### Packages Used

- **Git Pod**: The primary development environment.
  
- **Git**: Facilitated version control and file transfers between the code editor and the repository.
  
- **GitHub**: Housed the project files.
  
- **Balsamiq**: Assisted in wireframe creation for the site.

#### Resources Used

Throughout the development process, various resources such as the Django documentation, HTMX documentation, Django AllAuth documentation, and the Code Institute reference materials were invaluable. Every resource used is cited appropriately.


---

## Deployment 🚀

The Pie Central website has been developed using Gitpod, specifically from a template provided by Code Institute. The codebase for the site is hosted on GitHub, and the live site is deployed via Heroku. Below are the steps that outline the deployment process:

### Setting up in Gitpod:

1. **Starting with the Code Institute Template**:
   - The project was initialized using a Gitpod template provided by Code Institute. This template sets up an environment with some necessary tools and extensions beneficial for development.

2. **GitHub Repository Setup**:
   - Within the Gitpod workspace, a new git repository was initiated using `git init`.
   - This local repository was then linked to a corresponding GitHub repository.

3. **Regular Commits**:
   - During the development phase, regular commits were made to ensure a documented progression.
   - These commits were pushed to the GitHub repository with the `git push` command.

### Heroku Deployment:

1. **Creation of Heroku App**: 
   - A new Heroku app was established post-login.
   - The deploy tab was navigated, and the GitHub account was connected, subsequently linking the Pie Central repository.

2. **Configuring Environment Variables**: 
   - The 'Config Vars' section was accessed under the settings tab of the Heroku app.
   - Necessary environment variables were set here, ensuring sensitive information remains confidential and away from version control.

3. **Enabling Automatic Deployment**:
   - The deployment method set to GitHub can be found within the deploy tab.
   - Automatic deployment was enabled for the master branch. This configuration ensures that each time a push is made to this branch on GitHub, Heroku automatically deploys the updates.

### Local Execution:

- For the purposes of local development and testing, the project was hosted in Gitpod.
- Dependencies were managed using `pip install -r requirements.txt`.
- The `heroku local` command enabled viewing of the app within a local environment.

By using the Gitpod template from Code Institute, integrating Gitpod with GitHub, and then connecting GitHub to Heroku, a streamlined deployment process was maintained. This structure supports efficient development, testing, and live application updates.

---