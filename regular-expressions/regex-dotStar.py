import re
# ^ used to check for pattern in the beginning
beginsWithHelloRegex = re.compile(r'^Hello')
mo1 = beginsWithHelloRegex.search('Hello there!')
# print(mo1)

# Will not work
mo2 = beginsWithHelloRegex.search('Are you there? Hello!')
# print(mo2)

# $ at the end to check for pattern at the end
endsWithWorldRegex = re.compile(r'world!$')
mo3 = endsWithWorldRegex.search('Hello world!')
# print(mo3)

allDigitsRegex = re.compile(r'^\d+$')
mo4 = allDigitsRegex.search('235893458374503275')
# print(mo4)
mo5 = allDigitsRegex.search('23424524xdsdfsdfs')
# print(mo5)

# . the wildcard
atRegex1 = re.compile(r'.at')
mo6 = atRegex1.findall('The cat in the hat sat on the flat mat')
# print(mo6)

# . looks for any character except the newline
atRegex2 = re.compile(r'.{1,2}at')
mo7 = atRegex2.findall('The cat in the hat sat on the flat mat')
# print(mo7)

# .* means any pattern. It uses greedy mode. For non-greedy use .*?
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo8 = nameRegex.findall('First Name: Al Last Name: Sweigart')
print(mo8)

serve = '<To serve humans> a meal for dinner.>'
nonGreedy = re.compile(r'<(.*?)>')
mo9 = nonGreedy.findall(serve)
# print(mo9)


# Greedy match
greedy1 = re.compile(r'<(.*)>')
mo10 = greedy1.findall(serve)
# print(mo10)

prime = 'Serve the public trust. \nProtect the innocent. \nUpload the law'
# print(prime)
greedySpace = re.compile(r'.*')
mo11 = greedySpace.search(prime)
print(mo11)

# dot for every character
dotStar = re.compile(r'.*', re.DOTALL)
mo12 = dotStar.search(prime)
print(mo12)

# Match lower case and upper case
vowelRegex = re.compile(r'[aeiou]', re.I)
mo13 = vowelRegex.findall('Al, why does your programming book talk about Robocop so much?')
print(mo13)