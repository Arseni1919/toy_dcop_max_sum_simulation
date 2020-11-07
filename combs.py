import itertools
import collections
a = [1,3,4]
b = [2,3,5]
c = [3,4,5]

import operator
stats = {'a':1000, 'b':3000, 'c': 100, 5: 500000}
print(max(stats.items(), key=operator.itemgetter(1))[0], max(stats.items(), key=operator.itemgetter(1))[1])
# for i in collections.Counter(a).items():
#     print(i[1])
# for order, i in enumerate(itertools.product(*[a, b, c])):
#     print(order)
#     print(i)

list_of_domains = [[10,30,40], [-2,-3,-5], [3,4,5]]
for i in itertools.product(*list_of_domains):
    print(i)

# ccc = None
# if ccc:
#     print('1')
# else:
#     print(2)
