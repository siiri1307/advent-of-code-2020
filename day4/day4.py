import string


def readInput():
    file = open("day4_input.txt")
    list = file.readlines()
    list.append("\n")
    file.close()
    return list


def dictGen(input):
    dict = {}
    splitBySpace = input.strip("\n").split(" ")
    for elem in splitBySpace:
        key, value = elem.split(":", 2)
        dict[key] = value
    return dict


def processInput(list):
    documents = []
    completeDoc = {}
    for line in list:
        if line == "\n":
            documents.append(completeDoc)
            completeDoc = {}
        else:
            partialDoc = dictGen(line)
            completeDoc = {**completeDoc, **partialDoc}
    return documents


def getListDifference(list1, list2):
    # list comprehension
    result = [item for item in list1 if not item in list2]
    return result


def containsRequiredFields(ob):
    requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    difBetweenRequiredAndObject = getListDifference(requiredFields, ob.keys())
    difBetweenObjectAndRequired = getListDifference(ob.keys(), requiredFields)
    if((not difBetweenObjectAndRequired and not difBetweenRequiredAndObject) or (len(difBetweenRequiredAndObject) == 1 and difBetweenRequiredAndObject[0] == "cid")):
        return True
    else:
        return False


def isValidProp(key, value):
    if(key == "byr"):
        return isInValidNumberRange(value, 1920, 2002)
    elif(key == "iyr"):
        return isInValidNumberRange(value, 2010, 2020)
    elif(key == "eyr"):
        return isInValidNumberRange(value, 2020, 2030)
    elif(key == "hgt"):
        return isValidHeight(value)
    elif(key == "hcl"):
        return isValidHairColor(value)
    elif(key == "ecl"):
        return isValidEyeColor(value)
    elif(key == "pid"):
        return isValidPid(value)
    elif(key == "cid"):
        return True


def containsValidValues(doc):
    for key in doc:
        if(not isValidProp(key, doc[key])):
            return False
    return True


def isValidHeight(value):
    if("cm" in value):
        heightCm = int(value.split("cm")[0])
        return isInValidNumberRange(heightCm, 150, 193)
    elif("in" in value):
        heightIn = int(value.split("in")[0])
        return isInValidNumberRange(heightIn, 59, 76)
    else:
        return False


def isInValidNumberRange(comparableYear, min, max):
    return int(comparableYear) >= min and int(comparableYear) <= max


def isValidHairColor(value):
    elemList = list(value)
    valid = list(map(lambda x: str(x), list(range(0, 10)))) + \
        list(string.ascii_lowercase)[0:6]
    return len(elemList) == 7 and elemList[0] == "#" and containsValidCharacters(elemList[1:7], valid)


def isValidEyeColor(value):
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def isValidPid(value):
    input = list(value)
    return len(input) == 9 and containsValidCharacters(input, ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])


def containsValidCharacters(charList, acceptedChars):
    for char in charList:
        if char not in acceptedChars:
            return False
    return True


def countValidPassports(documents):
    valid = 0
    for doc in documents:
        if containsRequiredFields(doc):
            if containsValidValues(doc):
                valid += 1
    return valid


documents = processInput(readInput())
print(countValidPassports(documents))
