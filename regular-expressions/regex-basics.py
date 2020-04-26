import re

message = 'Call me on my cellphone at 416-999-5176, or on my home phone at 647-888-1234, or 647-123-0002'

phoneNumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

matchObject = phoneNumber.search(message)
print(matchObject.group())

matchAll = phoneNumber.findall(message)
print(matchAll)