from flask import Flask, render_template
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
    return render_template('tint.html', all_items=all_items)

if __name__ == "__main__":
    app.run()