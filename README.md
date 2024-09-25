# AWS Lambda

In the my_lambda.py file there is my AWS lambda function code

In the invoke_lambda.py file there is a script to execute an AWS Lambda function

Script uses AWS Python SDK - boto3

### In the script:
- There is a session initilization using AWS IAM User credentials;
- Defined Event, which is basicaly bunch of names;
- Invoking Lambda client that returns response;
- Finaly, response payoad is printed. It contains greetings for all the provided names.
