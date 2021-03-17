# Todo List

Super simple todo app built in Python.

The instructions in this README file are designed to be followed to run tests on this app using Jenkins on a Windows machine.

## Prerequisites

First, install Python:

https://www.python.org/downloads/

Follow the default settings for Python, but make sure that the option to 'Add to PATH' is checked.

Next, add the location of the Python executable to your System PATH variable:
- Enter Windows Key + R and enter `AdvancedSystemProperties`
- Click on the `Environment Variables` button
- Under 'System variables', double-click on Path
- Add the following path to this value: `C:\Users\<your-username>\AppData\Local\Programs\Python\Python39` where `<your-username>` is your username

## Testing the App

Create a virtual environment and activate it:

```
python -m venv venv
source venv/Scripts/activate
```

Install the pip requirements and pytest/pytest-cov (make sure you're in the repo root directory):

```bash
python -m pip3 install -r requirements.txt pytest pytest-cov
```

You need to set the database URI that the app needs to connect to and a secret key. This is done using *environment variables*.

```bash
export DATABASE_URI=[YOUR_DB_URI]
export SECRET_KEY=[YOUR_SECRET_KEY]
```

The secret key can be any value.

The Database URI can be set to an in-memory database using SQLite:

```bash
export DATABASE_URI=sqlite:///data.db
```

To run the tests, run:

```
python -m pytest --doctest-modules --junitxml=junit/test-results.xml --cov=application --cov-report=xml --cov-report=html
```

This will generate a JUnit-style test report for the unit tests in the location `junit/test-results.xml`, as well as a coverage report labelled `coverage.xml` on the root of the directory.

## Running the App

Before you run the app for the first time, you must run the `create.py` python script to create the database schema.

```bash
python create.py
```

Then to run the app, simply enter the following in your bash terminal:

```bash
python app.py
```

The website will be accessible on port 5000 on your machine's IP.

Make sure the machine's firewall rules allow network traffic on port 5000.

To stop the application, enter `ctrl+C`.
