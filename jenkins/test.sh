#!/bin/bash

# Install apt Dependencies
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv -y

# Create and source virtual environment
python3 -m venv venv
source venv/bin/activate

# Install pip requirements
pip3 install -r requirements.txt

# Run pytest
python3 -m pytest --cov=application --cov-report=xml --junitxml=junit/test-results.xml