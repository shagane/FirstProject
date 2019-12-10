import requests
import sqlite3
from bs4 import BeautifulSoup
import re

def get_data():
    url = u'https://iledebeaute.ru/shop/make-up/tint/'
    r = requests.get(url)
    return r.text.encode('utf-8').decode('raw-unicode-escape')

def parse_items_intext(text):
    patterns = r'''\"articul\":\"(\w*)\",\"brand\":\"([^"]+)\",\"pn\":\"(.*?)\",\"p_price\":\"(\d+.00)\",\"p_original_price\":\"(\d+.00)\"'''
    items = re.findall(patterns, text)
    return items

def conn(db_name):
    conn = sqlite3.connect('{}.db'.format(db_name))
    return conn

def create_db(conn, db_name):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS {}
                    (Articul text PRIMARY KEY, 
                    Brand text,
                    Product_name text, 
                    Price text, 
                    Original_price text)
                    '''.format(db_name))
    conn.commit
    cursor.lastrowid
    return conn
   
def insert_items(conn, db_name, items):
    for i in range(len(items)):
        conn.cursor().execute("""INSERT INTO {} VALUES
                    (?, ?, ?, ?, ?)
                    """.format(db_name), items[i])
        conn.commit
    return conn

def select_query(conn, db_name, atr):
    select_query = """SELECT * FROM {} WHERE Articul=?""".format(db_name)
    conn.cursor().execute(select_query, atr)
    select = conn.cursor().fetchall
    return select
        
def main():
    html_text = get_data()
    items = parse_items_intext(html_text)
    db_name = 'Makeup_items'
    db_connection = conn(db_name)
    dbcreated = create_db(db_connection, db_name)
    insert_items(dbcreated, db_name, items)
   

        
if __name__ == "__main__":
    main()





