from flask import Flask, render_template, json, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base

from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///d:\\Shagane\\Makeup_items.db'
db = SQLAlchemy(app)

# Makeup_items = db.Table('Makeup_items', db.metadata, autoload=True, autoload_with=db.engine)
# db.session.query(Makeup_items).all()   нужно дописать в функции которой нужно вызвать базу данных
# этот код позволяет связать существующую БД, но не позволяет ее изменять

Base = automap_base()
Base.prepare(db.engine, reflect=True)
mydb = Base.classes.Makeup_items

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/tint')
def showTints():
    all_items = db.session.query(mydb).all()
    brands = {item.Brand for item in all_items}
    brands = sorted(brands)
    return render_template('tint.html', all_items=all_items, brands=brands)

@app.route('/tint_sorted', methods=["POST"])
def sorted_by_brand():
    all_items = db.session.query(mydb).all()
    try:
        json_data = request.get_json()
    except Exception as e:
        return jsonify(result="bad data")

    print(json_data, type(json_data))
       
    items_sorted = []
    if json_data: 
        for brand in json_data:
            items_sorted.extend(db.session.query(mydb).filter(mydb.Brand == brand).all())
    
    else:
        items_sorted = all_items

    
    def make_norm_dict(inDct):
        dct = {}
        dct["Brand"] = inDct.Brand
        dct["Price"] = inDct.Price
        dct["Product_name"] = inDct.Product_name
        return dct

    return jsonify(list(map(make_norm_dict, items_sorted)))

# @app.route('/tint_sorted')
# def sorted_by_brand(brands):
#     return render_template('tint_sorted.html', all_items=all_items)
