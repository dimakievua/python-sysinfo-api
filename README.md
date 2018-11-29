PREPARATION AND RUN:
- Fetch code into repository:
git clone -b master git@github.com:dimakievua/python-sysinfo-api.git

- Install minimum modules needed to run application:
pip install flask json

- Set Environment variables:
For Linux and Mac:
export FLASK_APP=sysinfo
export FLASK_ENV=development

For Windows cmd, use set instead of export:
set FLASK_APP=sysinfo
set FLASK_ENV=development

- Run development server:
flask run

PACKAGE:
- After preparation setup.cy and MANIFEST.in run to install project in the virtual environment.
pip install -e .

- You can observe that the project is now installed with:
pip list

TEST:
- Install modules needed for test:
pip install pytest coverage

- To run the tests, use the pytest command:
pytest

- Measure the code coverage of your tests:
coverage run -m pytest

- View a simple coverage report in the terminal:
coverage report

- Create htmlcov/index.html report file:
coverage html

PRODUCTION:
The current standard for Python distribution is the wheel format, with the .whl extension. 
- Make sure the wheel library is installed first:
pip install wheel

- The bdist_wheel command will build a wheel distribution file:
python setup.py bdist_wheel

You can find the file in dist/flaskr-1.0.0-py3-none-any.whl. 
The file name is the name of the project, the version, and some tags about the file can install.

- Copy this file to another machine, set up a new virtualenv, then install the file with pip.
scp dist <host>:<path>

- Connect to <host> and cd <path>:
cd <path>

- Create virtual environment:
Linux:
python3 -m venv venv
On Windows:
py -3 -m venv venv

- If you needed to install virtualenv because you are on an older version of Python:
virtualenv venv

On Windows:
\Python27\Scripts\virtualenv.exe venv

- Activate the environment
Linux:
. venv/bin/activate
export FLASK_APP=sysinfo

On Windows:
source venv/Scripts/activate
set FLASK_APP=sysinfo

- Generate key and insert in venv/var/flaskr-instance/config.py:
python -c 'import os; print(os.urandom(16))'

- Install waiterss:
pip install waitress

- Install package:
pip install sysinfo-1.0.0-py3-none-any.whl

- Run production:
waitress-serve --call 'sysinfo:create_app'

USAGE:
Application has next endpoints:
/  - WEB page with system information
/healthcheck  - return Ok, could be used for automatic healthcheck testing
/api/all  - return JSON object with metadata and system laod info

Created by Dmytro Zhernosiekov based on Flask Tutorial documentation.
