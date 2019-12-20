import requests
import sqlite3
from bs4 import BeautifulSoup
import re

def get_data(i):
    url = u'https://iledebeaute.ru/shop/make-up/tint/page{}/?perpage=72'.format(i)
    r = requests.get(url)
    return r.text.encode('utf-8').decode('raw-unicode-escape')

def parse_items_intext(text):
    patterns = r'''\"articul\":\"(\w*)\",\"brand\":\"([^"]+)\",\"pn\":\"(.*?)\",\"p_price\":\"(\d+).00\",\"p_original_price\":\"(\d+).00\"'''
    items = re.findall(patterns, text)
    return items

def create_db(db_name):
    conn = sqlite3.connect('{}.db'.format(db_name))
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS {}".format(db_name))
    cursor.execute('''CREATE TABLE IF NOT EXISTS {}
                    (Articul ntext PRIMARY KEY NOT NULL, 
                    Brand ntext NOT NULL,
                    Product_name ntext NOT NULL, 
                    Price integer NOT NULL, 
                    Original_price integer NOT NULL)
                    '''.format(db_name))
    return conn
    
def insert_values(conn, db_name, items):
    cursor = conn.cursor()
    for item in items:
        cursor.execute('''INSERT INTO {} VALUES
                    (?, ?, ?, ?, ?)
                    '''.format(db_name), item)
    conn.commit()  
    return conn

def select_query(conn, db_name, atr):
    db = conn.cursor()
    db.execute("""SELECT * FROM {} WHERE Brand=?""".format(db_name), (atr,))
    return db.fetchall()
        
def main():
    db_name = 'Makeup_items'
    db = create_db(db_name)
    
    for i in range(1,6):
        html_text = get_data(i)
        items = parse_items_intext(html_text)
        db = insert_values(db, db_name, items)

    # art = 'Dior'
    # s = select_query(db, db_name, art)
    # create_db.close()  
       
if __name__ == "__main__":
    main()





