import requests
import sqlite3
from bs4 import BeautifulSoup
import re

def get_data():
    url = u'https://iledebeaute.ru/shop/make-up/tint/'
    r = requests.get(url)
    return r.text.encode("utf-8").decode('unicode_escape')

# def contain_items(text):
#     soup = BeautifulSoup(text)
#     item_list = soup.find()
#     return item_list is not None

def parse_items_intext(text):
    patterns = [r'\"articul\":\"(\w*)\"', 
                r'\"brand\":\"([^"]+)\"', 
                r'\"pn\":\"(.*?)\"', 
                r'\"p_price\":\"(\d+.00)\"', 
                r'\"p_original_price\":\"(\d+.00)\"']
    items = []
    for pattern in patterns:
        item = re.findall(pattern, text)
        items.append(item)
    return items

class DataBase():
    def __init__(self, name, articul, brand, prod_name, price, original_price):
        self.name = name
        self.articul = articul
        self.brand = brand
        self.prod_name = prod_name
        self.price = price
        self.original_price = original_price

    @staticmethod
    def create_db(self):
        mydb = sqlite3.connect('make-up_items.db')
        cursor = mydb.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS {}
                        (articul, brand, pn, p_price, p_original_price)
                        '''.format(self.name))
        return cursor
        
    def push_item(self):
        for i in range(len(self.articul)):
            self.__class__.create_db(self).execute("""INSERT INTO {} VALUES
                        (?, ?, ?, ?, ?)
                        """.format(self.name), (self.articul[i], self.brand[i], self.prod_name[i], self.price[i], self.original_price[i]))
                
def main():
    html_text = get_data()
    items = parse_items_intext(html_text)
    articul, brand, prod_name, price, original_price = items
    db_name = 'Makeup_items'
    make_up_db = DataBase(db_name, articul, brand, prod_name, price, original_price)
    make_up_db.push_item()


        
if __name__ == "__main__":
    main()


# with open(r'd:\Shagane\FirstProject\test.html', 'w') as output_file:
#     output_file.write()




