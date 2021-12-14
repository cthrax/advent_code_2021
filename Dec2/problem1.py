def main():
    depth = 0
    horizontal = 0
    with open('input.txt') as f:
        for line in f:
            command, amount = line.strip().split(" ")

            if command == "forward":
                horizontal += int(amount)
            elif command == "down":
                depth += int(amount)
            elif command == "up":
                depth -= int(amount)

    print(f'Horizontal: {horizontal}, Depth: {depth}, Product: {horizontal * depth}')


if __name__ == '__main__':
    main()
