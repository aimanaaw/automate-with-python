# Parse information from web pages

import bs4, requests

# Amazon
# Walmart
response = requests.get('https://www.kijiji.ca/v-cars-trucks/city-of-toronto/2018-ford-f-150-xlt-4wd-supercrew-5-5-box/1496594814')
# print(res.status_code)
# print(res.raise_for_status())

# html.parser to specify the html parser for the data
soup = bs4.BeautifulSoup(response.text, "lxml")

selector = '#ViewItemPage > div:nth-child(5) > div.itemTitleWrapper-4111598823 > div.mainColumn-1522885425 > div > h1'
# print(soup)
elemsTest = soup.select(selector)
print(elemsTest[0].text)

