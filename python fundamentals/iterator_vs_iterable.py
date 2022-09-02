# iterable: a thing we can iterate over
# iterator: a special object with next() method

import itertools


x = [1, 2, 3, 4] # list is iterable but not iterator

# for i in x:  # iterable
#     print(i)

# print(next(x)) # not iterator TypeError: 'list' object is not an iterator

it = itertools.cycle(x) # it is iterator ... also iterable
# print(next(it))

# for i in it: infinite iterable
#     print(i)

y = iter(x) # transform iterable to iterator 'y' is iterator ... also iterable
for i in y:
    print(i)
