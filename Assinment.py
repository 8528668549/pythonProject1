from itertools import permutations
list1 = [1, 2, 3, 4]
seq = permutations(list1)
print(seq)
for p in list(seq):
    print(p)

from itertools import permutations
list2 = [1, 2, 3, 4, 5]
seq = permutations(list2)
print(seq)
for p in list(seq):
    print(p)

