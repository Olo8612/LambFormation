import boto3
import yaml
import os

cfClient = boto3.client('cloudformation')
USE_CASE_STACK_PREFIX = os.environ['USE_CASE_STACK_PREFIX']
USER_STACK_PREFIX = os.environ['USER_STACK_PREFIX']

def getStateFromAWS():
    useCaseStackList, userStackList = getCfStackList()
    stateDict = {}
    userSet = set()
    for user in userStackList:
        userSet.add(user.replace(USER_STACK_PREFIX, ''))
    for useCaseStack in useCaseStackList:
        usersParameter = cfClient.describe_stacks(
            StackName = useCaseStack
        )['Stacks'][0]['Parameters']
        useCase = useCaseStack.replace(USE_CASE_STACK_PREFIX, '')
        stateDict[useCase] = usersParameter[1]['ParameterValue']
    return stateDict, userSet

def getCfStackList():
    useCaseStackList = []
    userStackList = []
    
    paginator = cfClient.get_paginator('list_stacks')
    pageIterator = paginator.paginate(StackStatusFilter=['CREATE_COMPLETE', 'UPDATE_COMPLETE', 'UPDATE_ROLLBACK_COMPLETE'])
    for page in pageIterator:
        stack = page['StackSummaries']
        for output in stack:
            if USE_CASE_STACK_PREFIX in output['StackName']:
                useCaseStackList.append(output['StackName'])
                continue
            elif USER_STACK_PREFIX in output['StackName']:
                userStackList.append(output['StackName'])
    return useCaseStackList, userStackList