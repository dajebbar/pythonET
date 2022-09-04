input_list = [5, 2, 3, 15, 10, 18, 20, 25, 7]

def div_by_five(x):
    if x % 5 == 0:
        return True
    else:
        return False
    
xyz = (i for i in input_list if div_by_five(i))
# [print(i) for i in xyz]
xyz = [i for i in input_list if div_by_five(i)]
print(xyz)