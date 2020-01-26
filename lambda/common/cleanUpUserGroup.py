import boto3

iamClient = boto3.client('iam')

def cleanUpUserGroup(useCaseName):
    userGroup = f'{useCaseName}-UserGroup'
    userGroupUserList = iamClient.get_group(
        GroupName = userGroup
    )['Users']

    for user in userGroupUserList:
        iamClient.remove_user_from_group(
            GroupName=userGroup,
            UserName=user['UserName']
        )

    return