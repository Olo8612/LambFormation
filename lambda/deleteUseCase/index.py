import boto3
from userGroupHandling import cleanUpUserGroup

cfClient = boto3.client('cloudformation')

def lambdaHandler(event, context):
    useCaseToDelete = event['useCaseName']
    cleanUpUserGroup(useCaseToDelete)
    
    useCaseStackName = f'lambformation-{useCaseToDelete}-resources'
    cfClient.delete_stack(
        StackName=useCaseStackName,
    )
    
