import bs4, requests

def getPrice(productUrl):
	res = requests.get(productUrl)
	# print(res.status_code())
	# print(response.raise_for_status())

	soup = bs4.BeautifulSoup(res.text, "lxml")
	elements = soup.select('#ViewItemPage > div:nth-child(5) > div.itemTitleWrapper-4111598823 > div.mainColumn-1522885425 > div > div > span > span:nth-child(1)')
	return elements[0].text.strip()


price = getPrice('https://www.kijiji.ca/v-cars-trucks/city-of-toronto/2018-ford-f-150-xlt-4wd-supercrew-5-5-box/1496594814')
print('The price is %s' % (price))