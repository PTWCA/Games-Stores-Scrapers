from DatabaseHandler import insert_data
from utilities import clean_price
from bs4 import BeautifulSoup
import requests 
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}



def get_steam_data(link):
  
  src = requests.get(link , headers = headers).content
  soup = BeautifulSoup(src,'lxml')
  # name
  Game_name = soup.find("div",{"class":"apphub_AppName"}).text
  # price 
  price = clean_price(soup.find("div",{"class":"discount_final_price"}).text)
  # url
  url = link.split('?')[0]
  # company name 
  developer = soup.find("div",{"class":"dev_row"}).find('a').text
  # data 
  insert_data([Game_name, price, url, developer, "Steam"])
