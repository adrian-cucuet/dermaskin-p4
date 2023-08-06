# DermaSkin #

* This is my Project Portofolio 4 for Code Institue Diploma in Software Development - E-commerce Applications. The project is a website for a derma clinic. The idea was to present the user with information about services that are offered by the business and explain more about them. If the user decides to use the services of the clinic, the booking page offers that possibility.
The users can create an account and save/update their contact information. The profile page offers a booking history as well. As a business owner, he can add services through the front-end, view all the future bookings and details, and can manage the products with a click of a button.
<hr>

![ScreenShot](./documents/readme_images/AmiResponsiveImg.png)

The live version of the website is available for you here : <a href="https://dermaskin-pp4-37d6c98e9c3c.herokuapp.com/">DermaSkin</a>

# README CONTENTS # 

<hr>

* ## [UX](#ux-1)
   * [User Stories](#user-stories)
   * [Agile Methodologies](#agile-methodologies)
   * [The Scope](#1-scope)
   * [Structure](#2-structure)
   * [Skeleton](#3-skeleton)
   * [Surface](#4-surface)

* ## [Features](#features)
    * [Home Page](#home-page)
    * [Navigation Menu](#navigation-menu)
    * [User Registration and Login](#user-registration-and-login)
    * [Services](#services)
    * [Service Detail](#service-detail)
    * [Booking service](#booking-service)
    * [Profile Page](#profile-page)
    * [Booking management](#booking-management)

* ## [Deployment](#deployment)
    * [Heroku Service](#herokucom-service)
    * [Final Steps](#final-steps)

* ## [Technologies Used]()
    * [Languages Used](#languages)
    * [Frameworks / Libraries](#frameworks-libraries)

* ## [Credits](#credits-1)

<hr>

# UX #

## User Stories ##

  * As the site owner I want : 
  
    * A simple and intuitive user interface that is easy to navigate.
    * The ability to manage user accounts and access.
    * The ability to manage the services offered.
    * The ability to receive bookings for services.
    * A responsive design that works well on any device.
    * The ability for the users to update personal detail and view booking history.

  * As the user, I would want : 

    * A responsive and user-friendly design that works well on any device
    * An easy and efficient way to browse through pages of the website.
    * The ability to create an account and see my appointments.
    * The possibility to save my data for future bookings.
    * The ability to book a service if I want.

<hr>    

## Agile Methodologies ##

The agile methodology approach was used here when creating DermaSkin website.

The MoSCoW principle was used when created the UserStories: 
- Must have
- Could Add

The application will have more features added in the future with constant progression towards a fully completed application.

<hr>

## 1. Scope ## 

The website aims to provide a platform for existing customers, and attract new customers for the business. Users will be able to register an account, save their data for future appointments, browse through services offered, book a service, and view a list of their bookings. The website is simple to use, with a focus on providing a visually appealing and responsive design.

<hr>

## 2. Structure ##

* Home Page - a landing page that provides an overview of the business and its services.
* Register Page - a page where users can create a new account by providing their name, email address and a password.
* Login Page - a page where users can log in to their account using their email address and password.
* User Profile Page - a page where users can update their personal information and view a list of their appointments.
* Service Page -  a page where users can view all the services offered.
* Service Detail Page - a page where the user can see a detailed view of the service.
* Bookings Page - a page where the user can create an appointment for any service offered by the business.
* Add Service Page - a page where the admin/owner can add a new service on the website.
* Edit Service Page - a page where the admin/owner can edit a service on the website.
* Booking Management Page - a page where the admin/owner can see all the future appointments and customer details.

<hr>

## 3. Skeleton ##

Here is a basic wireframe of the website's layout : 
![ScreenShot](./documents/readme_images/wireframe-dermaskin.png)

Here is the database schema for the project : 
![ScreenShot](./documents/readme_images/database.png)

<hr>

## 4. Surface ## 

The design of DermaSkin is clean and modern, with a focus on readability and ease of use. The color scheme consists primarily of white and blue, with green accents used sparingly for emphasis.

### Layout -

The layout of DermaSkin is responsive and adapts well to different screen sizes. Bootstrap and Bootstrap Studio used in order to provide a responsive website. The navbar is fixed at the top of the screen and is always visible, with the site logo, navigation links centered and spread between.
The Hero section uses a large background image, with a centered heading and subheading along with two buttons for Services page and Booking page.
Cards are used throughout the site to display content, such as services, information about business, information about individual service and forms.
The footer is fixed always to the bottom of the screen containing the contact details, navigation links, social media links and logo.

<hr>

# Features #

<hr>

## Navigation:
- A menu at the top of the page allows users to easily navigate between different pages on the site.
![ScreenShot](./documents/readme_images/HomePage.png)
## Home Page:
 - The Home page contains information about the services offered and skin problems that the user could face.
 ![ScreenShot](./documents/readme_images/GalleryPage.png)
## User registration and login:
- Users can create an account to access member-only features and log in to access their account in the future.
![ScreenShot](./documents/readme_images/SignUpForm.png)
![ScreenShot](./documents/readme_images/LoginForm.png)
## Services:
 - A collection of posts of different types of cars. Users can view these images, leave comments and like the post/comments.
 ![ScreenShot](./documents/readme_images/GalleryPage.png)
## Service Detail:
 - Each service has an individual page with important information, explanations, prices and FAQ.
 ![ScreenShot](./documents/readme_images/MyPostsPage.png)
## Booking service:
- Users can book a service on the booking page and submiting the form a success page is shown.
 ![ScreenShot](./documents/readme_images/CommentView.png)
 ![ScreenShot](./documents/readme_images/CommentView.png)
## Profile Page:
- Users can update their information on profile page and can see a history of bookings.
 ![ScreenShot](./documents/readme_images/CommentView.png)
## Booking management:
- Admin/owner can have a complete view of future bookings, filtered automatically by date.
 ![ScreenShot](./documents/readme_images/CommentView.png)

<hr>

# Testing # 

 * I have created a seperate markdown documentation for the testing of this project. 

 - You can view the testing here : [Testing.MD](./TESTING.md)

 <hr>

# Deployment #

* ## Heroku.com Service ##

  * Here we log in or create an account to begin with.
  * On the dashboard view click 'Create New App' from the dropdown menu
  * Choose your app-name and region
  * Setup the CONFIG_VARS in the Settings tab in your project. 
      * SECRET_KEY
      * DATABASE_URL
      * CLOUDINARY_URL

      These three url's are to be set up and configured in your project.
      These connect your Database , Cloudinary and your Django Enviroment Key.
  * In the buildpack section in the settings tab add Python , then save changes.
  * Last but not least Link your project under the Deploy tab by selecting it from your github repository.

* ## Final Steps #

  * Make sure your settings.py option DEBUG = True is set to FALSE.
  * Ensure you have your Procfile created with the following code :
      * web: gunicorn carstyleautos.wsgi


* You can find the deployed version of the website here : <a href="https://dermaskin-pp4-37d6c98e9c3c.herokuapp.com/" target="_blank">DermaSkin</a>

<hr>

# Technologies Used #

* ## Languages ##
  * HTML
  * CSS
  * Python
  * JavaScript

* ## Frameworks / Libraries / Programs ##
  * <a href="https://www.djangoproject.com/">Django (Python web Framework)</a> 
  * <a href="https://jquery.com/">jQuery (Javascript Library)</a>
  * <a href="https://getbootstrap.com/">Bootstrap (Front-End Library)</a>
  * <a href="https://django-crispy-forms.readthedocs.io/en/latest/">Django-Crispy-Forms (Django Form Rendering Library)</a>
  * <a href="https://pypi.org/project/psycopg2/">Psycopg2-Binary(PostgreSQL database adapter for Python)</a>
  * <a href="https://github.com/">GitHub (Version Control alongside a Local Development Enviroment)</a>
  * <a href="https://icons8.com/">Icon8 (Library of Icons)</a>
  * <a href="https://www.elephantsql.com/">ElephantSQL (Hosting service for the database for this application)</a>
  * <a href="https://cloudinary.com/?&utm_campaign=1329&utm_content=instapagelogocta-selfservetest">Cloudinary (Cloud based storage for all media files)</a>
  * <a href="https://heroku.com/">Heroku (Application hosting service)</a>
  * <a href="https://bootstrapstudio.io/">Bootstrap Studio</a>

<hr>

# Credits #

### Coding ###

* All the resources below, were extremly helpful in creating the project. Whenever I needed help stackoverflow and Code Institute walkthrough projects help immensily.

* <a href="https://google.com">Google</a>
* <a href="https://ui.dev/amiresponsive">AMI Responsive</a>
* <a href="https://stackoverflow.com/">Stack Overflow</a>
* <a href="https://freepik.com/">FreePik</a>
* <a href="https://icons8.com">Icon8</a>
* <a href="https://https://codeinstitute.net/">Code Institute</a>
* <a href="https://getbootstrap.com/docs/5.3/getting-started/introduction/">Boostrap Documentations</a>
* <a href="https://bootstrapstudio.io/">Boostrap Studio</a>

* All my images were sourced from FreePik, and any copyrights are reserved for the owners as these are just for display purposes only.

* Of course, without Code Institute providing the necessary guidance, this project could not exist. And Student Care for providing support when needed the most.

[def]: #credits