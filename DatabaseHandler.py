import sqlite3
def insert_data(list):
  
  connection_obj = sqlite3.connect('games.db')
  cursor_obj = connection_obj.cursor()
  
  sqlite_insert_query = f"""INSERT INTO GAMES
                        (Game_name, PRICE, URL, Developer_name, provider) 
                        VALUES 
                          (?,?,?,?,?);"""
  
  cursor_obj.execute(sqlite_insert_query, tuple(list))
  connection_obj.commit()
  connection_obj.close()