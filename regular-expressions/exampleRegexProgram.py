#! python3

import re, pyperclip

# TODO: Create a regex object for phone numbers

phoneRegex = re.compile(r'''
	# 415-555-0000, 555-0000, (415 555-0000, 555-000 ext 12345, ext. 12345, x12345)
	(((\d\d\d) | (\(\d\d\d\)))?	# area code (optional)
			(\s|-)	# first separator
			\d\d\d	# first 3 digits
			-	# separator
			\d\d\d\d	# last 4 digits
			(((ext(\.)?\s) | x)	# extension word-part (optional)
			(\d{2,5}))?		)	#extension number-part(optional)
	''', re.VERBOSE)

# TODO: Create a regex object for email address

emailRegex = re.compile(r'''
	# some.+_thing@(\d{2,5}))?.com
	[a-zA-Z0-9_.+]+	# name part. In between the character classes escape characters not required
	@ # @symbol
	[a-zA-Z0-9_.+]+ # domain name part
	''', re.VERBOSE)

# TODO: Get the text off the clipboard

text = pyperclip.paste()

# TODO: Extract the email/phone from this text

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
	allPhoneNumbers.append(phoneNumber[0])

print(allPhoneNumbers)



# TODO: Copy the extracted email/phone to the clipboard

results = '\n'.join(allPhoneNumbers) +'\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)


# Results after copying from file. Running this script. Then pasting below
939-537-1879
905-523-5311
975-675-8521
515-420-4722
mcbrid17@gmail.com
cohe1696@yahoo.com
hwalton3@hotmail.com
jacquesd@att.net