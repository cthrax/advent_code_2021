
class School:
    def __init__(self):
        self.counts = {}
        for day in range(0, 8 + 1):
            self.counts[day] = 0

    def addFish(self, initial=8):
        self.counts[initial] += 1

    def tick(self, days=1):
        for day in range(0, days):
            addedFish = self.counts[0]
            for cycle in range(1, 8+1):
                self.counts[cycle - 1] = self.counts[cycle]
            self.counts[8] = addedFish
            self.counts[6] += addedFish

    def currentCount(self):
        sum = 0
        for count in self.counts.values():
            sum += count
        return sum


def main():
    school = School()
    with open('input.txt') as f:
        for line in f:
            for initial in line.strip().split(","):
                school.addFish(int(initial, 10))

    school.tick(80)
    print(school.currentCount())


if __name__ == '__main__':
    main()
