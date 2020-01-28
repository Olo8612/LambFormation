import boto3
from botocore.exceptions import ClientError
import yaml
import os

REPOSITORY_NAME = os.environ['REPOSITORY_NAME']
STATE_FILE = os.environ['STATE_FILE']
codeCommitClient = boto3.client('codecommit')

def getStateFromFile():
    try:
        desiredState = codeCommitClient.get_file(
            repositoryName='string',
            commitSpecifier='string',
            filePath='string'
        )
        usersFile = yaml.safe_load(desiredState['fileContent'])
    except ClientError as e:
        print(f'Unable to download state file: {STATE_FILE}, from repositor: {REPOSITORY_NAME}')
        print(f'Possible error: {e}')
        return {}
    return usersFile