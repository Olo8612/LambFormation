import boto3
import os

cfClient = boto3.client('cloudformation')
USER_STACK_PREFIX = os.environ['USER_STACK_PREFIX']

def lambdaHandler(event, context):
    userToDelete = event['UserName']
    userStack = f'{USER_STACK_PREFIX}-{userToDelete}'
    cfClient.delete_stack(
        StackName=userStack
    )