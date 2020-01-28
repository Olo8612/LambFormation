def prepareChangesetList(currentState, currentUserSet, desiredState):
    createUseCaseDict = {}
    updateUseCaseDict = {}
    deleteUseCaseList = []
    desiredUserSet = set()
    createUserSet = set()
    deleteUserList = []
    for useCase in desiredState:
        for user in desiredState[useCase]:
            desiredUserSet.add(user)
        if useCase not in currentState:
            createUseCaseDict[useCase] = desiredState[useCase]
        if useCase in currentState and desiredState[useCase] != currentState[useCase]:
            updateUseCaseDict[useCase]= desiredState[useCase] 
    for useCase in currentState:
        if useCase not in desiredState:
            deleteUseCaseList.append(useCase)
    for user in desiredUserSet:
        if user not in currentUserSet:
            createUserSet.add(user)
    for user in currentUserSet:
        if user not in desiredUserSet:
            deleteUserList.append(user)

    
    return createUseCaseDict, updateUseCaseDict, deleteUseCaseList, createUserSet, deleteUserList 