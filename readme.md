# A dog a pet
#### Video Demo:  <URL HERE>
#### Description:
This project is meant to be the starting point of a pet adoptions web site. It allows users to register, register pets and ask for pets adoption. It also has a contact form which is not fully functional. It has been done using python with the Flask framework and a sqlite database.

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