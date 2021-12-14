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

    leastFuel = maxVal * len(positions)
    for alignment in range(0, maxVal):
        sum = 0
        for pos in positions:
            sum += abs(pos - alignment)

        if sum < leastFuel:
            leastFuel = sum

    print(leastFuel)


if __name__ == '__main__':
    main()
