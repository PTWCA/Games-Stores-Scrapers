# CSV_FORMAT: name, price, url, release date, provider 
# TODO: Use Pandas
import csv
import logging
from tqdm import tqdm
from utlities import clean_price
# PS: when debugging uncomment all logging lines

# logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)
query = "FORD" # "Enter query, in this case it is a car make"

def read_csv(file_name: str):
    with open(file_name, "r") as data:
        readed_data = csv.reader(data)
        csv_file = []
        next(readed_data)
        for row in readed_data:
            csv_file.append(row)
    logging.info("CSV IS READY")
    return csv_file

    
# def clean_price(text: str):
#     cleaned = ""
#     for character in text:
#         try:
#             int(character)
#             cleaned += character
#         except ValueError:
#             continue
#     # logging.info("PRICE IS CLEANED")
#     return cleaned


def clean_csv(file: list):
    clean_file = []
    # logging.info("CLEANING CSV")
    for row in tqdm(file):
        cleaned_price = clean_price(row[1])
        clean_file.extend([[row[0], float(cleaned_price), row[2]]])
    # logging.info("CSV IS CLEANED")
    return clean_file


def search_query(clean_data: list, query: str):
    search_results = []
    for row in clean_data:
        if row[0].lower() == query.lower():
            search_results.append(row)

    logging.info("FOUND QUERY RESULTS")
    return search_results


def get_lowest(filtered_results: list):
    min = 10 * 100
    result_idx = 0
    for idx, result in enumerate(filtered_results):
        if result[1] < min:
            min = result[1]
            result_idx = idx

    logging.info("FILTERED QUERY RESULTS")
    return filtered_results[result_idx]


def main():
    data = read_csv("cars.csv")
    clean_data = clean_csv(data)
    search_results = search_query(clean_data, query)
    lowest_result = get_lowest(search_results)
    return lowest_result


if __name__ == "__main__":
	routine = main()
	print(routine)
