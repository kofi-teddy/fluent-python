# Combination and Permutation

import itertools

word = 'sample'
my_letters = 'plmeas'

combinations = itertools.combinations(my_letters, 6)
permutations = itertools.permutations(my_letters, 6)

for p in permutations:
    # print(p)  
    if ''.join(p) == word:
        print('Match!')
        break
else:
    print('No Match!')

# my_list = [1, 2, 3, 4, 5, 6]

# combinations = itertools.combinations(my_list, 3)
# permutations = itertools.permutations(my_list, 3)

# print([ result for result in combinations if sum(result) == 10])


# combinations = itertools.combinations(my_list, 2)
# for c in combinations:
#     print(c)


# permutations = itertools.permutations(my_list, 2)
# for p in permutations:
#     print(p)