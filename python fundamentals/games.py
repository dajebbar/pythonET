import itertools


def game_board(game_map, player=0, row=0, column=0, just_display=False):
        try:
                if game_map[row][column] != 0:
                        print('This cas is occupado! Choose another.')
                        return game_map, False
                # print("   0  1  2")
                print("   " + "  ".join(str(i) for i in range(len(game))))
                if not just_display:
                        game_map[row][column] = player
                for count, row in enumerate(game_map):
                        print(count, row)
                        
                return game_map, True 
        except IndexError as e:
                print(f'Error: make sure you input row/column as 0 1 or 2! {e}') 
                return game_map, False
        except Exception as e:
                print(f'Something went wrong! {e}')
                return game_map, False

def win(game):
        
        def all_same(lst):
                if lst.count(lst[0]) == len(lst) and lst[0] != 0:
                        return True
                else:
                        return False
        # Horizontal
        for row in game:
                # print(row)
                if all_same(row):
                        print(f"Player {row[0]} is the winner horizontally (-)!")
                        return True
        # Vertical      
        for col in range(len(game)):
                check = [] 
                for row in game:
                        check.append(row[col])
                if all_same(check):
                        print(f"Player {check[0]} is the winner vertically (|)!")
                        return True
        # Diagonal \       
        diags = []
        for i in range(len(game)):
            diags.append(game[i][i])
        if all_same(diags):
                    print(f"Player {diags[0]} has won Diagonally (/)")
                    return True
        # Diagonal /
        rev_diags = []
        for idx, row in enumerate(reversed(range(len(game)))):
            rev_diags.append(game[row][idx])
        if all_same(rev_diags):
                print(f"Player {rev_diags[0]} has won Diagonally (\\)")
                return True
        
        return False
                    
                        
            
        
                
play = True
players_choice = itertools.cycle([1, 2])
while play:
        game = [[0,  0,  0],
                [0,  0,  0],
                [0,  0,  0],]
        
        game_won = False
        game, _ = game_board(game, just_display=True)
        while not game_won:
                current_player = next(players_choice)
                print(f'current player: {current_player}')
                played = False
                
                while not played:
                        column_choice = int(input('What column do you want to play? (0 1 2) >> ' ))
                        row_choice = int(input('What row do you want to play? (0 1 2) >> ' ))
                        game, played = game_board(game, current_player, row_choice, column_choice)
                        
                if win(game):
                        game_won = True
                        again = input('The game is over! Would you like to play again? (y/n) ')
                        if again[0].lower() == 'y':
                                print('Restarting...')
                        else:
                                print('Bye ;-)')
                                play = False
                
   

# game = game_board(game, just_display=True)
# print(game)
# print()
# game = game_board(game_board, 2, 5, 1)
# game[1][1] = 1
# print(game)

# game = win(game)

