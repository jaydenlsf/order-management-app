# QA DevOps Core Fundamental Project - Order Management App

## Contents

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
    - The store owner can view the status of each order as well as the recipent's details

- Update
    - The store owner can update the status of an order (between 'order placed', 'out for delivery', 'delivered', and 'order cancelled')

- Delete
    - The store owner can cancel an order if it has not been despatched

## Architecture

### Database Structure

