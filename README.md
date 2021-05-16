# QA DevOps Core Fundamental Project - Order Management App

## Contents
- [Brief](#brief)
    - [Requirements](#requirements)
    - [My Approach](#my-approach)
- [Architecture](#architecture)
    - [Risk Assessment](#risk-assessment)
    - [Project Tracking](#project-tracking)
    - [Database Structure](#database-structure)
    - [Continuous Integration](#continuous-integration)
- [Development](#development)
    - [Unit Testing](#unit-testing)
    - [Integration Testing](#Integration-testing)
    - [Front-end Design](#front-end-design)

## Brief

To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.

### Requirements

In addition to the brief, the tech stack required is as follows:

- A Kanban board (Trello or equivalent)
- Database: GCP SQL Server or other cloud hosted managed database
- Programming language: Python
- Unit testing with Python (Pytest)
- Integration testing with Python (Selenium)
- Front-end: Flask (HTML)
- Version control: Git
- CI server: Jenkins
- Cloud server: GCP Compute Engine

### My Approach

To satisfy the main objective of the project, I have decided to create an application which allows the store owner to do the following:

- Create
    - Register a new customer with the following details:
        - Email address
        - Name
        - House number
        - Postcode
        - Phone number

    - Place an order on the perspective of a customer
    - Generate a tracking number (random string) once the order status is changed to 'out for delivery'

- Read
    - The store owner can view the status of each order as well as the recipient's details

- Update
    - The store owner can update the status of an order (from initially 'order placed', to 'out for delivery', 'delivered', or 'order cancelled')

- Delete
    - The store owner can cancel an order as long as it has not been despatched

## Architecture

### Risk Assessment

A detailed risk assessment can be seen below, outlining the potential risks associated with this project:


The risk assessment for this project can be found in full [here](https://drive.google.com/file/d/1efTXkcBoZ8RQpSCS0N6ThL2ODaX4Y6YH/view?usp=sharing).

### Project Tracking

A Kanban board (Trello) was used to document the progress of my project, which has allowed me to effectively organise and prioritise tasks in a flexible way.

![trello-board](https://user-images.githubusercontent.com/54101378/118400853-54727b00-b65b-11eb-8351-273c35b00c47.png)

The link to this board can be found [here](https://trello.com/b/PZQrC10M/order-management-app).

### Database Structure

The original proposed ERD (entity relationship diagram) showing the structure of the database can be seen below.

![erd-proposed](https://user-images.githubusercontent.com/54101378/118401646-5db11700-b65e-11eb-89ec-ae9251f4aa0f.jpg)

However, to avoid making the application too complicated, I have decided to simplify the database structure, shown in the below screenshot.

![erd-actual](https://user-images.githubusercontent.com/54101378/118401846-2abb5300-b65f-11eb-9a9c-79dc044f5e16.jpg)

As shown in the ERD, the database structure models a one-to-many relationship between Users entities and Orders entities. The relationship allows a single user to either have no orders or place multiple orders. Whereas, a single order can only be associated with one user.

### Continuous Integration

![CI-Pipeline](https://user-images.githubusercontent.com/54101378/118402208-d5804100-b660-11eb-9538-3fe81a1048b3.jpg)

The continuous integration approach allowed me to frequently integrate modified code, and this is achieved through the use of automated testing tools to check the code before full integration. As soon as a new commit is pushed to the version control system (Github), Jenkins will automatically fetch the changes via Github webhook and run unit and integration tests. After the tests are completed, the developer will be able to view the reports produced and refactor the code if necessary.

#### Jenkins Script

## Development

### Front-end Design

#### Homepage
![homepage](https://user-images.githubusercontent.com/54101378/118413699-91109780-b698-11eb-8ea8-d5af715aeb52.png)

#### Register Page
![register-page](https://user-images.githubusercontent.com/54101378/118413786-f19fd480-b698-11eb-9338-0912d591406f.png)

#### Add Order Page
![add-order-page](https://user-images.githubusercontent.com/54101378/118413814-1a27ce80-b699-11eb-9e41-6de2f1e39deb.png)

#### View Order Details Page
![view-order-page](https://user-images.githubusercontent.com/54101378/118413956-d5e8fe00-b699-11eb-8e72-3c978fb5889a.png)

#### Update Order Page
![update-order-page](https://user-images.githubusercontent.com/54101378/118413833-3c215100-b699-11eb-87e9-3a7729a2e988.png)

### Unit Testing
Pytest is used in this project to test the route functions. The testing script is designed to assert that if a function is run, it should return an expected request response or a certain output. The testing script is run automatically everything when Jenkins receives a Github webhook. Jenkins console will print out the result of the build whether or not the tests were successful and also generate a coverage report.

If any of the unit testing fails, the entire Jenkins build is marked as failed, and the errors can be viewed within Jenkins built in console.

### Integration Testing

## Future Improvements

There are a few improvements I would like to make in the future to optimise the functionality of the application:

- Implement additional tables to allow the store owner to view an order's timeline

- Implement a login page to allow the store owner to login to an admin panel

- Allow a user to modify his/her delivery details (as long as the order has not been despatched)


## Author

Jayden Seng Foong Lee

## Acknowledgements

- [Oliver Nochols](https://github.com/OliverNichols)
- [Harry Volker](https://github.com/htr-volker)
