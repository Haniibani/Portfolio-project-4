# Recipie 🥧

## Introduction 📜

Welcome to **Recipie**! Dive deep into a world exclusively crafted for pie enthusiasts, where every recipe, filling, crust, and comment is dressed in the most refined and user-friendly designs. With colors emanating warmth and typography exuding sophistication, we've ensured that our pie universe is baked to perfection!

---

## Table of Contents 📖

1. [Introduction](#introduction-)
2. [UX](#ux-)
3. [Features](#features-🛠️)
4. [Future Enhancements](#future-enhancements-🚀)
5. [Social Media Integration](#social-media-integration-🌐)
6. [Testing Protocols](#testing-protocols-🧪)
7. [Deployment Guidelines](#deployment-guidelines-🚀)

---

## UX 🖥️

### Overall Goals

- Ensure the platform reflects sophistication, using the calming colors of `.light-bg`, `.dark-bg`, and `.main-bg`.
- Showcase featured pies and authors with the `.masthead`, styled with the `.masthead-text` and the `.masthead-image`.

### The Strategy Plane

Empower bakers by offering an interactive platform featuring pie recipes that are both visually appealing and easily accessible. Our `.image-container` ensures that every pie gets its spotlight, while the `.author` class highlights the creator.

### The Site's Ideal User

**Hobbyist Bakers**: Those who appreciate the fine craft of baking and are drawn by our meticulously styled `.card` and `.brand` designs.

### Site Goals

- Present pie recipes in a stylish `.card` format with emphasis on imagery using `.image-flash`.
- Boost engagement with actionable buttons styled as `.btn-like` and `.btn-signup`.

### Epics

**Social Engagement**: Using the `.btn-like` to allow users to appreciate recipes and the `.post-link` to share them.

### User Stories

1. As a user, I want to see the brand prominently, evident in the `.brand` and `.brand-centered` styles.
2. As a baker, the `.recipe-time` element is crucial for me to plan my baking sessions.

### The Scope Plane

Providing detailed pie recipes, ensuring rich content with the `.post-title` and `.post-subtitle`, and a smooth navigation experience through our `.link` design.

### The Structure Plane

A well-organized platform where recipes are not only easy to find but are also presented in a visually appealing manner using `.image-flash-likes` and `.masthead-featured-image`.

### The Skeleton Plane

#### Wireframe mock-ups

These should focus on the overall layout, ensuring our `.masthead` is prominently displayed and that our cards, styled with `.card`, are neatly arranged.

#### SEO Considerations

Optimizing for search engines by emphasizing key elements like the `.post-title` and `.author`.

---

## Features 🛠️

### Interactive Imagery 🖼️
At ReciPie, visual appeal meets interactivity, making browsing pie recipes a delightful experience:

- **Title Hover Effect**: Every pie recipe comes with its unique story. As users navigate the site, hovering over the title of each recipe reveals an engaging effect, thanks to the `.image-flash` design. This slight animation not only piques curiosity but also provides a hint of the artistry and details baked into every pie.

- **Like Counter Hover Effect**: Gauging a pie's popularity has never been this fun! As users move their cursors over the like counter, they witness an alluring hover effect. This dynamic interaction, enabled by the `.image-flash-likes` styling, makes appreciating and liking each recipe a captivating affair.

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

## Testing Protocols 🧪

- **UI Testing**: Checking the responsiveness of elements like `.masthead` across devices.
- **Functionality Testing**: Interactions such as signing up with `.btn-signup` and liking with `.btn-like` should be intuitive and error-free.

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

