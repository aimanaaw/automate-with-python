import re

batRegex = re.compile(r'Bat(wo)?man')

mo = batRegex.search('The adventures of Batman')
print(mo.group())

# ? means match 0 or 1 times
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneMO = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow')
print(phoneMO.group())

phoneRegexOptional = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
phoneMO1 = phoneRegexOptional.search('My phone number is 415-555-1234. Call me tomorrow')
phoneMO2 = phoneRegexOptional.search('My phone number is 555-1234. Call me tomorrow')
print(phoneMO1)
print(phoneMO2)

# * means match 0 or more times
batRegex1 = re.compile(r'Bat(wo)*man')
mo1 = batRegex1.search('The adventures of Batwowowowowowowoman')
print(mo1.group())

# + means match 1 or more times
batRegex3 = re.compile(r'Bat(wo)+man')
mo3 = batRegex3.search('The adventures of Batwoman')
print(mo3.group())

# {} mean match the exact number of times specified
haRegex = re.compile(r'(Ha){3}')
mo4 = haRegex.search('He said HaHaHa')
print(mo4.group())