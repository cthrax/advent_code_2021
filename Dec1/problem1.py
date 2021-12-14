def main():
    prev = None
    increased = 0
    with open('input.txt') as f:
        for line in f:
            if prev is None:
                prev = int(line.strip())
            else:
                val = int(line.strip())
                if val > prev:
                    increased += 1
                prev = val

    print(increased)


if __name__ == '__main__':
    main()
