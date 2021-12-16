def filterKnownValues(numbers, digits):
    for segment in digits:
        segmentSet = set([c for c in segment])
        if len(segment) == 2:
            # This is a 1
            numbers[1] = segmentSet
        elif len(segment) == 3:
            # This is a 7
            numbers[7] = segmentSet
        elif len(segment) == 4:
            # This is a 4
            numbers[4] = segmentSet
        elif len(segment) == 7:
            # this is an 8
            numbers[8] = segmentSet
        elif len(segment) == 5:
            numbers["fiveSegments"].append(segmentSet)
        elif len(segment) == 6:
            numbers["sixSegments"].append(segmentSet)
        else:
            print("Well I was wrong")


def filterSixSegments(numbers):

    # Six segments
    # (4 - 7) intersect (8 - X) if == [] then (6 or 9) else if === [d] then 0
    # (8 - 4) - X if == [] then (0 or 6) else if == [e] then 9
    # 6 = !9 and !0

    for segment in numbers["sixSegments"]:
        if len((numbers[8] - numbers[4]) - segment) == 1:
            numbers[9] = segment
        elif len((numbers[4] - numbers[7]).intersection(numbers[8] - segment)) == 1:
            numbers[0] = segment
        else:
            numbers[6] = segment

    del numbers["sixSegments"]


def filterFiveSegments(sevenSegments, numbers):

    for segment in numbers["fiveSegments"]:
        if segment == (numbers[8] - sevenSegments["topLeft"] - sevenSegments["bottomRight"]):
            numbers[2] = segment
        elif segment == (numbers[8] - sevenSegments["topRight"] - sevenSegments["bottomLeft"]):
            numbers[5] = segment
        else:
            numbers[3] = segment

    del numbers["fiveSegments"]


def sevenSegmentDisplay(numbers):
    # 4 - 1 = [b, d]
    # 1 - 4 = []
    # 4 - 7 = [b, d]
    # 7 - 1 = [a]
    # 1 - 7 = []
    # 8 - 1 = [a, b, d, e, g]
    # 8 - 4 = [a, e, g]
    # 8 - 7 = [b, d, e, g]
    # (8 - 7) - (4 - 7) = [e, g]

    # digits = [
    #     "abcefg",  # *0
    #     "cf",  # 1  Found
    #     "acdeg",  # **2
    #     "acdfg",  # **3
    #     "bcdf",  # 4  Found
    #     "abdfg",  # **5
    #     "abdefg",  # *6
    #     "acf",  # 7  Found
    #     "abcdefg",  # 8  Found
    #     "abcdfg",  # *9
    # ]

    # 7 - 4 = [a] top
    # (4 - 7) - (8 - 0) = [b] topLeft
    # (8 - 6) = [c] topRight
    # (8 - 0) = [d] middle
    # (8 - 9) = [e] bottomLeft
    # 1 - (8 - 6) = [f] bottomRight
    # ((8-7) - (4 - 7)) - (8 - 9) = [g] bottom
    return {
        "top": numbers[7] - numbers[4],
        "topLeft": (numbers[4] - numbers[7]) - (numbers[8] - numbers[0]),
        "topRight": numbers[8] - numbers[6],
        "middle": numbers[8] - numbers[0],
        "bottomLeft": numbers[8] - numbers[9],
        "bottomRight": numbers[1] - (numbers[8] - numbers[6]),
        "bottom": ((numbers[8] - numbers[7]) - (numbers[4] - numbers[7])) - (numbers[8] - numbers[9])
    }


def decode(digits, output):

    numbers = {
        1: None,
        4: None,
        7: None,
        8: None,
        "sixSegments": [],
        "fiveSegments": []
    }

    filterKnownValues(numbers, digits)
    filterSixSegments(numbers)
    sevenSegments = sevenSegmentDisplay(numbers)
    filterFiveSegments(sevenSegments, numbers)
    reverseLookup = {''.join(sorted(list(v))): k for k, v in numbers.items()}

    stringOutput = []
    for digit in output:
        stringOutput.append(str(reverseLookup[''.join(sorted(digit))]))

    return int(''.join(stringOutput), 10)


def testInput():
    digits = [
        "abcefg",  # *0
        "cf",  # 1  Found
        "acdeg",  # **2
        "acdfg",  # **3
        "bcdf",  # 4  Found
        "abdfg",  # **5
        "abdefg",  # *6
        "acf",  # 7  Found
        "abcdefg",  # 8  Found
        "abcdfg",  # *9
    ]

    output = ['abcefg', 'abcefg', 'bcdf', 'acdeg']

    return decode(digits, output)


def main():
    outputSum = 0
    with open('input.txt') as f:
        for line in f:
            digits, output = line.strip().split(" | ")
            digits = digits.split(" ")
            output = output.split(" ")

            outputSum += decode(digits, output)

    print(outputSum)


if __name__ == '__main__':
    main()
