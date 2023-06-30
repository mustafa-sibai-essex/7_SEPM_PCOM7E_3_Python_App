# Project Cost Calculator

## Description

Project Cost Calculator is a GUI-based Python application which helps users to calculate the cost of their project which involves software and hardware components.

The app provides the following features:

- Import a .json file with project details
- Make estimations based on the imported data 
- Start from a new template and create a project estimate from scratch 
- Export the estimations as a .json file

## Table of Contents

- [External Libraries and Dependencies](#external-libraries-and-dependencies)
  - [External Libraries](#external-libraries)
  - [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contact Information](#contact-information)
- [Tests](#tests)
- [License](#license)
- [References](#references)

## External Libraries and Dependencies

The application relies on a number libraries and have a few dependencies to provide the intended functionalities.

### External Libraries

The application uses the following external libraries:

- anytree (Anytree, N.D.): Provides the basic features for attack trees such as Node class and attack tree representation.
- cmd (Python.org, 2023a): A simple framework for command line-oriented applications.
- json (Python.org, 2023b): A basic .json encoder and decoder for python.
- copy (Python.org, 2023c): Provides deepcopy() function to create a new compound object by recursively cloning child objects of the original.
- time: (Python.org, 2023d): Provides a variety of time-related functions. In the app, only sleep() function is used to the interaction more human-friendly (i.e. by pausing for certain time to allow the user to read the messages displayed).

For unit testing, the following external libraries were used:
- unittest (Python.org, 2023e): Provides the unit testing functionality.
- mock (Foord, 2023): Provides the ability to mock user input or variables for testing purposes.
- os (Python.org, 2023f): Provides the ability to use operating system dependent functionality.

Please follow the links in the references to know more about these external libraries.

### Dependencies

Sole dependency of the application is Graphviz (2023) - an open source graph visualisation software. Please refer to the installation section for details about how to install it.

It should also be noted that the application was written in Python 3.10.5 and it is advised to update the Python version on the client machines if necessary.

## Installation

In order to install and run the application, follow the steps blow:

1. Unzip the application in your preferred directory.
2. Navigate to the project directory where *app.py* resides and run the application in the terminal/console by running the following commans:
~~~
python3 app.py
~~~
3. All modules used in the application are part of the standard Python distribution, so you do not need to install any modules to run the application.
4. However, it is recommended to update your Python version to the latest version.

## Usage

1. Starting the application:

Open the terminal, make sure that you are in the folder where you unzipped the application files (navigate to the appropriate folder if needed) and run the following command:
~~~
python3 app.py
~~~
You can also use your favourite IDE to run the application.

2. Importing a .json file:

The .json file that will be important should be structered like below:

A sample template is also provided with the application, in the root folder.

3. Making estimations:

4. Using a new template to create a project estimate:

5. Exporting project estimate as a .json file:

## Features

The features of the application are as follows:

## Contact Information

You can contact the developer (Etkin Getir) at eg22518@essex.ac.uk for questions, queries, ideas and contributions. All queries will be responded within 72 hours.

## Tests

Using unittest library, a total of XX test cases were written for the application.


Test cases can be found in the unit_tests.py file and can be run by running the following command (verbose mode):
~~~
python3 -m unittest -v unit_tests
~~~

## License

MIT License (MIT)

Copyright (c) 2023 Mustafa Sibai & Etkin Getir

Permission is hereby granted, free of charge, to any person obtaining a copy  of this software and associated documentation files (the "Software"), to deal  in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is 
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## References

