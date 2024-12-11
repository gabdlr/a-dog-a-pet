# A dog a pet
#### Video Demo: [Video url](https://www.youtube.com/shorts/PRFRn0t684g)
#### Description:
This project is meant to be the starting point of a pet adoptions web site. It allows users to register, register pets and ask for pets adoption. It also has a contact form which is not fully functional. It has been done using python with the Flask framework and a sqlite database.

The purpouse of the project is to build a web site where people looking to adopt a pet can contact with people that are offering pets for adoption, as a registered user you could do both, but this could actually be splitted into separate roles though. To adopt or publish a pet you'll need to fill the registration form which has validation both in the frontend and the backend making sure data is correct. After registration you have access to your profile where you can update some of your details as your email address or phone number, but not your name or lastname. In the pets page you can see all the listed pets for adoption whether you are registered or not, you can filter by attributes as pet type (cat or dog), sex and age range. Every pet has a picture and its details, like name, age, etc, and a link to ask to adopt it. If registered when clicking on the adopt link, it will set the pet as in 'pending' status adoption which is visually noticeable by the picture turning to grayscale, meaning other people can't ask to adopt it untill your request is rejected. If a non user tries to adopt a pet the link will lead to the login section. Only logged in users can see the add pet option in the menu, the add pet section also consists of a form with its validations, after succesfully submitting the pet data the user will be notified that the pets has been added and it will be publicly displayed in the pets section for everyone to see. A user can't adopt a pet that has published himself, it will simply ignore the request and redirect to the pet list without changes. 
Beside the adoptions there is information about the site itself and a contact form, it is not fully developed but it would be easy to extend and implement the functionality.

This projects uses a lot of resources from the flask environment as flask sqlalchemy orm, flask session, jinja, etc. It also integrates with cloudinary for the image hosting so having a cloudinary account is required for it to be fully functional as is. The deployed version also uses gunicorn as webserver but it can be run with the flask run command.

### General structure:
This app is divided in modules or "blueprints", it consists of a total of 4 modules: Users, Pets, Us and Main.

#### Users module
The users module resposability is to handle user related actions, as loging in, registering and updating user data, it consists of a couple of views and a User service.

#### Pets module
Pets module takes care of eveything related to the pets, as listing them and adding new ones, is consists of the pets and the registe pet views and a Pet service.

#### Us module
This module is intended for the site owners, it has a contact form and an about us view, basically only static assets a little logic.

#### Home module
Home module holds the entry point to the app, it only consists of a home page view

### Models:

This web app uses sqlalchemy ORM, the most important models are users and pets, then there is the logical model adoptions and lookup models like adoption status and pet kind.

### Services

#### User service

It consists of several user realated static methods (no DI in this project), it holds the logic for creating and updating users and loging in.

#### Pet service

Contains methods for listing and creating new pets, including handling image uploads and usage of Cloudinary sdk.

### Utils

Here we can found custom error classes, validation logic, constants and other necessary resources for the project to work properly.