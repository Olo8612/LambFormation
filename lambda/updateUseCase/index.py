import boto3
import os

cfClient = boto3.client('cloudformation')
USE_CASE_STACK_PREFIX = os.environ['USE_CASE_STACK_PREFIX']
USE_CASE_TEMPLATE_URL = os.environ['USE_CASE_TEMPLATE_URL']

def lambdaHandler(event, context):
    useCaseName = event['useCaseName']
    users = event['users']
    createAttachment = 'yes'
    if users == []:
        createAttachment = 'no'
    stackName = f'{USE_CASE_STACK_PREFIX}-{useCaseName}'
    cfClient.update_stack(
        StackName=stackName,
        UsePreviousTemplate=True,
        Parameters=[
            {
                'ParameterKey': 'UserName',
                'ParameterValue': useCaseName,
            },
            {
                'ParameterKey': 'Users',
                'ParameterValue': users,
            },
            {
                'ParameterKey': 'UsersExist',
                'ParameterValue': createAttachment,
            }
        ],
        Capabilities=[
            'CAPABILITY_NAMED_IAM',
        ],
        OnFailure='ROLLBACK',
    )