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
    - [Front-end Design](#front-end-design)
    - [Testing](#testing)
      - [Unit Testing](#unit-testing)
      - [Integration Testing](#Integration-testing)

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

![risk-assessment](https://user-images.githubusercontent.com/54101378/118416137-1b132d00-b6a6-11eb-9e98-20579cf591e8.png)

The risk assessment for this project can be found in full [here](https://drive.google.com/file/d/1efTXkcBoZ8RQpSCS0N6ThL2ODaX4Y6YH/view?usp=sharing).

### Project Tracking
A Kanban board (Trello) was used to document the progress of my project, which has allowed me to effectively organise and prioritise tasks in a flexible way.

![trello](https://user-images.githubusercontent.com/54101378/118416223-79d8a680-b6a6-11eb-9122-2ad51dae53be.png)

The link to this board can be found [here](https://trello.com/b/PZQrC10M/order-management-app).

### Database Structure
The original proposed ERD (entity relationship diagram) showing the structure of the database can be seen below.

![erd-proposed](https://user-images.githubusercontent.com/54101378/118414456-8ce67900-b69c-11eb-8a26-9b8accd95af8.jpg)

However, to avoid making the application too complicated, I have decided to simplify the database structure, shown in the below screenshot.

![erd-actual](https://user-images.githubusercontent.com/54101378/118414461-9a036800-b69c-11eb-97f1-cfc355cfb157.jpg)

As shown in the ERD, the database structure models a one-to-many or one-to-none relationship between Users entities and Orders entities. The relationship allows a single user to either have no orders or place multiple orders. Whereas, a single order can only be associated with one user.

### Continuous Integration
![CI Pipeline](https://user-images.githubusercontent.com/54101378/118414434-6f191400-b69c-11eb-843a-c289091f16b1.jpg)

The continuous integration approach allowed me to frequently integrate modified code, and this is achieved through the use of automated testing tools to check the code before full integration. As soon as a new commit is pushed to the version control system (Github), Jenkins will automatically fetch the changes via Github webhook and run unit and integration tests. After the tests are completed, the developer will be able to view the reports produced and refactor the code if necessary.

The screenshot below shows a webhook has been successfully sent to Jenkins.

![github-webhook-delivery](https://user-images.githubusercontent.com/54101378/118415482-79d6a780-b6a2-11eb-96bc-11329d293d38.png)

The screenshot below shows Jenkins automatically creates a new build whenever it receives a Github webhook.

![github-webhook-triggered](https://user-images.githubusercontent.com/54101378/118415487-82c77900-b6a2-11eb-9e00-2cd35229a251.png)


#### Jenkins Script
1. Installation of the virtual environment
```bash
sudo apt install python3-pip python3-venv -y

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

2. Installation of webdriver
```bash
sudo apt install chromium-chromedriver -y

sudo apt install wget unzip -y
version=$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$(chromium-browser --version | grep -oP 'Chromium \K\d+'))
wget https://chromedriver.storage.googleapis.com/${version}/chromedriver_linux64.zip
sudo unzip chromedriver_linux64.zip -d /usr/bin
rm chromedriver_linux64.zip
```

3. Set environment variables
```bash
export DATABASE_URI
export SECRET_KEY
```

4. Run unit and integration tests
```bash
python3 -m pytest --cov=application --cov-report=xml --cov-report=html --junitxml=junit/test-results.xml
```

## Development

### Front-end Design

#### Homepage
The homepage (/ or /index) of the web app displays a list of orders in an organised way. Apart from that, it also shows the total number of orders placed. For each of the orders, there is a button to view details of the order and another button to update the status of an order (if applicable).

![homepage](https://user-images.githubusercontent.com/54101378/118413699-91109780-b698-11eb-8ea8-d5af715aeb52.png)

#### Register Page
When navigated to the register page (/register), the user must fill in all fields. The email address has to be unique for every user. If the user tries to enter an email address that already exists in the database, the app will show a message telling the user to use a different email address.

![register-page](https://user-images.githubusercontent.com/54101378/118413786-f19fd480-b698-11eb-9338-0912d591406f.png)

#### Add Order Page
The add order page allows the user to place an order by entering his/her email address. A message will appear telling the user to register first if the email address has not been registered.

![add-order-page](https://user-images.githubusercontent.com/54101378/118413814-1a27ce80-b699-11eb-9e41-6de2f1e39deb.png)

#### View Order Details Page
When navigated to the view order details page (/view-order), the page will display the information with the associated order.

![view-order-page](https://user-images.githubusercontent.com/54101378/118413956-d5e8fe00-b699-11eb-8e72-3c978fb5889a.png)

#### Update Order Page
On the update order page (/update-order), the store owner will be able to update the status of an order to 'out for delivery' or cancel the order (if the order has not been sent out).

![update-order-page](https://user-images.githubusercontent.com/54101378/118413833-3c215100-b699-11eb-87e9-3a7729a2e988.png)

### Testing
The screenshot below shows a test report produced by Jenkins showing the results of unit test and integration test.

![test](https://user-images.githubusercontent.com/54101378/118414389-282b1e80-b69c-11eb-8095-0a0ffb149bfb.png)

#### Unit Testing
Pytest is used in this project to test the route functions. The testing script is designed to assert that if a function is run, it should return an expected request response or a certain output. The testing script is run automatically everything when Jenkins receives a Github webhook. Jenkins console will print out the result of the build whether or not the tests were successful and also generate a coverage report.

If any of the unit testing fails, the entire Jenkins build is marked as failed, and the errors can be viewed within Jenkins built in console.

![jenkins-test-report](https://user-images.githubusercontent.com/54101378/118415429-2a907700-b6a2-11eb-8d60-df94545953ba.png)

The block of code shown below is an example of a unit test to test the function for registering a new user. First, a post request is sent to `/register` route with the required information, then query for the data from `Users` table. `assertEqual` tests that the first and second arguments are equal. If the values are not the same, the test will fail.

```python
class TestCreateUser(TestCase):
    def test_create_user(self):
        response = self.client.post(
            url_for("register"),
            data=dict(
                email="test2@gmail.com",
                name="Test2",
                house_number="82",
                postcode="G2 8PX",
                phone="0788888888",
            ),
            follow_redirects=True,
        )
        user = Users.query.filter_by(id=2).first()
        self.assertEqual("test2@gmail.com", user.email)
        self.assertEqual("Test2", user.name)
        self.assertEqual("82", user.house_number)
        self.assertEqual("G2 8PX", user.postcode)
        self.assertEqual("0788888888", user.phone)
```

#### Integration Testing
Integration testing is used to test the application as a whole, rather than mocking the application to it's routes as we do in unit testing. To do this, a Python package called `Selenium` is used to simulate a user interacting with our application directly, and test the results are as expected.

The code block shown below is an example of integration testing to test the behaviour of the application when a user tries to place an order with a non-existing account. When this situation occurs, the user will see an error message displayed under the text box. `assertIn` tests the first and second arguments are equal. The test will fail if the values are not equal.

```python
class TestAddOrder(TestBase):
    def test_add_order(self):
        self.driver.get(f"http://localhost:{self.TEST_PORT}/add-order")
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys('random@gmail.com')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

        error = self.driver.find_element_by_xpath('/html/body/form/p[2]').text
        self.assertIn('Account does not exist.', error)
```

## Future Improvements
There are a few improvements I would like to make in the future to optimise the functionality of the application:

- Implement additional tables to allow the store owner to view an order's timeline

- Implement a login page to allow the store owner to login to an admin panel

- Allow a user to modify his/her delivery details (as long as the order has not been despatched)

- Implement a notification tool to notify the customer whenever the status of his/her order changes via an email or a text message

- Implement an additional page for the user to enter a tracking number to extract information about an order

## Author
Jayden Seng Foong Lee

## Acknowledgements
- [Oliver Nochols](https://github.com/OliverNichols)
- [Harry Volker](https://github.com/htr-volker)
