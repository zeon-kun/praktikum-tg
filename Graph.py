class KnightsTour:
    def __init__(self, size):
        self.N = size
        self.papan = [[-1 for _ in range(self.N)] for _ in range(self.N)]
        self.STEPS = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        self.counter = 0

    def is_safe(self, loc):
        x, y = loc
        return 0 <= x < self.N and 0 <= y < self.N and self.papan[x][y] == -1

    def search(self, pos=0, curr=(0, 0)):
        self.counter += 1
        print(str(self.counter) + '.', pos, curr)

        if pos == self.N ** 2:
            return True

        for step in self.STEPS:
            next_step = (curr[0] + step[0], curr[1] + step[1])

            if self.is_safe(next_step):
                self.papan[next_step[0]][next_step[1]] = pos
                if self.search(pos + 1, next_step):
                    return True

                self.papan[next_step[0]][next_step[1]] = -1

        return False


if __name__ == "__main__":
    size_of_chessboard = 8
    knights_tour = KnightsTour(size_of_chessboard)
    
    if knights_tour.search():
        print("Solution Found!")
    else:
        print("No Solution Found.")

    print(knights_tour.papan)
