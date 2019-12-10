import requests
import sqlite3
from bs4 import BeautifulSoup
import re

def get_data():
    url = u'https://iledebeaute.ru/shop/make-up/tint/'
    r = requests.get(url)
    return r.text.encode('utf-8').decode('raw-unicode-escape')

# def contain_items(text):
#     soup = BeautifulSoup(text)
#     item_list = soup.find()
#     return item_list is not None

def parse_items_intext(text):
    patterns = r'''\"articul\":\"(\w*)\",\"brand\":\"([^"]+)\",\"pn\":\"(.*?)\",\"p_price\":\"(\d+.00)\",\"p_original_price\":\"(\d+.00)\"'''
    items = re.findall(patterns, text)
    return items

class DataBase():

    def __init__(self, name, items):
        self.name = name
        self.items = items
        self.conn = sqlite3.connect('{}.db'.format(self.name))
        
    def create_db(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS {}
                        (articul text, 
                        brand text,
                        pn text, 
                        price text, 
                        original_price text)
                        '''.format(self.name))
        self.conn.commit
        return cursor.lastrowid
   
    def insert_item(self):
        cursor = self.conn.cursor()
        cursor.executemany("""INSERT INTO {} VALUES
                    (?, ?, ?, ?, ?)
                    """.format(self.name), self.items)
        self.conn.commit
        return cursor.lastrowid
        
              
def main():
    html_text = get_data()
    items = parse_items_intext(html_text)
    db_name = 'Makeup_items'
    make_up_db = DataBase(db_name, items)
    make_up_db.create_db()
    make_up_db.insert_item()

        
if __name__ == "__main__":
    main()





