from collections import Counter

dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'b': 200, 'c': 500, 'd': 400}

the_sums = Counter(dict1) + Counter(dict2)
print(the_sums)

