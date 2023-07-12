
## Description

Project Cost Calculator is a GUI-based Python application which helps users to calculate the cost of their project which involves software and hardware components.

The app provides the following features:

- Import a .json file with project details
- Make estimations based on the imported data (i.e. changing components, costs, adding or deleting components and updating the total cost)
- Start from a new template and create a project estimate from scratch 
- Export the estimations as a .json file

## Table of Contents

- [Libraries and Dependencies](#libraries-and-dependencies)
  - [Libraries](#libraries)
  - [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contact Information](#contact-information)
- [Tests](#tests)
- [License](#license)
- [References](#references)

## Libraries and Dependencies

The application relies on a number libraries and have a few dependencies to provide the intended functionalities.

### External Libraries

The application uses the following external libraries:

- Tkinter: The application uses tkinter library to provide a GUI.
- Dataclasses: In order to store global data used across the app, a dataclass object is initiated.
- json: Importing and exporting .json functionality is provided by the json library.
- os: OS-level functionality (i.e. as opening files) is provided by os library.

### Dependencies

All modules used in the application are part of the standard Python distribution, so you do not need to install any modules.

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

The .json file that holds the project data should be structered like below:

~~~
{
	"Hardware": [{
			"type": "Board",
			"description": "A83-S",
			"count": 1,
			"price": 25,
			"man_cost": 14,
			"des_cost": 8,
			"cod_cost": 0,
			"tes_cost": 1.38
		},
		{
			"type": "RAM",
			"description": "256KB",
			"count": 2,
			"price": 5,
			"man_cost": 0,
			"des_cost": 16,
			"cod_cost": 0,
			"tes_cost": 2.76
		}
	],
	"Software": [{
			"type": "OS",
			"description": "HB/OS in ROM",
			"count": 1,
			"price": 0,
			"man_cost": 0,
			"des_cost": 9,
			"cod_cost": 8.85,
			"tes_cost": 1.38

		},
		{
			"type": "OS",
			"description": "MccOS",
			"count": 1,
			"price": 0,
			"man_cost": 0,
			"des_cost": 2.25,
			"cod_cost": 2.95,
			"tes_cost": 0.15
		}
	]
}
~~~


A sample template is also provided in the root folder.

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

