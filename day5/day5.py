import math


def readInput():
    file = open("day5_input.txt")
    list = file.readlines()
    file.close()
    return list


def getRange(letter, rangeStart, rangeEnd):
    mid = (rangeEnd - rangeStart)/2
    if letter == "F" or letter == "L":
        return (rangeStart, rangeStart + mid)
    elif letter == "B" or letter == "R":
        return (rangeStart + mid, rangeEnd)


def getBinarySearchResult(list, range):
    for elem in list:
        range = getRange(elem, *range)
    return range[0]


def generateRowSeatTuples(inputList):
    tuples = []
    for elem in inputList:
        rowCoords = list(elem)[0:7]
        seatCoords = list(elem)[7:10]
        row = getBinarySearchResult(rowCoords, (0, 128))
        seat = getBinarySearchResult(seatCoords, (0, 8))
        tuples.append((row, seat))
    return tuples


def calculateSeatIds(tuplesArray):
    results = []
    for tuple in tuplesArray:
        result = int(tuple[0]) * 8 + int(tuple[1])
        results.append(result)
    return results


def getMaxSeatId(seatIdsArray):
    return max(seatIdsArray)


def getMissingSeatId(numbers):
    missing = None
    for i in range(0, len(numbers)-1):
        if numbers[i] + 1 != numbers[i+1]:
            missing = numbers[i] + 1
    return missing


taskInput = readInput()
tuplesArray = generateRowSeatTuples(taskInput)
numbers = calculateSeatIds(tuplesArray)
numbers.sort()
print("Highest seat ID on a boarding pass: " + str(getMaxSeatId(numbers)))
print("ID of my seat: " + str(getMissingSeatId(numbers)))
