
def gameboard():
        rows, cols = (20, 20)
        gameboard = [[0]*cols] * rows
        gameboard[0][0] = 0
        gameboard[0][0] = 1
        for row in gameboard:
            print(row)

gameboard()