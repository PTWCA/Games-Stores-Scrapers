import csv
import pyshorteners
def read_csv(file_name):
	"""
	returns a list of all rows in a csv file given its name
	"""
	file = open(file_name, "r")
	reader = csv.reader(file)
	return list(reader)[1:]

def url_shortener(url:str):
	type_tiny = pyshorteners.Shortener()
	short_url = type_tiny.tinyurl.short(url)
	return short_url

	
def clean_price(text):
   cleaned = ""
   for character in text:
       try:
           int(character)
           cleaned += character
       except ValueError:
           continue
   cleaned = float(int(cleaned) / 100)
   return cleaned
#eyad is idle rn..will be back soon. salam,
# salam, ana momken arga3 tany 3la 6 am cairo time
# aw kman sa3a
# salam
# ezabi will be away when you come back, . salam
# 4bab e7tmal anzel, dlw2ty "url_shortener" di heya el shortening func, na2es bas n3ml loop over all urls in csv and shorten them..
# ha2fel el call we hab2a arga3 tany.
# tmam

"""
#[headers]
[aksj]
[alksj]
"""
def clean_file(file_name, new_file_name):
	rows = read_csv(file_name)
	file = open(new_file_name, "w")
	writer = csv.writer(file)
	for row in rows:
		row[2] = url_shortener(row[2])
		row[1] = clean_price(row[1])
		writer.writerow(row)


def get_dupes(query:str):
	duplicate_list = []
	csv_file = read_csv("cars.csv")
	for row in csv_file:
		if row[0].lower() == query.lower():
			duplicate_list.append([row[0], float(clean_price(row[1])), row[2]])

	return duplicate_list

def comp_dupes(duplicate_list:list):
	return min(duplicate_list, key = lambda x: x[1])

#print(get_dupes("TOYOTA"))
#dupes = get_dupes("TOYOTA")
#print()
#print(comp_dupes(dupes))

clean_file("cars.csv", "cleaned_cars.csv")
