def readInput():
    numbers = []
    file = open("day1_input.txt")
    input = file.readlines()
    for line in input:
        numbers.append(int(line))
    file.close()
    return numbers


def findNumbers(list):
    for x in list:
        for y in list:
            for z in list:
                if(x + y + z == 2020):
                    return x * y * z


print(findNumbers(readInput()))
