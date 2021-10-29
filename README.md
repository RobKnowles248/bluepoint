<h1 align="center">Bluepoint</h1>

[View the live project here.](https://bluepoint-rob.herokuapp.com/)

Bluepoint is a site similar to climbing websites [8a.nu](https://www.8a.nu/) and [UKClimbing](https://www.ukclimbing.com/) where users create a logbook of outdoor climbs that they have completed. However, instead of logging successful climbs, users will log their successful belays of other climber's ascents. The term "bluepoint" is given to this by some climbers.

## User Experience (UX)

-   ### Primary Goals

    To create a site similar to the inspirations for this where climbers can keep a logbook of climbs that they have belayed other people on rather than climbs they have done themselves.

-   ### Developer Goals

    -   To gain experience using the Django framework to build a full stack application.
    -   To create a site where friends of the developer and other climbers can log their "bluepoints".

-   ### User stories

    -   #### Viewing and Navigation

        1. As a First Time Visitor, I want to easily understand the main purpose of the site so that I can decide if the site is for me.
        2. As a site user, I want to be able to navigate easily to pages of the site, so that I can enjoy using the site.

    -   #### Registration and User Accounts

        1. As a Site User, I want to be able to easily register for an account, so I can view my profile and log bluepoints.
        2. As a Site User, I want to be able to easily login or logout, so I can access my profile and log bluepoints quickly.
        3. As a Site User, I want to be able to easily recover my password if I forget it, so I am never locked out of my account.
        4. As a Site User, I want to receive a confirmation email after registering, so that I can verify my registration was successful.
        5. As a Site user, I want to have a logbook page, so that I can view and edit my existing bluepoints and personal details.

    -   #### Logging Bluepoints
        1. As a logged in user, I want to be able to log my bluepoints, so that I can add to my logbook of bluepoints.
        2. As a logged in user, I want to be able to see other users logbooks, so that I can compare with mine.
        3. As a logged in user, I want to be able to search for other users to compare their logbooks to mine.

    -   #### Donations
        1. As a donor, I want to be able to easily enter my payment information, so that I can donate quickly and easily.
        2. As a donor, I want to know that my payment details are secure, so that I can pay confidently.
        3. As a donor, I want to see confirmation after I have donated, to know my donation was successful.

-   ### Design
    -   #### Colour Scheme
        -   The two main colours used are blue and white.
    -   #### Typography
        -   The Roboto font is the main font used throughout the whole website with Sans Serif as the fallback font in case for any reason the font isn't being imported into the site correctly.
        -   The heading use the Nunito font

-   ### Wireframes

    -   Home Page Wireframe - [View](wireframes/home-page.pdf)

    -   User Logbook Wireframe - [View](wireframes/logbook-page.pdf)

## Features

-   ### Existing Features

    -   Home page with info about the site.
    -   Login and signup functionality for users of the site.
    -   Functionality for users to add edit and delete bluepoints for their logbook.
    -   A logbook page where users can view all of their bluepoints sorted by grade.
    -   A searchbar where users can search for the logbooks of other users.
    -   A list of the 10 most recently logged bluepoints on the homepage.
    -   A list of the 10 highest graded bluepoints on the homepage.
    -   A donation page where users of the site can donate to support the development of the site.
    -   Integration with Stripe to take payments securely from users when they donate.

-   ### Future Potential Features to Implement

    -   The ability for users to make their logbooks private.
    -   Tying the "climber" field in the bluepoint model to another user of the site if the climber is also a user of the site.

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://www.javascript.com/)
-   [Python3](https://www.python.org/)

### Frameworks, Libraries & Programs Used

1. [Bootstrap 5.1:](https://getbootstrap.com/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Roboto' and 'Nunito' fonts for use across the site.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used for icons across the site.
1. [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive but was used in much of the javascript.
1. [Git](https://git-scm.com/)
    - Git was used for version control.
1. [GitHub:](https://github.com/)
    - GitHub was used to store the projects code after being pushed from Git.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the wireframes during the design process.
1. [Django](https://www.djangoproject.com/)
    - Django was the framework used to build the site.
1. [Django-allauth](https://django-allauth.readthedocs.io/en/latest/index.html)
    - Django-allauth was used on the authentication pages on the site.
1. [Heroku](https://www.heroku.com/)
    - Heroku was used to deploy the app.
1. [AWS](https://www.aws.amazon.com/)
    - AWS S3 was used to store the static files of the app.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

### Testing responsiveness



### Testing User Stories from User Experience (UX) Section

Screenshots of the parts of the finished site that satisfy the user stories:

-   #### Viewing and Navigation

    1. As a First Time Visitor, I want to easily understand the main purpose of the site so that I can decide if the site is for me.
    ![Site purpose](/media/screenshots/site_purpose.png)
    2. As a site user, I want to be able to navigate easily to pages of the site, so that I can enjoy using the site.
    ![Navigation](/media/screenshots/navigation.png)

-   #### Registration and User Accounts

    1. As a Site User, I want to be able to easily register for an account, so I can view my profile and log bluepoints.
    ![Signup page](/media/screenshots/signup.png)
    2. As a Site User, I want to be able to easily login or logout, so I can access my profile and log bluepoints quickly.
    ![Login page](/media/screenshots/login.png)
    ![Logout page](/media/screenshots/logout.png)
    3. As a Site User, I want to be able to easily recover my password if I forget it, so I am never locked out of my account.
    ![Reset password page](/media/screenshots/reset_password.png)
    4. As a Site User, I want to receive a confirmation email after registering, so that I can verify my registration was successful.
    5. As a Site user, I want to have a logbook page, so that I can view and edit my existing bluepoints and personal details.
    ![Logbook page](/media/screenshots/logbook.png)

-   #### Logging Bluepoints
    1. As a logged in user, I want to be able to log my bluepoints, so that I can add to my logbook of bluepoints.
    ![Log a bluepoint page](/media/screenshots/log.png)
    2. As a logged in user, I want to be able to see other users logbooks, so that I can compare with mine.
    ![Other user's logbook](/media/screenshots/robs_logbook.png)
    3. As a logged in user, I want to be able to search for other users to compare their logbooks to mine.

-   #### Donations
    1. As a donor, I want to be able to easily enter my payment information, so that I can donate quickly and easily.
    2. As a donor, I want to know that my payment details are secure, so that I can pay confidently.
    3. As a donor, I want to see confirmation after I have donated, to know my donation was successful.

### Testing Home App

The home app was tested using a number of manual tests detailed below.

-   #### Accordions

    -   Accordions on the home page were opened and close to ensure they were working as intended
    ![Accordions](/media/screenshots/accordions.png)

-   #### Recent Bluepoints

    -   More than 10 bluepoints were logged to check that only 10 showed
    ![Recent Bluepoints](/media/screenshots/recent-bluepoints.png)
    -   Some new bluepoints were logged to check that the climbs were ordered by most recent (they came up at the top)
    -   The links were clicked to check they led to the right logbook

-   #### Top Bluepoints

    -   More than 10 bluepoints were logged to check that only 10 showed
    ![Top Bluepoints](/media/screenshots/top-bluepoints.png)
    -   Some bluepoints of various grades were logged to check that the list was ordered by grade
    -   The links were clicked to check they led to the right logbook

### Testing Donate App

The donate app was tested using a number of manual tests detailed below.

-   #### Donation Form

-   #### Payment Form

### Testing Logbooks App

The logbooks app was tested using a number of manual tests detailed below.

-   #### Logbook Page

    -   The "My Logbook" button was clicked and the user was taken to the correct logbook.
    -   Multiple bluepoints were logged to check that the pyramid and logbook were updated and ordered correctly with the correct info.
    ![Pyramid](/media/screenshots/pyramid.png)
    ![Logs](/media/screenshots/logs.png)
    -   All buttons on the logbook page were clicked to check they led to the right place
    ![Logbook](/media/screenshots/logbook.png)

-   #### Log Bluepoint Form

    -   The add_bluepoint buttons in the navigation, homepage and logbook pages were all clicked and led to the correct page
    -   The form was submitted without a route name to check it would not submit
    ![No route name](/media/screenshots/no-route-name.png)
    -   The form was submitted without a grade to check it would not submit
    ![No grade](/media/screenshots/no-grade.png)
    -   The form was submitted correctly to check and the bluepoint was added to the correct user's logbook with a success message
    ![Logged bluepoint](/media/screenshots/log-bluepoint.png)
    -   I attempted to access the add_bluepoint url manually without being logged in and was redirected to the log in page and then the add_bluepoint page after logging in 
    ![Add bluepoint redirect](/media/screenshots/add-bluepoint-redirect.png)
    ![Add bluepoint redirect 2](/media/screenshots/add-bluepoint-redirect-2.png)

-   #### Edit Bluepoint Form

    -   The edit button on a bluepoint in the logbook was clicked and it led to the edit bluepoint page for the correct bluepoint
    -   The form was submitted without a route name to check it would not submit
    ![No route name](/media/screenshots/no-route-name.png)
    -   The form was submitted without a grade to check it would not submit
    ![No grade](/media/screenshots/no-grade.png)
    -   The form was submitted correctly to check and the bluepoint was changing correctly in the correct user's logbook with a success message
    ![Edit bluepoint success](/media/screenshots/edit-bluepoint.png)
    -   I attempted to access the edit_bluepoint url manually without being logged in and was redirected to the log in page and then the        edit_bluepoint page after logging in.
    ![Edit bluepoint redirect](/media/screenshots/edit-bluepoint-redirect.png)
    -   I attempted to access the edit_bluepoint url of a bluepoint that was not mine and was redirected to the homepage with an error message
    ![Edit bluepoint not allowed](/media/screenshots/edit-bluepoint-not-allowed.png)

-   #### Delete Bluepoint

    -   The delete bluepoint button in the logbook was clicked and it deleted the correct bluepoint
    ![Delete bluepoint success](/media/screenshots/delete-bluepoint.png)
    -   I attempted to access the delete_bluepoint url of a bluepoint that was not mine and was redirected to the homepage with an error message
    ![Delete bluepoint not allowed](/media/screenshots/delete-bluepoint-not-allowed.png)  

-   #### Search Form

## Deployment

The site was deployed using the following steps:

1. Created a new app on Heroku called 'bluepoint-rob' in the European region.

2. Provisioned a new Postgres database in the resources tab on the Heroku dashboard.

3. Used pip to install dj_database_url and psycopg2-binary to the development environment

4. Imported dj_database_url in settings.py and replaced the default database with a call to `dj_database_url.parse(url)` with the database url being the one for our new Postgres database in our config vars in Heroku.

5. Ran the migrations on the new database and created a superuser.

6. Added an if statement to settings.py to decide which database to connect to depending on the environment variables.

7. Installed gunicorn using pip as our webserver.

8. Created a Procfile to tell Heroku to create a web dyno which will run gunicorn

9. Logged in to the Heroku CLI and ran `heroku config:set DISABLE_COLLECTSTATIC=1 --app <app_name>` to stop Heroku trying to collect the static files when we deploy.

10. Added the Heroku app hostname to allowed hosts in settings.py.

11. Ran `heroku git:remote -a bluepoint-rob` to set up the git remote.

12. Commit and pushed any changes then ran `git push heroku master`

13. In the deploy tab in the Heroku dashboard, connected the app to our github repository and enabled automatic deploys.

14. An AWS S3 bucket was created and setup to store the static files of the app.

## Credits

### Code

-   The basics of the project were created by following the Code Institute Boutique Ado walkthrough project and customised to suit the needs of the site.

### Content

-   The site was inspired by the sites [8a.nu](https://www.8a.nu/) and [UKClimbing](https://www.ukclimbing.com/)

### Media

-   The homepage hero image was provided by Thomas Teece.

### Acknowledgements

-   My Mentor Akshat Garg for continuous helpful feedback.