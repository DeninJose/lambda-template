"""
AWS Lambda Function Module.

This module contains the entry point for an AWS Lambda function. The function
is designed to handle incoming events, process them, and return appropriate
responses.

Functions:
    lambda_handler(event, _): Processes the incoming event and returns a response.

Usage:
    Deploy this module as an AWS Lambda function. The `lambda_handler` function
    will be invoked automatically when the Lambda function is triggered.

Example:
    Event:
        {
            "key": "value"
        }
    Response:
        {
            "statusCode": 200,
            "body": "Hello from Lambda!"
        }
"""

def lambda_handler(event, _):
    """
    This function is the entry point for the AWS Lambda function.
    It processes the incoming event and returns a response.
    """
    # Log the incoming event
    print("Received event:", event)


    # Process the events
    response = {
        "statusCode": 200,
        "body": "Hello from Lambda!"
    }

    # Return the response
    return response
