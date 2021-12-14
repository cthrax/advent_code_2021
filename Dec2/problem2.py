def main():
    depth = 0
    horizontal = 0
    aim = 0
    with open('input.txt') as f:
        for line in f:
            command, amount = line.strip().split(" ")
            amount = int(amount)

            if command == "forward":
                horizontal += amount
                depth += (aim * amount)
            elif command == "down":
                aim += amount
            elif command == "up":
                aim -= amount

    print(f'{command} {amount} - Horizontal: {horizontal}, Depth: {depth}, Aim: {aim}, Product: {horizontal * depth}')


if __name__ == '__main__':
    main()
