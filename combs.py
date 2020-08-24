import itertools
import collections
a = [1,3,4]
b = [2,3,5]
c = [3,4,5]

# for i in collections.Counter(a).items():
#     print(i[1])
# for order, i in enumerate(itertools.product(*[a, b, c])):
#     print(order)
#     print(i)

list_of_domains = [[1,3,4], [2,3,5], [3,4,5]]
for i in itertools.product(*list_of_domains):
    print(i)