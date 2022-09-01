game = [[1, 0, -2],
        [1, -2, 2],
        [-2, 2, 1]]

def diag(game):
    diags = []
    for i in range(len(game)):
        diags.append(game[i][i])
    return diags
    
def reverse_diag(game):
    rev_diags = []
    for idx, row in enumerate(reversed(range(len(game)))):
        rev_diags.append(game[row][idx])
    return rev_diags
    
def board(game):
    print( 0, 1, 2)
    for index, row in enumerate(game):
        print(index, row)

#board(game)
print(diag(game))
#print(game[0][2], game[1][1], game[2][0])
print(reverse_diag(game))

