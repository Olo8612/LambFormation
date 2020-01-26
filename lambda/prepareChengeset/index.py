import boto3
from botocore.exceptions import ClientError
import yaml

codeCommitClient = boto3.client('codecommit')
lambdaClient = boto3.client('lambda')
s3 = boto3.resource('s3')

def lambdaHandler(event, context):
    