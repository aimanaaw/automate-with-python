import re

namesRegex = re.compile(r'Agent \w+')
mo1 = namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')
print(mo1)

# The sub method replaces the words with a specified word
mo2 = namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo2)

namesRegex2 = re.compile(r'Agent (\w)\w*')
mo3 = namesRegex2.findall('Agent Alice gave the secret documents to Agent Bob.')
print(mo3)

# Match and replace a specific word. Specify the group. In this case group 1
mo4 = namesRegex2.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo4)

# Verbose Method /////
re.compile(r'''
	(\d\d\d-) | #area code
	(\(\d\d\d))
	\d\d\d\ #first dash
	-		#second dash
	\d\d\d\d
	\sx\d{2,4} #last 4 digits''', re.VERBOSE | re.DOTALL | re.IGNORECASE)