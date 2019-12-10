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
        self.cursor = create_db()
        def create_db():
            mydb = sqlite3.connect('{}.db'.format(self.name))
            cursor = mydb.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS {}
                            (articul, brand, pn, p_price, p_original_price)
                            '''.format(self.name))
            return cursor
    
    def push_item(self):
        self.cursor.execute("""INSERT INTO {} VALUES
                    (?, ?, ?, ?, ?)
                    """.format(self.name), self.items)
              
def main():
    html_text = get_data()
    items = parse_items_intext(html_text)
    db_name = 'Makeup_items'
    make_up_db = DataBase(db_name, items)
    make_up_db.push_item()

        
if __name__ == "__main__":
    main()


# with open(r'd:\Shagane\FirstProject\test.html', 'w') as output_file:
#     output_file.write()




