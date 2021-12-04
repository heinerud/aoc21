from dataclasses import dataclass


@dataclass
class Cell:
    value: int
    visited: int = False


def bingo_score(board, row, col):
    unvisited = [c for r in board for c in r if not c.visited]
    return board[row][col].value * sum(x.value for x in unvisited)


def bingo(board, row, col):
    if all(c.visited for c in board[row]):
        return bingo_score(board, row, col)
    if all(c.visited for c in (r[col] for r in board)):
        return bingo_score(board, row, col)
    return 0


if __name__ == "__main__":
    with open("04.in") as f:
        bingo_row = [int(x) for x in f.readline().split(",")]
        f.readline()

        boards = []
        board = []
        for l in f.readlines():
            l = l.strip()
            if not l:
                boards.append(board)
                board = []
            else:
                board.append([Cell(int(x)) for x in l.split()])
        boards.append(board)

        board_maps = []
        for board in boards:
            board_map = {}
            for r, row in enumerate(board):
                for c, n in enumerate(row):
                    board_map[n.value] = (r, c)

            board_maps.append(board_map)

    won = [False for _ in range(len(boards))]

    for x in bingo_row:
        for i, (board, board_map) in enumerate(zip(boards, board_maps)):
            if won[i]:
                continue
            try:
                row, col = board_map[x]
            except KeyError:
                continue

            board[row][col].visited = True

            score = bingo(board, row, col)
            if score:
                # Part 1
                if not any(won):
                    print(score)

                won[i] = True

                # Part 2
                if all(won):
                    print(score)
                    exit()
