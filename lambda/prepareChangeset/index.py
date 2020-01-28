import boto3
import yaml
import os
import json
from getStateFromAWS import getStateFromAWS
from getStateFromFile import getStateFromFile
from prepareChangesetList import prepareChangesetList

CREATE_USER_LAMBDA = os.environ['CREATE_USER_LAMBDA']
DELETE_USER_LAMBDA = os.environ['DELETE_USER_LAMBDA']
CREATE_USECASE_LAMBDA = os.environ['CREATE_USECASE_LAMBDA']
UPDATE_USECASE_LAMBDA = os.environ['UPDATE_USECASE_LAMBDA']
DELETE_USECASE_LAMBDA = os.environ['DELETE_USECASE_LAMBDA']
codeCommitClient = boto3.client('codecommit')
lambdaClient = boto3.client('lambda')
s3 = boto3.resource('s3')

def lambdaHandler(event, context):
    currentState, currentUserSet = getStateFromAWS()
    desiredState = getStateFromFile()
    
    if desiredState == {}:
        print('Cannot find file for useCase maintenence')
        return
    if currentState == desiredState:
        print('Current state is same as file, nothing to change')

    createUseCaseDict, updateUseCaseDict, deleteUseCaseList, createUserSet, deleteUserList = prepareChangesetList(currentState, currentUserSet, desiredState)

    for user in createUserSet:
        payload = {'UserName': user}
        payload = json.dumps(payload)
        lambdaClient.invoke(
            FunctionName=CREATE_USER_LAMBDA,
            InvocationType='Event',
            LogType='Tail',
            Payload=bytes(payload, 'utf-8'),
        )

    for user in deleteUserList:
        payload = {'UserName': user}
        payload = json.dumps(payload)
        lambdaClient.invoke(
            FunctionName=DELETE_USER_LAMBDA,
            InvocationType='Event',
            LogType='Tail',
            Payload=bytes(payload, 'utf-8'),
        )

    for useCase in deleteUseCaseList:
        payload = {'useCaseName': useCase}
        payload = json.dumps(payload)
        lambdaClient.invoke(
            FunctionName=DELETE_USECASE_LAMBDA,
            InvocationType='Event',
            LogType='Tail',
            Payload=bytes(payload, 'utf-8'),
        )

    for useCase in createUseCaseDict:
        payload = {
            'useCaseName': useCase,
            'users': createUseCaseDict[useCase]
        }
        payload = json.dumps(payload)
        lambdaClient.invoke(
            FunctionName=CREATE_USECASE_LAMBDA,
            InvocationType='Event',
            LogType='Tail',
            Payload=bytes(payload, 'utf-8'),
        )

    for useCase in updateUseCaseDict:
        payload = {
            'useCaseName': useCase,
            'users': updateUseCaseDict[useCase]
        }
        payload = json.dumps(payload)
        lambdaClient.invoke(
            FunctionName=UPDATE_USECASE_LAMBDA,
            InvocationType='Event',
            LogType='Tail',
            Payload=bytes(payload, 'utf-8'),
        )
    

        
        