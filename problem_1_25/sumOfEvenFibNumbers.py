def findFibsum():
    item1 = 1
    item2 = 2
    item3 = 3
    total = 2
    while item3 < 4000000:
        item3 = item1 + item2
        if item3 % 2 == 0:
            total += item3
        item1 = item2
        item2 = item3
    return total


findFibsum()