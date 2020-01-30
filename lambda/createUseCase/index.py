import boto3
import os

cfClient = boto3.client('cloudformation')
USE_CASE_STACK_PREFIX = os.environ['USE_CASE_STACK_PREFIX']
USE_CASE_TEMPLATE_URL = os.environ['USE_CASE_TEMPLATE_URL']

def lambdaHandler(event, context):
    useCaseName = event['useCaseName']
    users = event['users']
    users = ', '.join(users)
    createAttachment = 'yes'
    if users == []:
        createAttachment = 'no'
    stackName = f'{USE_CASE_STACK_PREFIX}{useCaseName}'
    cfClient.create_stack(
        StackName=stackName,
        TemplateURL=USE_CASE_TEMPLATE_URL,
        Parameters=[
            {
                'ParameterKey': 'UseCaseName',
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