game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]


def game_board(player=0, row=0, column=0, just_display=False):
        print("   0  1  2")
        if not just_display:
                game[row][column] = player
        for count, row in enumerate(game):
                print(count, row)

game_board(just_display=True)
print()
game_board(2, 1, 1)
# game[1][1] = 1
