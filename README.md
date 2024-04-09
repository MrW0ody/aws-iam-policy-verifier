# Policy Verifier

Policy Verifier is a simple Python application that allows verification of JSON files according to the specified AWS IAM
Role Policy format.

## Description

The application contains a PolicyVerifier class, which allows you to check whether a given JSON file meets the
requirements specified for IAM policies in Amazon Web Services.

## Installation

1. Install python version 3.12 if you don't have his in your computer from:

       https://www.python.org/downloads/ 
   and choose version for your system

2. Create directory for example:  homework
3. Navigate to the created directory:
4. Open git and clone this project to your local machine:


      git clone repository name


5. Open repository directory in pycharm or visual studio code
6. create virtual environment in repository directory:
      

      pip install virtualenv
      
      virtualenv venv
      
      enter venv\scripts\activate
      
6. Install requirements.txt:


      pip install -r requirements.txt

7. Run the application:


   If you are usign pycharm open main.py file and press:

         ctrl+shift+F10

   or if you are using vscode enter in terminal:
            
         python main.py

## Usage

To use Policy Verifier, simply provide the path to the JSON file you want to verify.
The return value of the `verify_iam_policy` method is True or False, depending on whether the JSON file meets the
specified
IAM policy requirements.

## Tests

The application includes a set of tests that can be run using pytest. To do this, make sure you have the pytest package
installed, and then run:

<h2>To run tests enter in terminal</h2>

      pytest