# for position search problem:

def manhattan(actual, goal):
    return abs(actual.x - goal.x) + abs(actual.y - goal.y)

def euclidean(actual, goal):
    return ((actual.x - goal.x) **2 + (actual.y - goal.y) **2) **.5
