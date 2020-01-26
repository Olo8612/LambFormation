import boto3
from cleanUpUserGroup import cleanUpUserGroup

cfClient = boto3.client('cloudformation')

def lambdaHandler(event, context):
    useCaseToDelete = event['useCaseName']
    cleanUpUserGroup(useCaseToDelete)
    
    useCaseStackName = f'{useCaseToDelete}-resources'
    cfClient.delete_stack(
        StackName='string',
    )
    
