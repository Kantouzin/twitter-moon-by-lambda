#!/bin/sh
python-lambda-local --function lambda_handler --timeout 100 lambda_function.py lambda-local/event.json -e lambda-local/config.json
