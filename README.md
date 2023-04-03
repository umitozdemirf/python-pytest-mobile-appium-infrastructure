<h1>Pytest Appium Automation Project</h1>
This project is prepared for the self improvement.
<h2>Tool stack</h2>

* Python
* Pytest
* Appium
* Selenium
* PyYAML
* Faker

<h3>Requirements</h3>

* Python 3 or higher must be installed (Version 3 preferred) <a href="https://www.python.org/downloads/"> Python
  download page
* Pytest must be installed <a href="https://pypi.org/project/pytest/">Pytest download</a>,
* Appium must be installed <a href="https://appium.io/downloads.html">Appium download</a>,

<h3>Project Tree</h3>

```

.
├── README.md
├── app
│   └── app-debug.apk
├── config
│   ├── account
│   │   └── account_config.py
│   └── base_config.py
├── conftest.py
├── output
│   ├── assets
│   │   └── style.css
│   └── report.html
├── pages
│   ├── base_page.py
│   └── login
│       └── login_page.py
├── platform
│   └── app_android.yml
├── pytest.ini
├── requirements.txt
├── resources
│   └── validation.py
├── test
│   ├── output
│   │   ├── assets
│   │   │   └── style.css
│   │   └── report.html
│   └── test_login.py
└── utils
    └── data
        └── data_generator.py

```

<h4>Config Folder</h4>
Used for environment variables. There are usually *_config.py files.

<h4>Platform Folder</h4>
This will be used for Appium capabilities in the project. Capabilities should be defined in the YAML file.

<h4>Pages Folder</h4>
This will be used for Page Object Model implementation in the project. Locators should be defined at the top of the page.
The locator definition should not be made inside the methods. Actions of all steps are defined on pages.

<h4>Test folder</h4>
Test files, that is, test cases in Pytest format will be located under this folder.

<h4>Utils Folder</h4>
The utils class and methods of the project will be defined in this folder.

<h4>conftest.py</h4>
File where decorators such as global fixtures are defined for pytest.

<h4>pytest.ini</h4>
Required file for pytest configuration.

<h4>requirements.txt</h4>
The file required for the installation of project necessary libraries.

<h4>output/*</h4>
Generates pytest-html reports after each execution.

<h2>Naming Convention</h2>

Conditions are requested when naming. Names should be short and meaningful.

``directory names = my_directory (snake case)``

``variable name = my_variable (snake case)``

``method name = my_method (snake case)``

``class name = MyClass (Pascal case)``

``tag name = @MyTag (Pascal case)``



<h2> Test Run </h2>

Python CLI command to run tests.

execution tests :

``
python3 -m pytest
``

execution tests via specific test file

``
python3 -m pytest 'file path'
``

execution tests via marks

@pytest.mark.smoke should be added in the test case

``
pytest -v -m smoke
``
