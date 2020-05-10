# Request module lets you download data from the web

import requests

res = requests.get('https://automatetheboringstuff.com/chapter11/')

print(res.status_code)
# print(res.text[:500])

# badRes = requests.get('https://automatetheboringstuff.com/vndfkjvndfkvnjdkfjvndv')
# print(badRes.raise_for_status())


playFile = open('RomeoAndJuliet.txt', 'wb')
# response object can be written to a file using a for loop. 100,000 bytes per iteration. 1 chunk in each iteration
for chunk in res.iter_content(100000):
	playFile.write(chunk)

playFile.close()