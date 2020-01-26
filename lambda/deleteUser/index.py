import boto3

cfClient = boto3.client('cloudformation')

def lambdaHandler(event, context):
    userToDelete = event['userName']
    userStack = f'userStack-{userToDelete}'
    cfClient.delete_stack(
        StackName=userStack
    )