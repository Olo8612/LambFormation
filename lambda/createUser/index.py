import boto3
import os

cfClient = boto3.client('cloudformation')
USER_TEMPLATE_URL = os.environ['USER_TEMPLATE_URL']
USER_STACK_PREFIX = os.environ['USER_STACK_PREFIX']

def lambdaHandler(event, context):
    stackName = f'{USER_STACK_PREFIX}{event["UserName"]}'
    cfClient.create_stack(
        StackName=stackName,
        TemplateURL=USER_TEMPLATE_URL,
        Parameters=[
            {
                'ParameterKey': 'UserName',
                'ParameterValue': event['UserName'],
            },
        ],
        Capabilities=[
            'CAPABILITY_NAMED_IAM',
        ],
        OnFailure='ROLLBACK',
    )