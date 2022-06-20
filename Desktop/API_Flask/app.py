from urllib.parse import uses_netloc
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)

# Product Class/Model
class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
  description = db.Column(db.String(200))
  price = db.Column(db.Float)
  qty = db.Column(db.Integer)

  def __init__(self, name, description, price, qty):
    self.name = name
    self.description = description
    self.price = price
    self.qty = qty

# Product Schema
class ProductSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'description', 'price', 'qty')

# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


@app.route('/product', methods=['POST'])
def add_product():
  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  qty = request.json['qty']

  new_product = Product(name, description, price, qty)

  db.session.add(new_product)
  db.session.commit()

  return product_schema.jsonify(new_product)


@app.route('/product', methods=['GET'])
def get_products():
  all_products = Product.query.all()
  return products_schema.jsonify(all_products)


@app.route('/product/<id>', methods=['GET'])
def get_product(id):
  product = Product.query.get(id)
  return product_schema.jsonify(product)


@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
  product = Product.query.get(id)

  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  qty = request.json['qty']

  product.name = name
  product.description = description
  product.price = price
  product.qty = qty

  db.session.commit()

  return product_schema.jsonify(product)


@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
  product = Product.query.get(id)
  db.session.delete(product)
  db.session.commit()

  return product_schema.jsonify(product)


@app.route('/welcome', methods=['GET'])
def get_welcome_message():
  return {"data": "Welcome to MobileOnline.com"}

@app.route('/conversation', methods=['POST'])
def chat_conversation():
  response_message = ""
  user_input = request.json['user_input']
  user_input=user_input.lower()
  
  # user_Model =request.json['user_Model']
  

  # user_price = request.json['user_price']
  

  if user_input == "hi" or user_input == "hello":
    response_message = "How can we help you ?"
  elif user_input == "want to buy mobile" or user_input == "buy mobile" or user_input == "purchase mobile":
    response_message = "Which brand you want ?"
  elif user_input == "nokia" or user_input == "Mi":
    response_message = "which model?"
  elif user_input == "nk1200":
    response_message = "This model is out of stock"
  elif user_input == "nk6300":
    response_message = "This is in stock"
  elif user_input == "What is price ?" or user_input == "price":
    response_message = "Its Price is 65000"
  else:
    response_message = "invalid input"
  print(user_input)

  return { "data": response_message }
  


# Run Server
if __name__ == '__main__':
  app.run(debug=True)