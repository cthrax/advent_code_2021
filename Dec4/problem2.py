class Cell:
    def __init__(self, value):
        self.value = value
        self.marked = False


class Board:
    def __init__(self):
        self.rows = []
        self.hasWon = False

    def addLine(self, line):
        columns = []
        for value in line.strip().split(" "):
            if value != '':
                columns.append(Cell(value))
        self.rows.append(columns)

    def markNumber(self, number):
        for row in self.rows:
            for cell in row:
                if cell.value == number:
                    cell.marked = True

    def isWinner(self):
        columns = {}
        for rowIdx, row in enumerate(self.rows):
            rowComplete = True
            for colIdx, cell in enumerate(row):
                if columns.get(colIdx) is None:
                    columns[colIdx] = True

                if not cell.marked:
                    rowComplete = False
                    columns[colIdx] = False
            if rowComplete:
                self.hasWon = True
                return True

        for columnComplete in columns.values():
            if columnComplete:
                self.hasWon = True
                return True

    def unmarkedSum(self):
        sum = 0
        for row in self.rows:
            for cell in row:
                if not cell.marked:
                    sum += int(cell.value, 10)

        return sum


def main():
    callOrder = None
    boards = []
    with open('input.txt') as f:
        board = None
        for line in f:
            if callOrder is None:
                callOrder = line.strip().split(',')
            elif line.strip() == '':
                if board is not None:
                    boards.append(board)
                board = Board()
            else:
                board.addLine(line)

    lastWinner = None
    lastWinningDraw = None
    for draw in callOrder:
        for board in boards:
            if not board.hasWon:
                board.markNumber(draw)
                if board.isWinner():
                    lastWinner = board
                    lastWinningDraw = draw

    print(lastWinner.unmarkedSum() * int(lastWinningDraw, 10))


if __name__ == '__main__':
    main()
