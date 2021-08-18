# https://www.acmicpc.net/problem/22939

import sys

def distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def lenOfRoute(route: list, n):
    length = 0
    for i in range(n-1):
        length += distance(route[i], route[i+1])
    return length

def findShortestDistance(start, end, toppings):
    sequences = ((0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0))
    lengths = []
    for i in range(6):
        route = [start]
        sequence = sequences[i]
        for j in range(3):
            route.append(toppings[sequence[j]])
        route.append(end)
        lengths.append(lenOfRoute(route, 5))
    return min(lengths)

def main():
    n = int(sys.stdin.readline().rstrip())
    J, C, B, W = [], [], [], []
    for i in range(n):
        row = sys.stdin.readline().rstrip()
        for j in range(n):
            cell = row[j]
            if cell == "H":
                start = (i, j)
            elif cell == "#":
                end = (i, j)
            elif cell == "J":
                J.append((i, j))
            elif cell == "C":
                C.append((i, j))
            elif cell == "B":
                B.append((i, j))
            elif cell == "W":
                W.append((i, j))
    
    fieldLengths = []
    fieldLengths.append(findShortestDistance(start, end, J))
    fieldLengths.append(findShortestDistance(start, end, C))
    fieldLengths.append(findShortestDistance(start, end, B))
    fieldLengths.append(findShortestDistance(start, end, W))

    fieldNames = ("Assassin", "Healer", "Mage", "Tanker")
    print(fieldNames[fieldLengths.index(min(fieldLengths))])

main()