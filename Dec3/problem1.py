def main():
    columnCounts = {}
    with open('input.txt') as f:
        for line in f:
            binary = line.strip()
            for idx, value in enumerate(reversed(binary)):
                if columnCounts.get(idx) is None:
                    columnCounts[idx] = {"0": 0, "1": 0}

                columnCounts[idx][value] += 1

    gamma = []
    epislon = []
    orderedKeys = list(columnCounts.keys())
    orderedKeys.sort(reverse=True)
    for column in orderedKeys:
        counts = columnCounts[column]

        if counts['0'] > counts['1']:
            gamma.append('0')
            epislon.append('1')
        else:
            gamma.append('1')
            epislon.append('0')

    gamma = int(''.join(gamma), 2)
    epislon = int(''.join(epislon), 2)

    print(gamma * epislon)


if __name__ == '__main__':
    main()
