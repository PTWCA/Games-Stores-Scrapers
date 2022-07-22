from DatabaseHandler import insert_data ; from utilities import clean_price

def get_type(soup:str) -> str:
	if soup.find('strong',class_='bundle_price'):
		type = 'Bundle'
	elif soup.find('strong',class_='percent_off') or soup.find('div',class_='sale_label'):
		type = 'Sale'
	elif soup.find('h2',id='download'):
		type = 'Free'
	else:
		type = 'Normal'
	return type

def get_price(soup:str,type:str) -> float or str:
	if type == 'Normal':
		price = soup.find('span',{'itemprop':'price'})
		if price:
			price = clean_price(price.text)
		else:
			price = 'N/A'
	elif type == 'Sale':
		price = soup.find('button',class_='button buy_game_btn')
		if price:	
			price = clean_price(price.text)
		else:
			price = 'N/A'
	elif type == 'Bundle':
		price = soup.find('strong',class_='bundle_price')
		if price:
			price = clean_price(price.text)
		else:
			price = 'N/A'
	elif type == 'Free':
		price = 0
	else:
		price = 'N/A'
	return price

def get_author(soup:str,type:str) -> str:
	author = soup.find('span',class_ = 'on_follow') or soup.find('div',class_='promotion_host')
	if author:
		author = author.text
	else:
		return 'N/A'
	if type == 'Sale':
		author = author[17:]
	elif type == 'Bundle':
		if "bundle" in author:
			author = author[19:]
		else:
			author = author[17:]
	elif type == 'Normal' or type == 'Free':
		author = author[7:]
		author = author[:-6]
	return author

def get_name(soup:str)->str:
	game_name = soup.find('h1',class_='game_title') or soup.find('h1',class_='promotion_title')
	if game_name:
		return game_name.text
	else:
		return 'N/A'

	
def itch(response,soup):
	url = response.url
	type = get_type(soup)
	price = get_price(soup,type)
	author = get_author(soup,type)
	game_name = get_name(soup)
	
	data = [game_name,price,url,author,'itch.io']
	if 'N/A' in data:
		return 'Error: missing info, or invalid game url'
	insert_data(data)
	return 'Done'