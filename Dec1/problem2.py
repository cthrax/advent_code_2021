def main():
    prev = []
    increased = 0
    currentSum = 0

    with open('input.txt') as f:
        for line in f:
            if len(prev) != 3:
                val = int(line.strip())
                prev.append(val)
                currentSum += val
            else:
                val = int(line.strip())
                oldStart = prev.pop(0)
                prevSum = currentSum
                currentSum -= oldStart
                currentSum += val
                if currentSum > prevSum:
                    increased += 1
                prev.append(val)

    print(increased)


if __name__ == '__main__':
    main()
