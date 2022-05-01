# **1001 Moroccan Souks**

![Responsive preview of 1001 Moroccan Souks](https://github.com/BelT26/1001-Souks/blob/main/static/screenshots/responsive_preview.jpg)

## Table of Contents 
* [Overview]
* [Planning](#planning)
    * [Wireframes](#wireframes)
    * [Database Structure](#database-structure)
    * [Agile Tools](#agile-tools)
        * [Epics](#epics)
        * [User Stories](#user-stories)
        * [Tasks](#tasks)   
* [Design](#design)
    * [Fonts](#fonts)
    * [Colors](#colors)
    * [Logo](#logo)  
* [Features](#features)
    * [Toasts](#toasts)
    * [Navbar](#navbar)
    * [Footer](#footer)
    * [Home Page](#home-page)
    * [Map](#map)
    * [Location Page](#location-page)
    * [Category Page](#category-page)
    * [All Products](#all-products)
    * [Product Info](#product-info)
    * [Checkout](#checkout)
    * [Product Admin](#product-admin)
* [User Authentication](#user-authentication)
    * [User Profiles](#user-profiles)
* [Search Enine Optimization](#search-engine-optimization)
* [Social Media Marketing](#social-media-marketing)
* [Technologies used](#technologies-used)
    * [Languages](#languages)
    * [Libraries and Frameworks](#libraries-and-frameworks)
    * [Other Tools](#other-tools)
* [Testing](#testing)
* [Bugs](#bugs)
* [Deployment](#deployment)
    * [Local Deployment](#local-deployment)
    * [Heroku Deployment](#heroku-deployment)
* [Credits](#credits)

--- 

## **Overview** 
The project was created for Jo, a friend of mine with a real passion for Morocco.  Jo has a property in Marrakesh and through her frequent trips there has got to know many local craftsmen.  She was so impressed by their work that she has decided to set up a business importing their products to the UK and this website is intended to launch her new venture.

## **Planning**

### **Wireframes**
I used [Balsamiq](https://balsamiq.com/wireframes/) to create wireframes for my website.   
[Home page](wireframes/home.png)  
[Category](wireframes/category.png)  
[All Products](wireframes/all_products.png)  
[Map](wireframes/map.png)  
[Contact Form](wireframes/contact.png)  

### **Database Structure**

I created ___ models for this project.  The relationship between the models can be seen in the table below. 

### **User Stories**

Please see the below table for the user stories.  Each story is categorized under an epic and given a priority rating of 1 (must have), 2 (should have) or 3 (nice to have).


## **Design**

### **Colors**

Morocco is famous for it's bold bright colours. The yellow used in the header and footer was inspired by the window grilles of the Majorelle garden in Morocco. Originally we planned to use a green font on a yellow background however the text was not clearly legible and did not pass contract checker accessibility tests.  Jo suggested using Tyrian Purple, which as well as providing a great contrast against the yellow also incorporates some more local culture as it is one of the Moroccan natural dyes, used in the past for the robes of Roman emperors, and is made from the shells of murex snails found off the coast of Essaouira (the purple islands).


### **Fonts**
The fonts for the website were sourced from google fonts [Google Fonts](https://fonts.google.com/ "Google Fonts") 
Cairo is used for the main headings and Alegreya Sans is used for the remaining text and Babylonica for the signature.

### **Logo**
The logo was designed by my friend Jo using Canva.

![Logo](https://github.com/BelT26/1001-Souks/blob/main/static/screenshots/logo.jpg)

## **Features**


## Toasts
Feedback on user interaction is provided via Django messages which appear in the form of toasts which I formatted to keep the general style of the website. 

![Toast Example](https://github.com/BelT26/1001-Souks/blob/main/static/screenshots/toast.jpg)

### Navbar
The navbar was created using a Bootstrap template and modifed to fit the site requirements.  It is split into 3 sections:
The left section contains the site logo.
The middle section incorporates the main navigation links and includes a dropdown menu which a user can use to navigate to a product category and a dropdown search bar that in which the user can look for specific items.
The right side shows whether the user is logged in, provides a link to their basket and offers them the possibility to log in or sign up if they are logged out.  If the user has superuser credentials, the admin dropdown menu is displayed in this section.

![Navbar](https://github.com/BelT26/1001-Souks/blob/main/static/screenshots/navbar.jpg)

## Footer
The contact email address is on the left side of the footer and allows users to get in touch with any queries. The email address opens up a link to the user's email account with a prepopulated 'to' field.
The right side of the footer contains social media links to Facebook and Instagram. The icons change from purple to blue when the user hovers over them to indicate to the user that they are links. 

![Footer](https://github.com/BelT26/1001-Souks/blob/main/static/screenshots/footer.jpg)

### Home Page
At the top of the home page there is a hero image of some shops selling a variety of traditionsl Moroccan sandals and shoes.  This photograph was taken on a recent trip to Marrakech by my friend Jo.
![Hero Img]()

Below the main image is a section featuring the tale behind the conception of 1001 Moroccan souks that is told in the form of a story designed to engage the interest of the user. The information is accompanied by images from traditional Moroccan souks that were taken by Jo.

![About](https://github.com/BelT26/1001-Souks/blob/main/static/screenshots/intro.jpg)


### Map
The map provides the user with some information about the locations in Morocco that are famous for the production of certain crafts.  A popover appears when the user hovers on the location with a brief description and a link to the destination page.  A link in the description takes the user to a page with more information about the location and a list of the available products that are made there. I used the Google maps documentation as a guide to creating the map and adding the popover. An asterisk was used inside the marker so that it resembled the Moroccan flag which is a star on a red background.

![Map]()

### Location Page
The location page is accessed from the links on the map page and is split into two sections.  The top section includes an image of the featured town with a description to the side.

Below are a list of local producers with a picture and information about the maker and a list of their products that the user can view further information about by clicking on a button link.

![Location Page]()

### Category Page
The category page follows a similar structure to the Location Page.  The top section contains an image representing the selected category alongside information about the history and traditions of the craft.

Underneath, all the products available in that category are listed and the user can view further information by clicking on the link.

![Category Page]()

### All Products Page
The All Products Page displays all of the products on sale. By default they are sorted by price. This template is also returned with all matching products when the user submits search criteria.  

![All Products Page](https://github.com/BelT26/1001-Souks/blob/main/static/screenshots/all_products.jpg)

If no products meet the search term the user is advised of this and can return to the home page via the button.

![No Results Message](https://github.com/BelT26/1001-Souks/blob/main/static/screenshots/no_results.jpg)

### Product Info Page
The product info page provides a larger photo of the product and more details, including a description and the product size.
From the product info page the user can add the product to their basket.

![Product Info Page](https://github.com/BelT26/1001-Souks/blob/main/static/screenshots/product_detail.jpg)

### Basket
The basket stores the items the user wishes to purchase before they checkout. I followed the code in the Boutique Ado walkthrough project to create the profile app then customised it for my site.

![Basket](https://github.com/BelT26/1001-Souks/blob/main/static/screenshots/product_detail.jpg)

### Contact Form
This form is intended for users who wish to send a more detailed query to the site owner. It incluced a dropdown menu with the most common query categories.

![Contact Form](https://github.com/BelT26/1001-Souks/blob/main/static/screenshots/contact_form.jpg)

### FAQs
This page answers common questions and provides a link to the company privacy policy.  I felt it was important to add this page to address GDPR concerns and to help the site rank more highly for trustworthiness and authorativeness

![FAQs] ()

## User Authentication
Django Allauth was installed to enable users to sign up, log in and log out.  I copied the Allauth templates into a separate folder and created a custom container for them in the allauth base.html which extends the project level base.html.

![Sign Up Form](https://github.com/BelT26/1001-Souks/blob/main/static/screenshots/signup.jpg)

## User Profiles
Users have the opportunity of saving their details for future session by creating a user profile using the below form.  I followed the code in the Boutique Ado walkthrough project to create the profile app then customised it for my site.

![Profile Form](https://github.com/BelT26/1001-Souks/blob/main/static/screenshots/profile.jpg)


## Admin Features

The below menu is displayed when a user is logged in as a superuser

![Admin Menu](https://github.com/BelT26/1001-Souks/blob/main/static/screenshots/admin_menu.jpg)

### Product Admin

![Add Product]()

![Edit or Delete Product]()

### Maker Admin

![Add Maker]()

![Edit or Delete Maker]()

### Customer Queries

![Customer Queries]()

## **Technologies used**

### **Languages**
HTML
CSS
Python
JavaScript

### **Libraries and Frameworks**
Django
Bootstrap

### **Other Tools**

#### **Planning**
GitHub projects
Balsamiq wireframes
Excel

#### **Payments""
Stripe

#### **File Hosting**
Amazon Web Service

#### **Deployment**
Github
Heroku

## Testing


## Bugs
Adjust basket call was not functioning.  Issue with the JQuery selector. Consulted Jquery documentation and realised that 'prev' in the JQuery selector referred to the next sibling.  As I had added a div to adjust the layout of the links the form was no longer a sibling of the anchor elements.  To correct this I went up one level by adding a .parent() selector before .prev().

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



## **Credits**
The logo and text for the site were provided by Jo Jarvis



### Future Development Possibilities
As this is a real project I will be continuing to work on it after submission and plan to implement the following features:

Give customers the possibility to add ratings to products

Add the possibility to sort and filter products by the rating given.

Expand the range of products offered

[Back to Top](#table-of-contents)