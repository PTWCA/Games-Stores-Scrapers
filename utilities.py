def clean_price(text: str):
	cleaned = ''
	for character in text:
		try:
			if int(character):
				cleaned += character
		except ValueError:
			if character == '.':
				cleaned += '.'
	cleaned = float(cleaned)
	return cleaned


def print_database():
  import sqlite3
  connection_obj = sqlite3.connect('games.db')
  cursor_obj = connection_obj.cursor()
  
  sqlite_insert_query = """select * from GAMES;"""
  
  cursor_obj.execute(sqlite_insert_query)
  rows = cursor_obj.fetchall()
  print(rows)
  connection_obj.commit()
  connection_obj.close()

from requests import get ; from requests.exceptions import MissingSchema
def URL_validation(url:str,store:str):
	while True:	
		try:
			response = get(url)
			if int(response.status_code) < 300 and store in url:
				break
			else:
				url = input('Error 2: Invalid URL, try again: ')
		except MissingSchema:
			url = input('Error 1: Invalid URL, try again: ')
	return response