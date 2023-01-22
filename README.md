# Assignment

# 1.Automation for Non-Functional Test cases
JMeter Performance Test Cases

This project contains a collection of JMeter test cases for performance testing of APIs provided. The test cases include two scenarios
with all the valid inputs and with all the invalid inputs:

- Create user test: Testing create_user API by sending a large number of concurrent creating user requests.
- Deposit: Tests the deposit functionality of the API by sending a large number of concurrent deposit requests.
- Send Money: Tests the send money API by sending a large number of concurrent send money requests.
- Withdraw Money: Tests the performance of Withdraw money API by sending a large number of concurrent withdrawing money requests.
- Get Balance: Tests the performance of get balance API by sending a large number of concurrent get_balance requests.

Instructions for Running the Test Cases:

1. Install Apache JMeter on your machine (https://jmeter.apache.org/download_jmeter.cgi)
2. Download the project files
3. Open Apache JMeter
4. Click on "Open" and select the ".jmx" file of the test case you want to run.
5. In the Thread Group, set the number of threads and the ramp-up period to your desired values.
6. Run the test by clicking on the "Start" button
7. Check the results in the "View Results Tree" listener

Note:
- The test cases includes dummy URL in url variable. If your application is running on a different host or port, you will need to update the appropriate values in the test cases.
- The test cases can use CSV files to provide input data but due to very less number of testcases I used the value directly without using any user defined variables.
- Please make sure that the target server is ready for the load before running the test. 
Note: As the detailed information depend on how the test cases are written and what the application is doing and what you want to measure, this is just a sample and can be modified accordingly.


# 2. Functional and Non Functional testcases
This includes the list of functional and non functional test cases for all the APIs provided.

# 3.Mock APIs functional testcases

This project contains a collection of functional test cases for testing mock APIs of Exbanking application using Postman.
The requests can be of folowing types and more. However, the collection inclueds only GET and POST requests as these are only required.
- GET test: Tests the GET endpoint of the mock API by sending a GET request and validating the response code and the response data.
- POST test: Tests the POST endpoint of the mock API by sending a POST request with a JSON payload and validating the response code and the response data.
- PUT test: Tests the PUT endpoint of the mock API by sending a PUT request with a JSON payload and validating the response code and the response data.
- DELETE test: Tests the DELETE endpoint of the mock API by sending a DELETE request and validating the response code.

Instructions for Running the Test Cases:

1. Install Postman on your machine (https://www.postman.com/downloads/)
2. Download the project files
3. Open Postman
4. Import the project files by clicking on the "Import" button and selecting the ".postman_collection.json" file
5. Run the test cases by clicking on the "Runner" button and selecting the collection and the environment
6. Check the test results in the "Test Results" tab

Note:
- The test cases assume that the mock API is running on the mockserver provided by Postman. If your mock API is running on a different host or port, you will need to update the environment variables in the project files.
- The test cases use variables to provide input data. Make sure the variables are correctly set before running the test.
- Make sure that the target server is ready before running the test.

# 4. Test Automation for functional testcases

   API Testing Automation Framework
   
   This project has a API testing framework in python using requests libray. it uses testing library, pytest for Running tests. 
   This framework can be used for any Restful application to verify APIs requests and response.
   
   Framework:
   It uses request library, The library is a powerful and easy-to-use library for making HTTP requests in Python. It abstracts the complexities of making requests behind a simple API so that you can focus on interacting with the service you are requesting from.
   and get the response later to verify the headers,response codes and other contents.
   
  Structure:
   /APIs (contain all the methods which hit the API with the payload and retutn the response)\
    &ensp/create_user.py\
    &ensp/deposit.py\
    &ensp/get_balance.py\
    &ensp/send.py\
    &ensp/withdraw.py\
   /Jsons(Contains all the jsons and payload required)\
    &ensp/jsons.py\
   /TestCases (Contain all the test cases)\
    &ensp/test_create_user.py\
    &ensp/test_deposit\
    &ensp/test_get_balance\
    &ensp/test_send\
    &ensp/test_withdraw\
   /TestData (contain all the endpints and variables\
    &ensp/APIbase\
   /Utility\
    &ensp/utilities\
   /runner\
   
   # Installation
   
   Installing Python

Python is a widely-used programming language that can be installed on a variety of operating systems.

Instructions for Windows:
1. Download the Python installer from the official website (https://www.python.org/downloads/)
2. Run the installer and follow the prompts to complete the installation.
3. Add Python to the PATH by checking the "Add Python to PATH" checkbox during the installation process.
4. Verify the installation by opening a command prompt and typing "python --version"

Instructions for Mac:
1. Download the Python installer from the official website (https://www.python.org/downloads/)
2. Run the installer and follow the prompts to complete the installation.
3. Verify the installation by opening a terminal and typing "python --version"


Note:
- Make sure to download the appropriate version of Python for your system (e.g. Python 3.x for Windows or Mac, Python 2.x for Linux)
- After installing python, you can install necessary packages or modules using pip or any other package manager, for example: pip install requests

Installing pytest and requests Library
pytest is a powerful and easy-to-use testing framework for Python, and the requests library allows you to easily make HTTP requests in Python.

Instructions for installing pytest:
1. Open a command prompt or terminal
2. Type the command "pip install pytest" and press Enter
3. Verify the installation by typing "pytest --version"

Instructions for installing requests:
1. Open a command prompt or terminal
2. Type the command "pip install requests" and press Enter
3. Verify the installation by typing "pip show requests"

Note:
- Make sure you have python installed in your system before installing pytest and requests library
- You can also use other package manager like conda, easy_install to install pytest and requests library

Installing Pycharm (If nor already installed)

PyCharm is an integrated development environment (IDE) for Python. It provides a wide range of useful features for writing, running, and debugging Python code.

Instructions for Windows:
1. Download the PyCharm installer from the official website (https://www.jetbrains.com/pycharm/download/)
2. Run the installer and follow the prompts to complete the installation.
3. Once the installation is complete, open PyCharm from the start menu or by running the "pycharm.exe" file in the installation directory.

Instructions for Mac:
1. Download the PyCharm DMG file from the official website (https://www.jetbrains.com/pycharm/download/)
2. Open the DMG file and drag the PyCharm icon to the Applications folder
3. Once the installation is complete, open PyCharm from the Applications folder

Note:
- Make sure to download the appropriate version of PyCharm for your system
- You can also use the Snap package manager to install PyCharm on Ubuntu and other Linux distributions
- PyCharm requires a Java runtime environment (JRE) to be installed on your system, if you don't have it installed, PyCharm will prompt you to install it during the setup process.

# Setup project in Pycharm

1. Go to the download folder where the project is downloaded and open the project folder.
2. Right click on it
3. Select open project as "Pycharm project"

