
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
- [Features](#features)
- [Usage](#usage)
- [Contact Information](#contact-information)
- [Tests](#tests)
- [License](#license)
- [References](#references)

## Libraries and Dependencies

The application relies on a number libraries and have a few dependencies to provide the intended functionalities.

### External Libraries

The application uses the following external libraries:

- Tkinter (Python, N.D.): The application uses tkinter library to provide a GUI.
- Dataclasses: In order to store global data used across the app, a dataclass object is initiated.
- json: Importing and exporting .json functionality is provided by the json library.
- os: OS-level functionality (i.e. as opening files) is provided by os library.

### Dependencies

All modules used in the application are part of the standard Python distribution, so you do not need to install any modules.

However, depending on your system configuration, you may need to install tkinter. To install tkinter run the following command in the terminal:

#### Windows:
~~~
pip install tk
~~~

#### MacOS:
~~~
brew install python-tk
~~~
Note: Make sure you specify the correct Python version in the end.

#### Debian/Ubuntu:
~~~
sudo apt-get install python3-tk
~~~

## Installation

In order to install and run the application, follow the steps blow:

1. Unzip the application in your preferred directory.
2. Navigate to the project directory where *app.py* resides and run the application in the terminal/console by running the following commans:
~~~
python3 app.py
~~~
3. All modules used in the application are part of the standard Python distribution, so you do not need to install any modules to run the application.
4. However, it is recommended to update your Python version to the latest version.

## Features

The features of the application are as follows:

- Importing prohect data from a .json file
- Making estimations by changing costs of components or adding/deleting components
- Creating a project from scratch with a new template
- Exporting project data as a .json file

## Usage

1. Starting the application:

Open the terminal, make sure that you are in the folder where you unzipped the application files (navigate to the appropriate folder if needed) and run the following command:
~~~
python3 app.py
~~~
You can also use your favourite IDE to run the application.

![app1.png](assets%2Fapp1.png)

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

The user can update the cost of the components and update the project cost by clicking on the "Update" button at the bottom at the bottom of the table.

![app2.png](assets%2Fapp2.png)

4. Using a new template to create a project estimate:

The user can open an empty template (by clicking on "Start with a new template" button on the main screen or clicking on "New Template" from File menu) and add components and associated costs manually to calculate the total cost of the project.

![app3.png](assets%2Fapp3.png)

5. Adding/deleting components:

To add or delete a component, the user has to edit the .json file that holds the project data. The user can do this conveniently by selecting "Open and edit .json" from the File menu. This will open the .json file in the default app.

6. Exporting project estimate as a .json file:

The project can be exported as a .json file simply by selecting "Export .json" from File menu.

## Contact Information

You can contact the developer (Etkin Getir) at eg22518@essex.ac.uk for questions, queries, ideas and contributions. All queries will be responded within 72 hours.

## Tests

Using pytest library, a total of 7 test cases were written for the application in order to test the basic functionality.

Test cases can be found under tests folder, in tests.py file and fixtures used can be found in conftest.py file.

In order to run the tests pytest, mock and pytest-mock packages should be isntalled by running the commands below:

~~~
pip install mock
pip install pytest
pip install pytest-mock
~~~

Tests can be run by running the following command in the tests folder:
~~~
pytest tests.py
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

Python.org (N.D.) tkinter — Python interface to Tcl/Tk. Available from: https://docs.python.org/3/library/tkinter.html [Accessed 12 July 2023]
Python.org (N.D.) dataclasses — Data Classes. Available from: https://docs.python.org/3/library/dataclasses.html [Accessed 12 July 2023]
Python.org (N.D.) json — JSON encoder and decoder. Available from: https://docs.python.org/3/library/json.html [Accessed 12 July 2023]
Python.org (N.D.) os — Miscellaneous operating system interfaces. Available from: https://docs.python.org/3/library/os.html [Accessed 12 July 2023]