# FOR_NEXT_VERSION: use selenium to handle age-restricted games
# use vscode live share b3deen?
from bs4 import BeautifulSoup
from utilities import clean_price, URL_validation
from DatabaseHandler import insert_data

def get_ubisoft_data(link):
    req = URL_validation(link, "store.ubi.com")
    url = req.url
    soup = BeautifulSoup(req.content, "html.parser")
    tags = soup.find_all("li", class_="product-details-info-item")
    if not tags: 
        return "Error: missing info, or invalid url"
    for tag in tags:
        tag = tag.text.strip().split("\n")
        if tag[0] == "Developer:":
            developer = tag[1].strip()
            break
    price_wrapper = soup.find('div', class_='flex-reverse-order')
    if not price_wrapper:
        return "Error: missing info, or invalid url"
    price = price_wrapper.find("span", class_="price-sales standard-price")
    if price:
        price = price.text
        if price.strip() == '$0.00':
            price = 0.00
        else:
            price = clean_price(price)
    else:
        return "Error: missing info, or invalid url"
    name = soup.find("span",class_="breadcrumb-element breadcrumb-element-visible")
    if name:
        name = name.text.strip()
    else:
        return "Error: missing info, or invalid url"
    
    data = [name, price, url, developer, "Ubisoft"]
    insert_data(data)
    return "Done"

print(get_ubisoft_data(input("Enter URL: ")))