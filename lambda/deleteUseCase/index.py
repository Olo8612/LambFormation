import boto3
import os

USE_CASE_STACK_PREFIX = os.environ['USE_CASE_STACK_PREFIX']

cfClient = boto3.client('cloudformation')

def lambdaHandler(event, context):
    print(event)
    useCaseToDelete = event['useCaseName']
    
    useCaseStackName = f'{USE_CASE_STACK_PREFIX}{useCaseToDelete}'
    response = cfClient.delete_stack(
        StackName=useCaseStackName,
    )    
