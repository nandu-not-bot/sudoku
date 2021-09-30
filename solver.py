from pprint import pprint

unsolved_board = [
    #0  1  2  3  4  5  6  7  8
    [3, 0, 6, 5, 0, 8, 4, 0, 0],  # 0
    [5, 2, 0, 0, 0, 0, 0, 0, 0],  # 1
    [0, 8, 7, 0, 0, 0, 0, 3, 1],  # 2
    [0, 0, 3, 0, 1, 0, 0, 8, 0],  # 3
    [9, 0, 0, 8, 6, 3, 0, 0, 5],  # 4
    [0, 5, 0, 0, 9, 0, 6, 0, 0],  # 5
    [1, 3, 0, 0, 0, 0, 2, 5, 0],  # 6
    [0, 0, 0, 0, 0, 0, 0, 7, 4],  # 7
    [0, 0, 5, 2, 0, 6, 3, 0, 0],  # 8
]

class Solver:
    def __init__(self, board):
        self.board = board

    def is_board_legal(self):
        def check(arr: list) -> bool:
            arr = [x for x in arr if x != 0]
            return len(arr) == len(set(arr))

        if len(self.board) != 9:
            return False

        for row in self.board:
            if len(row) != 9:
                return False

            if not check(row):
                return False

        for i in range(9):
            if not check(self._get_column(i)):
                return False

        for i in range(3):
            for j in range(3):
                if not check(self._get_block(i, j)):
                    return False

        return True

    def solve(self) -> bool:
        if not self.is_board_legal():
            return False

        if len(self.empty_coords) == 0:
            return True

        for coord in self.empty_coords:
            row, col = coord

            for n in range(1, 10):
                if self._is_legal(row, col, n):

                    self.board[row][col] = n

                    if self.solve():
                        return True

                    self.board[row][col] = 0

            return False

    @property
    def empty_coords(self):
        arr = []
        for i, row in enumerate(self.board):
            for j, element in enumerate(row):
                if element == 0:
                    arr.append((i, j))

        return arr

    # coords = (row, col)
    def _get_column(self, col: int) -> list:
        return [row[col] for row in self.board]

    def _get_block(self, row: int, col: int) -> list:
        row_block = (row // 3 + 1) * 3
        col_block = (col // 3 + 1) * 3
        return_list = []
        for l in [
            r[col_block - 3 : col_block] for r in self.board[row_block - 3 : row_block]
        ]:
            for i in l:
                return_list.append(i)

        return return_list

    def _is_legal(self, row: int, col: int, num: int) -> bool:
        if num in self.board[row]:
            return False

        if num in self._get_column(col):
            return False

        if num in self._get_block(row, col):
            return False

        return True


def main():
    solver = Solver(unsolved_board)
    if solver.solve():
        pprint(solver.board)
        print("Yay!")
        return

    print("Solving Failed! Board is Illegal!")


if __name__ == "__main__":
    main()
