import math


def getProbabilityWord(dataList):
    return 1 / len(dataList)


def getProbabilityLetter(letter, dataList):
    cnt = 0
    for elm in dataList:
        if letter in elm:
            cnt += 1
    return cnt / len(dataList)


def getEntropyWord(dataList):
    prob = getProbabilityWord(dataList)
    return - (prob * math.log(10, (1 / prob)))


def getEntropyLetter(letter, dataList):
    prob = getProbabilityLetter(letter, dataList)
    return - (prob * math.log(10, (1 / prob)))
