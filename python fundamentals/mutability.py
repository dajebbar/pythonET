game = 'I want to play a game'
# game = [1, 2, 3]
print(id(game))
def board():
    # print(game)
    global game 
    game = 'game'
    # game[1] = -99
    print(game)
    print(id(game))
    

print(game)
board()
print(game)
print(id(game))