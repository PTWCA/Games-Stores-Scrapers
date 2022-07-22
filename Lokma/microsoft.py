from DatabaseHandler import insert_data ; from utilities import clean_price

def get_price(soup):
	price = soup.find('span',class_='Price-module__srOnly___2mBg_')
	if price:
		if price.text == 'Free':
			price = 0.00
			return price
		if 'sale' in price.text:
			tags = soup.find_all('div',class_='typography-module__xdsCaption___2Ut3x ProductTags-module__tagItem___36qAO')
			for tag in tags:
				if 'sale' in tag.text:
					sale = clean_price(tag.text)
					break
			original_price = float(soup.find('span',class_='Price-module__originalPrice___1zgYT Price-module__strikeThrough___WaylD').text[1:])
			price = round(original_price - sale, 2)
		elif price:
			price = clean_price(price.text)
		else:
			price = 'N/A'
	else:
		price = 'N/A'
	return price

def get_author(soup):
	author = soup.find('div',class_='typography-module__xdsSubTitle1___2twuH ProductDetailsHeader-module__productInfoLine___2pgrC')
	if author:
		author = author.text.split(' • ')[0]
	else:
		author = 'N/A'
	return author

def get_name(soup):
	name = soup.find('h1',class_='typography-module__xdsH1___zrXla ProductDetailsHeader-module__productTitle___l-kbD')
	if name:
		name = name.text
	else:
		name = 'N/A'
	return name


def microsoft(response,soup):
	url = response.url
	price = get_price(soup)
	author = get_author(soup)
	game_name = get_name(soup)
	data = [game_name,price,url,author,'Microsoft']
	if 'N/A' in data:
		return 'Error: missing info, or invalid game url'
	insert_data(data)
	return 'Done'