import requests
import sqlite3
from bs4 import BeautifulSoup
import re

def get_data():
    url = r'https://iledebeaute.ru/shop/make-up/tint/'
    r = requests.get(url)
    return r.text

# def contain_items(text):
#     soup = BeautifulSoup(text)
#     item_list = soup.find()
#     return item_list is not None

# def read_file(file_name):
#     with open(file_name) as input_file:
#         text = input_file.read()
#     return text

def parse_items_from_shop(text):
    patterns = [r'"articul":"\w*"', r'"brand":"[^"]+"', r'"pn":"[^"]+"', r'"p_price":"\d+.00"', r'"p_original_price":"\d+.00"']
    items = []
    for pattern in patterns:
        item = re.findall(pattern, text)
        items.append(item)

    articul, brand, pn, p_price, p_original_price = [x for x in items]
    return articul, brand, pn, p_price, p_original_price

# def tag_separation(items):
#     for i in range(len(items)):
#         articul, brand, pn, p_price, p_original_price = items[i]
#     return articul, brand, pn, p_price, p_original_price

# def create_db(db_name):
#     mydb = sqlite3.connect('make-up_items.db')
#     cursor = mydb.cursor()
#     cursor.execute('''CREATE TABLE {}
#                         (articul, brand, pn, p_price, p_original_price)
#                         '''.format(db_name))
#     return mydb
    
# def push_item(articul, brand, pn, p_price, p_original_price, db=create_db):     
#     db.execute("""INSERT INTO {} VALUES
#                     ({}, {}, {}, {}, {})
#                     """.format(articul, brand, pn, p_price, p_original_price))
    

def main():
    html_text = get_data()
    items_list = parse_items_from_shop(html_text)
    # db_name = "Make-up items"
    
    # create_db(db_name)

if __name__ == "__main__":
    main()



# with open(r'd:\Shagane\FirstProject\test.html', 'w') as output_file:
#     output_file.write()




