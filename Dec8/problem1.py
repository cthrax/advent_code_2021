
def main():
    unique = 0
    with open('input.txt') as f:
        for line in f:
            digits, output = line.strip().split(" | ")
            digits = digits.split(" ")
            output = output.split(" ")

            for segment in output:
                if len(segment) == 2:
                    # This is a 1
                    unique += 1
                elif len(segment) == 3:
                    # This is a 7
                    unique += 1
                elif len(segment) == 4:
                    # This is a 4
                    unique += 1
                elif len(segment) == 7:
                    # this is an 8
                    unique += 1

    print(unique)


if __name__ == '__main__':
    main()
