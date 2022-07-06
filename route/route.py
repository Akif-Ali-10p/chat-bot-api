from flask import Blueprint, request,jsonify ,make_response
from action.action import * 
from arms.arms import *
import jwt
import datetime
from decorator.decorator import token_required
from constant.constant import SECRET_KEY


api=Blueprint('api',__name__)
# api.config['SECRET_KEY']='ThisisSecretKey'

@api.route("/sha")
def hello_world():
  return "Hello, World!"


@api.route('/welcome', methods=['GET'])
def get_welcome_message():
  return {"data": "Welcome to MobileOnline.com"}

@api.route("/armstrong/<int:n>", methods=['GET'])
def get_armstrong(n):
  result = arm(n)
  return result

@api.route('/conversation', methods=['POST'])
def chat_conversation():
  response_message = ""
  user_input = request.json['user_input']
  return actions_conversation(user_input)


@api.route('/unprotected', methods=['GET'])
def unprotected():
    return jsonify({'message':'anyone can view this'})


@api.route('/protected',methods=['GET'])
@token_required
def protected():
    return jsonify({'message':'Only avvailable to people with valid token'})


@api.route('/login', methods=['POST'])
def login():
    response_message = ""
    user_input_id = request.json['user_input_id']
    user_input_pass = request.json['user_input_pass']

    if user_input_pass=='newpass' and user_input_id=="id":
        token=jwt.encode({'user':user_input_id,'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=5)},SECRET_KEY)
        return jsonify({'token':token.encode("windows-1252").decode("utf-8")})
    return make_response({"message":'could not verify! login credentials'}, 401)    

  