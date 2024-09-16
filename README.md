RESTful API Testing Automation Framework
Overview
This project is a RESTful API Testing Automation Framework designed to simplify and streamline the testing process for RESTful APIs. 
It includes a configuration file, API request handling, and test cases to ensure the reliability and functionality of your APIs.

Configuration
The configuration file (config.yaml) allows you to specify essential parameters for your API requests and testing. Here's a sample configuration:
v 1.0.1

# REST API Automation Framework Configuration File

# API base URL
API base URL: https://site.name/api

# API Authorization Basic
Authorization Username: some_username
Authorization Password: some_password

# Postgres Database Connection
host: localhost
database: db_test
user: some_user
password: some_password
Make sure to update the values according to your specific API and database configurations.

API Requests
The api_requests.py module handles API requests, utilizing the requests library. 
The configuration parameters are loaded from the config.yaml file.


Getting Started

Clone the repository.
Install the required dependencies: pip install -r requirements.txt.
Configure your API and testing parameters in the config.yaml file.
Run your test cases using python API_test_executor.py.
Feel free to customize this README to better suit your project's structure and additional information. 

Good luck with your RESTful API Testing Automation Framework!