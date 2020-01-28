import boto3

iamClient = boto3.client('iam')

def cleanUpUser(userName):
    userGroupList = iamClient.list_groups_for_user(
        UserName=userName
    )['Groups']

    for group in userGroupList:
        iamClient.remove_user_from_group(
            GroupName=group['GroupName'],
            UserName=userName
        )

    return

def cleanUpGroup(groupName):
    usersList = iamClient.get_group(
        GroupName=groupName,
    )['Users']

    for user in usersList:
        iamClient.remove_user_from_group(
            GroupName=groupName,
            UserName=user['UserName']
        )
    return