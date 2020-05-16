def eggs(someParameter):
	someParameter.append('Hello')


spam = [1, 2, 3]
eggs(spam)
print(spam)

import copy

# deepcopy makes a total copy instead of just a reference

spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
cheese[1] = 42

print(spam)
print(cheese)