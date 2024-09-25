import boto3
import os
import json


AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_PRIVATE_KEY = os.getenv("AWS_PRIVATE_KEY")
AWS_REGION = os.getenv("AWS_REGION")


session = boto3.session.Session(
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_PRIVATE_KEY,
    region_name=AWS_REGION
)


event = {
    "names": [
        "Giorgi",
        "Ardak",
        "Adellina",
        "Gaioz"
    ]
}


lambda_client = session.client("lambda")


response = lambda_client.invoke(
    FunctionName='HelloStudentFunction',
    InvocationType='RequestResponse',  
    Payload=json.dumps(event)
)


response_payload = json.loads(response['Payload'].read())


print("Response from Lambda:")
print(json.dumps(response_payload, indent=4))