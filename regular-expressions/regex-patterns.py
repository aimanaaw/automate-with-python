import re

batRegex = re.compile(r'Bat(wo)?man')

mo = batRegex.search('The adventures of Batman')
print(mo.group())

# ? means match 0 or 1 times
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneMO = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow')
# print(phoneMO.group())

phoneRegexOptional = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
phoneMO1 = phoneRegexOptional.search('My phone number is 415-555-1234. Call me tomorrow')
phoneMO2 = phoneRegexOptional.search('My phone number is 555-1234. Call me tomorrow')
# print(phoneMO1)
# print(phoneMO2)

# * means match 0 or more times
batRegex1 = re.compile(r'Bat(wo)*man')
mo1 = batRegex1.search('The adventures of Batwowowowowowowoman')
# print(mo1.group())

# + means match 1 or more times
batRegex3 = re.compile(r'Bat(wo)+man')
mo3 = batRegex3.search('The adventures of Batwoman')
print(mo3.group())

# {} mean match the exact number of times specified
haRegex = re.compile(r'(Ha){2}')
mo4 = haRegex.search('He said HaHaHa and HaHaHa')
# print(mo4.group())
# {x,y} matches between x and y number of groups
phoneRegex2 = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){1,2}')
mo5 = phoneRegex2.search('My numbers are 415-555-1234,555-4242,212-555-0000')
print(mo5)

# Greedy match tries to find the longest possible match
digitRegex = re.compile(r'(\d){3,5}')
mo6 = digitRegex.search('1234567890')
print(mo6)

# Non greedy match will find the quickest possible match
digitRegex2 = re.compile(r'(\d){3,5}?')
mo7 = digitRegex2.search('1234567890')
print(mo7)