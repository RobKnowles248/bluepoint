<h1 align="center">Bluepoint</h1>

[View the live project here.](https://bluepoint-rob.herokuapp.com/)

Bluepoint is a site similar to climbing websites [8a.nu](https://www.8a.nu/) and [UKClimbing](https://www.ukclimbing.com/) where users create a logbook of outdoor climbs that they have completed. However, instead of logging successful climbs, users will log their successful belays of other climber's ascents. The term "bluepoint" is given to this by some climbers.

## User Experience (UX)

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

*   ### Wireframes

    -   Home Page Wireframe - [View](wireframes/home-page.pdf)

    -   User Logbook Wireframe - [View](wireframes/logbook-page.pdf)

## Features



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

### Testing User Stories from User Experience (UX) Section

Screenshots of the parts of the finished site that satisfy the user stories:

-   #### Viewing and Navigation

    1. As a First Time Visitor, I want to easily understand the main purpose of the site so that I can decide if the site is for me.
    ![Site purpose](/media/screenshots/site_purpose.png)
    2. As a site user, I want to be able to navigate easily to pages of the site, so that I can enjoy using the site.

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

### Further Testing

### Known Bugs

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

### Media

-   The homepage hero image was provided by Thomas Teece.

### Acknowledgements

-   My Mentor Akshat Garg for continuous helpful feedback.