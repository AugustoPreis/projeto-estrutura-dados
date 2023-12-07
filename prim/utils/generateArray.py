import random


def generateArray(length):
    return [random.randint(1, 1000) for _ in range(length)]
