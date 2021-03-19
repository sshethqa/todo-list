#!/bin/bash
source venv/bin/activate
python3 -m pytest --cov=application --junitxml=junit.xml --cov-report=xml
