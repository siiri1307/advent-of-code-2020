import re


def readFile():
    file = open("day2_input.txt")
    input = file.readlines()
    file.close()
    return input


def isValid(min, max, char, code):
    # first part of the task
    # charCount = code.count(char)
    # if (charCount > min or charCount == min) and (charCount < max or charCount == max):
    # return True

    # second part of the task
    # in the task, the positions start from 1, not 0
    isInPos1 = code.count(char, min-1, min)
    isInPos2 = code.count(char, max-1, max)
    if (isInPos1 == 1) ^ (isInPos2 == 1):
        return True


def getValidCount(file):
    validPasswordCount = 0
    for line in file:
        min, max, letter, passcode = re.split(r'[ -]', line.strip("\n"))
        letter = letter.strip(":")
        if isValid(int(min), int(max), letter, passcode):
            validPasswordCount += 1
    return validPasswordCount


print(getValidCount(readFile()))
