names = ['Jeff', 'Gary', 'Jill', 'Samantha']

for name in names:
    statement = 'Hello there ' + name # This is easily read, but unfortunately not the ideal choice
    # print(statement)

for name in names:
    statement = ' '.join(['Hello there ', name]) # join() scales better
    # print(statement)
    
import os

file_loc = 'loc'
file_name = 'exp.txt'
# print(file_loc + '/' + file_name) # not the correct method

with open(os.path.join(file_loc, file_name)) as f: # better way
    print(f.read())


# Formatting
who = 'gary'
how_many = 12
print(who, ' bought ', how_many, ' apples today!') 
print(f'{who} bought {how_many} apples today!')