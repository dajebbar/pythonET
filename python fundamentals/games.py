game = [[2, 0, -2],
        [1, -2, 1],
        [-2, 2, 2],]


def game_board(game_map, player=0, row=0, column=0, just_display=False):
        try:
                print("   0  1  2")
                if not just_display:
                        game_map[row][column] = player
                for count, row in enumerate(game_map):
                        print(count, row)
                        
                return game_map  
        except IndexError as e:
                print(f'Error: make sure you input row/column as 0 1 or 2! {e}') 
                return False
        except Exception as e:
                print(f'Something went wrong! {e}')

def win(game):
        for row in game:
                # print(row)
                if row.count(row[0]) == len(row) and row[0] != 0:
                        print('winner!')
        check = []       
        for col in range(len(game)):
                for row in game:
                        check.append(row[col])
                if check.count(check[0]) == len(check) and check[0] != 0:
                        print('winner!')
                        
        diags = []
        for i in range(len(game)):
            diags.append(game[i][i])
        if diags.count(diags[0]) == len(diags) and diags[0] != 0:
                    print('winner!')
        
        rev_diags = []
        for idx, row in enumerate(reversed(range(len(game)))):
            rev_diags.append(game[row][idx])
        if rev_diags.count(rev_diags[0]) == len(rev_diags) and rev_diags[0] != 0:
                print('winner!')
                    
                        
            
        
                
        

game = game_board(game, just_display=True)
# print(game)
print()
# game = game_board(game_board, 2, 5, 1)
# game[1][1] = 1
# print(game)

game = win(game)

