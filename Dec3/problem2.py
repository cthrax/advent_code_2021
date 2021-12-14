
def calculateColumn(columnIdx, list):
    count = {
        "0": 0,
        "1": 0,
    }
    for item in list:
        count[item[columnIdx]] += 1

    return count


def filterList(columnIdx, list, filterValue):
    newList = []
    for item in list:
        if item[columnIdx] == filterValue:
            newList.append(item)

    return newList


def findOxygen(list):
    columnCount = len(list[0])
    for column in range(0, columnCount):
        counts = calculateColumn(column, list)
        if counts["1"] >= counts["0"]:
            list = filterList(column, list, "1")
        else:
            list = filterList(column, list, "0")

        if len(list) == 1:
            return list[0]


def findCo2(list):
    columnCount = len(list[0])
    for column in range(0, columnCount):
        counts = calculateColumn(column, list)
        if counts["0"] <= counts["1"]:
            list = filterList(column, list, "0")
        else:
            list = filterList(column, list, "1")

        if len(list) == 1:
            return list[0]


def main():
    binaryList = []
    with open('input.txt') as f:

        for line in f:
            binary = line.strip()
            binaryList.append(binary)

    oxygen = findOxygen(binaryList)
    co2 = findCo2(binaryList)

    print(int(oxygen, 2) * int(co2, 2))


if __name__ == '__main__':
    main()
