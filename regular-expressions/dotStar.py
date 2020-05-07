import re
# ^ used to check for pattern in the beginning
beginsWithHelloRegex = re.compile(r'^Hello')
mo1 = beginsWithHelloRegex.search('Hello there!')
print(mo1)

# Will not work
mo2 = beginsWithHelloRegex.search('Are you there? Hello!')
print(mo2)

# $ at the end to check for pattern at the end
endsWithWorldRegex = re.compile(r'world!$')
mo3 = endsWithWorldRegex.search('Hello world!')
print(mo3)

allDigitsRegex = re.compile(r'^\d+$')
mo4 = allDigitsRegex.search('235893458374503275')
print(mo4)
mo5 = allDigitsRegex.search('23424524xdsdfsdfs')
print(mo5)