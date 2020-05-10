import webbrowser, sys, pyperclip

sys.argv

# Check if command line arguments were passed
if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:])
else:
	address = pyperclip.paste()

print(sys.argv)
print(address)
webbrowser.open('https://automatetheboringstuff.com/' + address + '/')