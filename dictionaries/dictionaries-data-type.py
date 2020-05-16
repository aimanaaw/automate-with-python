import pprint

myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size'])

spam = {12344: 'luggage combination', 42: 'The Answer'}
# Items in dictionaries are unordered

print(spam.keys())

print(spam.values())

print(spam.items())


# multiple assignments
for k,v in spam.items():
	print(k, v)

# It looks for size key, if it does not find the key, it will return 'skinny'
print(myCat.get('size', 'skinny'))

myCat.setdefault('age', 8)
print(myCat)

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message.upper():
	count.setdefault(character, 0)
	count[character] += 1
pprint.pprint(count)
rjtext = pprint.pformat(count)
print(rjtext)