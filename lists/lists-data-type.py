# spam = ['cat', 'bat', 'rat', 'elephant']
# # slice returns a list
# print(spam[1:3])

# change a list value
spam = [10, 20, 30]
spam[1] = 'Hello'
print(spam)

spam[1:3] = ['Cat', 'Dog', 'Mouse']
print(spam)

# To delete items at index
del spam[2]
print(spam)

print(len(spam))

print([1, 2, 3] + [4, 5, 6])
print([1, 2, 3] * 3)

someString = 'abcdef'
print(list(someString))