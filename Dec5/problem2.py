class VentLine:
    def __init__(self, start, end):
        self.original = [start, end]
        self.x1, self.y1 = self._getCoords(start)
        self.x2, self.y2 = self._getCoords(end)
        self.isDiagonal = not (self.x1 == self.x2 or self.y1 == self.y2)
        self.isFortyFive = self.isDiagonal and pow((self.x2 - self.x1), 2) == pow((self.y2 - self.y1), 2)

        #if (self.y2 <= self.y1 and self.x2 <= self.x1) or (self.x2 >= self.x1 and self.y2 <= self.y1):
        if self.y2 <= self.y1:
            tempX = self.x2
            tempY = self.y2
            self.x2 = self.x1
            self.y2 = self.y1
            self.x1 = tempX
            self.y1 = tempY

        self.isDownRight = self.isFortyFive and (self.x2 > self.x1)

    def _getCoords(self, csv):
        return tuple([int(coord, 10) for coord in csv.split(",")])

    def maxX(self):
        return max(self.x2, self.x1)

    def minX(self):
        return min(self.x1, self.x2)

    def maxY(self):
        return max(self.y2, self.y1)

    def minY(self):
        return min(self.y1, self.y2)

    def getLine(self):
        coords = []
        if not self.isDiagonal:
            # print("line")
            for x in range(self.minX(), self.maxX() + 1):
                for y in range(self.minY(), self.maxY() + 1):
                    coords.append([x, y])
        elif self.isDownRight:
            # print("DownRight")
            x = self.x1
            y = self.y1

            while x <= self.x2:
                coords.append([x, y])
                x += 1
                y += 1

        elif self.isFortyFive:
            # print("UpRight")
            x = self.x1
            y = self.y1

            while y <= self.y2:
                coords.append([x, y])
                x -= 1
                y += 1
        # print(f"{self.original[0]} -> {self.original[1]} -- {self.x1},{self.y1} -> {self.x2},{self.y2}")
        # print(coords)
        return coords


class Map:
    def __init__(self):
        self.grid = []
        self.ventLines = []
        self.maxIntersection = 0
        self.colCount = 0
        self.rowCount = 0

    def _maxRow(self):
        return len(self.grid) - 1

    def _maxCol(self):
        if len(self.grid) > 0:
            return len(self.grid[0]) - 1
        else:
            return -1

    def _expandGrid(self, newMaxRows, newMaxCol):
        if self.colCount < newMaxCol:
            self.colCount = newMaxCol

        if self.rowCount < newMaxRows:
            self.rowCount = newMaxRows

        for rowIdx in range(0, self.rowCount + 1):
            if rowIdx > self._maxRow():
                self.grid.append([])

        for row in self.grid:
            for colIdx in range(0, self.colCount + 1):
                if (len(row) - 1) < colIdx:
                    row.append(0)

    def setLineCross(self, x, y):
        self.grid[x][y] += 1

        if self.grid[x][y] > self.maxIntersection:
            self.maxIntersection = self.grid[x][y]

    def addVentLine(self, ventLine):
        if not ventLine.isDiagonal or ventLine.isFortyFive:
            self.ventLines.append(ventLine)
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

    def print(self):
        for row in self.grid:
            colVals = []
            for col in row:
                colVals.append("." if col == 0 else str(col))
            print('  '.join(colVals))


def main():
    map = Map()
    with open('input.txt') as f:
        for line in f:
            start, end = line.strip().split(" -> ")
            map.addVentLine(VentLine(start, end))

#     map = Map()
#     rawInput = '''0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2'''
#     for line in rawInput.strip().split("\n"):
#         start, end = line.strip().split(" -> ")
#         map.addVentLine(VentLine(start, end))

    print(f"{len(map.grid)}x{len(map.grid[0])}")
    print(map.getMostDangerousCount())
    #map.print()


if __name__ == '__main__':
    main()
