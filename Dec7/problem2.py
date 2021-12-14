def createLookupTable(maxValue):
    table = {}
    fuelCost = 0
    totalCost = 0
    for movement in range(0, maxValue + 1):
        totalCost += fuelCost
        fuelCost += 1
        table[movement] = totalCost
    return table


def getMaxPos(positions):
    maxVal = 0
    for pos in positions:
        if pos > maxVal:
            maxVal = pos
    return maxVal


def main():
    positions = []
    with open('input.txt') as f:
        for line in f:
            positions = [int(pos, 10) for pos in line.strip().split(",")]

    maxVal = getMaxPos(positions)
    costTable = createLookupTable(maxVal)

    leastFuel = costTable[maxVal] * len(positions)
    for alignment in range(0, maxVal):
        sum = 0
        for pos in positions:
            movement = abs(pos - alignment)
            cost = costTable[movement]
            sum += cost

        if sum < leastFuel:
            leastFuel = sum

    print(leastFuel)

if __name__ == '__main__':
    main()
