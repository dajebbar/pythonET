players = [1, 0]
choice = 1

for _ in range(10):
    current_player = choice + 1
    # print(current_player)
    choice = players[choice]


# Other method
import itertools

player_choice = itertools.cycle(range(1, 3))
for _ in range(10):
    print(next(player_choice))