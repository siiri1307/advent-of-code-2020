def readInput():
    file = open("day6_input.txt")
    groupsAsStrings = file.read().split("\n\n")
    file.close()
    return groupsAsStrings


def getAllGroupsYesAnswers(groupStrings):
    groupsYesAnswers = []
    for group in groupStrings:
        personInAGroup = group.split("\n")
        groupsYesAnswers.append(getGroupYesAnswers(personInAGroup))
    return groupsYesAnswers


def getGroupYesAnswers(group):
    groupYesAnswers = []
    answersOfPeopleInGroup = []
    for person in group:
        personAnswers = list(person)
        answersOfPeopleInGroup.append(personAnswers)
    commonYesAnswersInGroup = list(
        set.intersection(*map(set, answersOfPeopleInGroup)))
    return commonYesAnswersInGroup


def sumGroupsYesAnswers(answersByGroups):
    sum = 0
    for group in answersByGroups:
        sum += len(group)
    return sum


groups = readInput()
yesAnswersOfGroups = getAllGroupsYesAnswers(groups)
print("The sum of the number of questions to which everybody in a group answered 'yes': " +
      str(sumGroupsYesAnswers(yesAnswersOfGroups)))
