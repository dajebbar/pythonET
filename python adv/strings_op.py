names = ['Jeff', 'Gary', 'Jill', 'Samantha']

for name in names:
    statement = 'Hello there ' + name # This is easily read, but unfortunately not the ideal choice
    # print(statement)

for name in names:
    statement = ' '.join(['Hello there ', name]) # join() scales better
    # print(statement)
    

