from bs4 import BeautifulSoup ; from requests import get, Session, exceptions ; import os


def url_validation(url:str):
	headers = {
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62",
		"Accept-Language": "en-US,en;q=0.9",
		"X-Amzn-Trace-Id": "Root=1-62d50e85-3b8e2dfc461c4cf5250c9dad",
		"referer": "https://www.google.com/",
		"DNT":'1'
	}
	while True:	
		try:
			response = Session().get(url, headers=headers)
			print(response.status_code)
			if int(response.status_code) < 300:
				break
			else:
				url = input('Error 2: Invalid URL, try again: ')
		except exceptions.MissingSchema:
			url = input('Error 1: Invalid URL, try again: ')
	return response

def get_type(soup:str)->str:
	type = soup.find('div',class_='css-u4p24i')
	if type:
		type = type.text
	return type
	
def get_name(soup:str)->str:
	name = soup.find('span',class_='css-inhi4e')
	if name:
		name = name.text
	return name

def get_price(soup:str)->float:
	price = soup.find('span',class_='css-z3vg5b') or soup.find('span',class_='css-1yqcr93')
	if price:
		price = price.text
	return price

def get_discount(soup:str)->int:
	discount = soup.find('div',class_='css-b0xoos')
	if discount:
		discount = int(discount.text) * -1
	return discount

def get_publisher(soup:str)->str:
	publisher = soup.find('span',class_='css-z3vg5b')
	if publisher:
		publisher = publisher.text
	return publisher

def get_release_date(soup:str)->str:
	release_date = soup.find('span',class_='css-z3vg5b')
	if release_date:
		release_date = release_date.text
	return release_date


	
wishlist = []
if not os.path.exists("Epic Updates.csv"):
	while True:
		url = input('Enter URL: ')
		if not url or url.lower() == 'exit':
			break
		else:
			response = url_validation(url)
			wishlist.append(url)

for url in wishlist:
	response = get(url)
	soup = BeautifulSoup(response.text,'html.parser')
	type = get_type(soup)
	name = get_name(soup)
	price = get_price(soup)
	discount = get_discount(soup)
	publisher = get_publisher(soup)
	release_date = get_release_date(soup)
	print()
	print(f'{name} by {publisher}')
	print(f'Price    = {price}')
	print(f'Discount = {discount}')
