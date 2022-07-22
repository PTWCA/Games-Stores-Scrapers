from bs4 import BeautifulSoup
from utilities import print_database, URL_validation
from steamparser import get_steam_data
from Lokma.microsoft import microsoft
from Lokma.itch import itch
from ubisoft_scraper import get_ubisoft_data

while True:
    url = input("Enter a URL: ")
    if not url or url.lower() == 'exit':
        print_database()
        break

    if 'itch.io' in url:
        response = URL_validation(url, 'itch.io')
        soup = BeautifulSoup(response.text, 'html.parser')
        print(itch(response, soup), '\n')

    elif 'store.steampowered.com' in url:
        get_steam_data(url)

    elif 'xbox.com' in url:
        response = URL_validation(url, 'xbox.com')
        soup = BeautifulSoup(response.text, 'html.parser')
        print(microsoft(response, soup), '\n')

    elif "store.ubi.com" in url:
        print(get_ubisoft_data(url))

    else:
        print('Invalid URL')