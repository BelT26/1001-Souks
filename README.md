# **1001 Moroccan Souks**

![Responsive preview of 1001 Moroccan Souks]()

## **Project Goal** 
The project was created for Jo, a friend of mine with a real passion for Morocco.  Jo has a property in Marrakesh and through her frequent trips there has got to know many local craftsmen.  She was so impressed by their work that she has decided to set up a business importing their products to the UK and this website is intended to launch her new venture

## Table of contents 
* [UX](#ux)
    * [Planning](#planning)
    * [User Stories](#user-stories)
    * [User Requirements and Expectations](#user-requirements-and-expectations)
        * [Requirements](#requirements)
        * [Expectations](#expectations)
    * [Design](#design-choices)
        * [Fonts](#fonts)
        * [Colors](#colors)    
* [Wireframes and Flowcharts](#wireframes-and-flowcharts)
    * [Wireframes](#wireframes)
    * [Flowcharts](#flowcharts)
    * [Database Structure](#database-structure)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Features to be implemented](#features-to-be-implemented)
* [Search Enine Optimization](#search-engine-optimization)
* [Social Media Marketing](#social-media-marketing)
* [Technologies used](#technologies-used)
    * [Languages](#languages)
    * [Libraries and Frameworks](#libraries-and-frameworks)
    * [Tools](#tools)
* [Testing](#testing)
* [Bugs](#bugs)
* [Deployment](#deployment)
    * [Local Deployment](#local-deployment)
    * [Heroku Deployment](#heroku-deployment)
* [Credits](#credits)

--- 

<a name="ux"></a>

## **UX**

<a></a>

### **User Goals**

* The landing page should create an instant good feeling, motivating the user to look at the rest the of site.
* The website has to work well on all kind of devices like mobile phones, tables and desktops.
* Ability to see the various rooms that the accommodation offers.
* Have some information about the surroundings of the accommodation like restaurants, places to visit etc.
* Be able to make a reservation online
* Visually appealing website

[Back to Top](#table-of-contents)

<a></a>

### **User Stories**

As a user:  
* I want the website to be visually appealing so I can already imagine myself being on holiday there.
* I want to have some information about the property and it's location.
* I want to have an intuitive navigation so I know right away where I can find which information.
* I want to see which different rooms the accommodation has to offer.
* I want to know what kind of amenities are included in the room.
* I want to see a lot of pictures so I can really visualise the place.
* I want to be able to make a reservation on the website itself.
* I want to be able to choose the exact room in which I want to stay.
* I want to have some information about the surroundings of the accommodation.
* I want to be able to get in contact with the property in case I have some questions.
* I want to know the address and how far / close it is to big cities.

### **Site owners Goals**

As an owner:  
* I want to promote my property the best way possible to attract new customers.
* I want to increase direct bookings by making the booking process easy and intuitive.
* I want to be able to see all the reservations.
* I want to have a separate section for arriving and inhouse reservations.
* I want to have a separate section as well for the reservations for the next 7 days so I can plan in advance.
* I want to be able to update the rooms easily in case I make some improvements to the room.
* I want to be able to add some rooms in case I decide to expand the accommodation.
* I want to be able to easily add some news places to visit, eat so the information stays accurate and up-to-date.

<a></a>


[Back to Top](#table-of-contents)

<a></a>

### **User Requirements and Expectations**

<a></a>

#### Requirements

* Easy to navigate by having a responsive navigation bar and various links to other pages throughout the site.
* Appealing landing page creating a warm feeling towards the place.
* Easy to find the various rooms and its amenities.
* Possibility to make a reservation.
* Find information about the environment, things to do, eat, see etc.
* Contact information like email, phone and address.
* Many images to be able to visualise how my holiday would look like.


### **Design**


#### Colors

Morocco is famous for it's bold bright colours.  The original idea was to use a green font on a yellow background however the text was not easy to read and did not pass the accessibility tests on the contrast checker.  Jo suggested using Tyrian Purple, which as well as providing a great contrast against the yellow also incorporates some local culture as it is one of the Moroccan natural dyes, used in the past for the robes of Roman emperors, and is made from the shells of murex snails found off the coast of Essaouira (the purple islands).

### Logo
The logo was designed by my friend Jo.


#### Fonts
The fonts for the website were sourced from google fonts [Google Fonts](https://fonts.google.com/ "Google Fonts") 
Cairo is used for the main headings and Alegreya Sans is used for the remaining text.


### Structure



## **Wireframes and Flowcharts**

### **Wireframes**
I used [Balsamiq](https://balsamiq.com/wireframes/) to create wireframes for my website.   
[Home page](wireframes/home.png)  
[Category](wireframes/category.png)  
[All Products](wireframes/all_products.png)  
[Map](wireframes/map.png)  
[Contact Form](wireframes/contact.png)  

### **Database Structure**

I created ___ models for this project.  The relationship between the models can be seen in the table below. 


## **Features**

### Navbar
The navbar was created using a Bootstrap template and modifed to fit the site requirement.  It is split into 3 sections:
The left section contains the site logo
The middle section incorporates the main navigation links and includes a dropdown menu which a user can use to navigate to a product category and a dropdown search bar that in which the user can look for specific items.
The right side shows whether the user is logged in, provided a link to their basket and offers them the possibility to log in or sign up if they are logged out.






## **Technologies used**

### **Languages**
HTML
CSS
Python
JavaScript

### **Libraries and Frameworks**
Django
Bootstrap

### **Planning Tools**
GitHub projects
Balsamiq wireframes
Excel

### **Payments""
Stripe

### **File Hosting**
Amazon Web Service

### **Deployment**
Github
Heroku

## Testing


## Bugs


## **Deployment**

### Local Deployment

My project was created on Github and my code was written on Gitpod [Gitpod](https://gitpod.io/) using regular commits to document the creation process. 
I've deployed this project to Heroku and used "git push heroku master" to make sure my pushes to GitHub were also made to Heroku. 

This project can be run locally using Gitpod by following the steps below. You may need to make some adjustment if using another IDE. Information about installing packages using pip and virtual environments can be fount in this [link](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

To clone the project: 

1. From the application's repository, click the "code" button and download the zip of the repository.
    Alternatively, you can clone the repository using the following line in your terminal:

    ``` 
    git clone https://github.com/BelT26/1001-Souks.git
    ``` 

2. Access the folder in your terminal window and install the application's [link to required modules](https://github.com/BelT26/1001-Souks/blob/master/requirements.txt) using the following command:

    ```
    pip3 install -r requirements.txt
    ```

3. Create a file containing your environmental variables called env.py at the root level of the application, containing the following lines and variables:
    ```
    import os

    os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY"
    os.environ["DEVELOPMENT"] = "True"

    os.environ["DEFAULT_FROM_EMAIL"] = 'DEFAULT_FROM_EMAIL'

    os.environ["STRIPE_PUBLIC_KEY"] = "STRIPE_PUBLIC_KEY"
    os.environ["STRIPE_SECRET_KEY"] = "STRIPE_SECRET_KEY"
    os.environ["STRIPE_WH_SECRET"] = "STRIPE_WH_SECRET"
    os.environ["STRIPE_CURRENCY"] = "EUR"

    ```
    This filename should be added to your gitignore file to ensure that sensitive information is hidden.

    For information on how to obtain the Stripe variables, please visit the [Stripe Documentation](https://stripe.com/docs)

    

4. Migrate the database models with the following command
    ```
    python3 manage.py migrate
    ```
5. Create a superuser and set up the credentials with the following command
    ```
    python3 manage.py createsuperuser
    ```
6. Launch the app on a local server with the following command
    ```
    python manage.py runserver
    ```
    To access the admin panel add '/admin' to the end of the website address displayed in the browser window and enter your superuser name and password.

    
### Heroku Deployment 

1. Login to your Heroku account and create a new app. Select your region. 
2. Once the app is created click on the resources button and under Add-ons, look for the Heroku Postgres to attach a postgres database to your project.  Select the Hobby Dev - Free plan and click 'Submit order form'   
3. On the settings page  click "Reveal config vars". Enter the below variables:
    ```
    AWS_ACCESS_KEY_ID = "AWS_ACCESS_KEY_ID"
    AWS_SECRET_ACCESS_KEY = "AWS_SECRET_ACCESS_KEY"
    AWS_S3_REGION_NAME = "AWS_S3_REGION_NAME"
    AWS_STORAGE_BUCKET_NAME = "AWS_STORAGE_BUCKET_NAME"
    USE_AWS = True
    
    DATABASE_URL = "This variable is automatically set when adding the Postgres Add on"

    SECRET_KEY = "SECRET_KEY"

    STRIPE_PUBLIC_KEY = "STRIPE_PUBLIC_KEY"
    STRIPE_SECRET_KEY = "STRIPE_SECRET_KEY"
    STRIPE_WH_SECRET = "STRIPE_WH_SECRET"
    STRIPE_CURRENCY = EUR

    DEFAULT_FROM_EMAIL = "DEFAULT_FROM_EMAIL"
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_HOST_PASS = "EMAIL_HOST_PASS"
    EMAIL_HOST_USER = "EMAIL_HOST_USER"
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    ```
4. From this screen, copy the value of DATABASE_URL
5. After this go to your settings.py file in the main project folder and comment out the default database configuration and add:
    ```
    DATABASES = {
        'default': dj_database_url.parse('Put your DATABASE_URL here'))
    }
    ```
6. Migrate again with the following command
    ```
    python3 manage.py migrate
    ```


7. Create a superuser for the postgres database so you can have access to the django admin by setting up the credentials with the following command
    ```
    python3 manage.py createsuperuser
    ```

    Login to the admin page and check the boxes 'Verified and primary"

8. If you are uploading a file of dats, use the following command: 

    ```
    python3 manage.py loaddata <name of file containing the data *>
    ``` 
    Data can also be added manually through the admin feature.

9. After migrations are complete, change database configurations to:
```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
```
This set up will allow your site to use Postgres in deployment and sqlite3 in development.


10. Make sure you have your requirements.txt file and your Procfile. In case you don't, follow the below steps:
    Requirements:
    ```
    pip3 freeze --local > requirements.txt
    ```
    Procfile:
    ```
    echo web: python app.py > Procfile
    ```
11. The Procfile should contain the following line:
    ```
    web: gunicorn <project_name>.wsgi:application

    ```

12. Add your files and commit them to GITHUB by running the following commands:
    ```
    git add . 
    git commit -m "Your commit message"
    git push
    ```

13. Add your Heroku app URL to ALLOWED_HOSTS in your settings.py file
14. Disable collect static so that Heroku doesn't try to collect static files when you deploy by typing the following command in the terminal
    ```
    heroku config:set DISABLE_COLLECTSTATIC=1
    ```
15. Select "Deploy" in the from the Heroku menu and under Deployment Method selectGithub. 
16. Enter the name of your repository and click connect. 
17. Click 'Enable automatic deploys' and then Deploy Brance
18. Once Heroku has finished building the app click "view app" to open it.
19. Commit any changes using git push. 

### File Storage
1. AWS has been used to store static and media files. Full documentation is available her [Amazon S3 Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html).
    

### Email Set Up
1. The following steps document how to set up an email service using Gmail to send emails to users. 

* Navigate to your account settings.
* Select Security then Signing in to Google and ensure 2 step verification is enabled.
* Under the 'App passwords' option, select 'mail' and under device type select 'other' and enter 'Django'.
* Copy the newly created password and set it as a config var on the settings page in Heroku:

```
    EMAIL_HOST_PASS = 'Password you just copied'
    EMAIL_HOST_USER = 'Your gmail account
```
* Go to your settings.py in the main project folder and add the following:

```
    if "DEVELOPMENT" in os.environ:
        EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
        DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
    else:
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAIL_USE_TLS = True
        EMAIL_PORT = 587
        EMAIL_HOST = 'smtp.gmail.com'
        EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
        EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
        DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
```


[Back to Top](#table-of-contents)


## **Credits**
