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

def parse_items_intext(text):
    patterns = [r'"articul":"\w*"', r'"brand":"[^"]+"', r'"pn":"[^"]+"', r'"p_price":"\d+.00"', r'"p_original_price":"\d+.00"']
    items = []
    for pattern in patterns:
        item = re.findall(pattern, text)
        item = re.sub(r'("\w+":")'r'([^"]+)'r'(")', r'\2', str(item))
        items.append(item)
    return items


# class DataBase():
#     def __init__(self, name, articul, brand, prod_name, price, original_price):
#         self.name = name
#         self.values = values

#     def create_db(self):
#         mydb = sqlite3.connect('make-up_items.db')
#         cursor = mydb.cursor()
#         cursor.execute('''CREATE TABLE IF NOT EXISTS {}
#                         (articul, brand, pn, p_price, p_original_price)
#                         '''.format(self.name))
        
#     def push_item(articul, brand, pn, p_price, p_original_price, db_name, db=):     
#         db.execute("""INSERT INTO {} VALUES
#                         ({}, {}, {}, {}, {})
#                         """.format(db_name, articul, brand, pn, p_price, p_original_price))
        
        
def main():
    html_text = get_data()
    items = parse_items_intext(html_text)
    articul, brand, prod_name, price, original_price = [x for x in items]
    db_name = 'Makeup_items'
    make_up_db = create_db(db_name)
    

        
if __name__ == "__main__":
    main()


# with open(r'd:\Shagane\FirstProject\test.html', 'w') as output_file:
#     output_file.write()




