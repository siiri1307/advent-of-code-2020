from functools import reduce


file = open("day3_input.txt")
map = file.readlines()
file.close()


def getColumn(row, column):
    rowLen = len(map[row].strip("\n"))
    if(column >= rowLen):
        mod = column % rowLen
        return mod
    return column


def isTree(row, column):
    if(map[row][column] == "#"):
        return True


def getNumberOfTreesPerTraversal(column, row):
    incrRow = row
    incrCol = column
    c = 0
    while row < len(map):
        if isTree(row, getColumn(row, column)):
            c += 1
        row += incrRow
        column += incrCol
    return c


def getFactors():
    traversals = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    treesPerTraversals = []
    for traversal in traversals:
        treesPerTraversals.append(
            getNumberOfTreesPerTraversal(traversal[0], traversal[1]))
    return treesPerTraversals


def getProduct():
    return reduce((lambda x, y: x * y), getFactors())


print(getProduct())
