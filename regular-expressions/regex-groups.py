import re
# Groups in the string
phoneNum = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phoneNum.search('My number is 415-555-4242')

matchObject = phoneNum.search('My number is 415-555-4242')
print(matchObject.group())
print(matchObject.group(1))
print(matchObject.group(2))


phoneNum1 = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
matchObject1 = phoneNum1.search('My number is (415) 555-4242')
print(matchObject1.group())

# Pipe character
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel in a Batcity')
print(mo.group())
print(mo.group())