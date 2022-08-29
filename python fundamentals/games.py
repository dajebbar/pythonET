game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]


def game_board(player=0, row=0, column=0):
        print("   0  1  2")
        game[row][column] = player
        for count, row in enumerate(game):
                print(count, row)

game_board(2, 1, 1)
# game[1][1] = 1
game_board()