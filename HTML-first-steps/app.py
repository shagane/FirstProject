from flask import Flask, render_template, json, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///d:\\Shagane\\Makeup_items.db'
db = SQLAlchemy(app)

# Makeup_items = db.Table('Makeup_items', db.metadata, autoload=True, autoload_with=db.engine)
# db.session.query(Makeup_items).all()   нужно дописать в функции которой нужно вызвать базу данных
# этот код позволяет связать существующую БД, но не позволяет ее изменять

Base = automap_base()
Base.prepare(db.engine, reflect=True)
Makeup_items_class = Base.classes.Makeup_items

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/tint')
def showTints():
    all_items = db.session.query(Makeup_items_class).all()
    brands = {item.Brand for item in all_items}
    brands = sorted(brands)
    return render_template('tint.html', all_items=all_items, brands=brands)

@app.route('/tint_sorted', methods=["POST"])
def sorted_by_brand():
    try:
        json_data = request.get_json()
        retuslt = json_data['a'] + json_data['b']
        return jsonify(result=retuslt)
    except Exception as e:
        return jsonify(result="bad data")

# @app.route('/tint_sorted')
# def sorted_by_brand(brands):
#     return render_template('tint_sorted.html', all_items=all_items)


if __name__ == "__main__":
    app.run()