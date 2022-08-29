game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]


def game_board(game_map, player=0, row=0, column=0, just_display=False):
        try:
                print("   0  1  2")
                if not just_display:
                        game_map[row][column] = player
                for count, row in enumerate(game_map):
                        print(count, row)
                        
                return game_map  
        except IndexError as e:
                print(f'Error: meke sure you input row/column as 0 1 or 2! {e}') 
                return False
        except Exception as e:
                print(f'Something went wrong! {e}')

game = game_board(game, just_display=True)
# print(game)
print()
game = game_board(game_board, 2, 5, 1)
# game[1][1] = 1
# print(game)
