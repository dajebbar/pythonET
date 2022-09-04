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

with open(os.path.join(file_loc, file_name)) as f:
    print(f.read())
