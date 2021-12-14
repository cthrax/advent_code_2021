class VentLine:
    def __init__(self, start, end):
        self.x1, self.y1 = self._getCoords(start)
        self.x2, self.y2 = self._getCoords(end)
        self.isDiagonal = not (self.x1 == self.x2 or self.y1 == self.y2)

        if self.x2 < self.x1:
            temp = self.x1
            self.x1 = self.x2
            self.x2 = temp

        if self.y2 < self.y1:
            temp = self.y1
            self.y1 = self.y2
            self.y2 = temp

    def _getCoords(self, csv):
        return tuple([int(coord, 10) for coord in csv.split(",")])

    def maxX(self):
        return self.x2

    def maxY(self):
        return self.y2

    def getLine(self):
        coords = []
        for x in range(self.x1, self.x2 + 1):
            for y in range(self.y1, self.y2 + 1):
                coords.append([x, y])
        return coords


class Map:
    def __init__(self):
        self.grid = []
        self.ventLines = []
        self.maxIntersection = 0

    def _maxRow(self):
        return len(self.grid) - 1

    def _maxCol(self):
        if len(self.grid) > 0:
            return len(self.grid[0]) - 1
        else:
            return -1

    def _expandGrid(self, newMaxRows, newMaxCol):
        if self.grid is None:
            self.grid = []

        for rowIdx in range(0, newMaxRows + 1):
            if rowIdx > self._maxRow():
                self.grid.append([])

        for row in self.grid:
            for colIdx in range(0, newMaxCol + 1):
                if (len(row) - 1) < colIdx:
                    row.append(0)

    def setLineCross(self, x, y):
        self.grid[x][y] += 1

        if self.grid[x][y] > self.maxIntersection:
            self.maxIntersection = self.grid[x][y]

    def addVentLine(self, ventLine):
        self.ventLines.append(ventLine)
        if not ventLine.isDiagonal:
            if ventLine.maxX() > self._maxRow() or ventLine.maxY() > self._maxCol():
                self._expandGrid(ventLine.maxX(), ventLine.maxY())

            for coords in ventLine.getLine():
                self.setLineCross(coords[0], coords[1])

    def getMostDangerousCount(self):
        count = 0
        for row in self.grid:
            for cell in row:
                if cell > 1:
                    count += 1
        return count


def main():
    map = Map()
    with open('input.txt') as f:
        for line in f:
            start, end = line.strip().split(" -> ")
            map.addVentLine(VentLine(start, end))

    print(f"{len(map.grid)}x{len(map.grid[0])}")
    print(map.maxIntersection)
    print(map.getMostDangerousCount())


if __name__ == '__main__':
    main()
