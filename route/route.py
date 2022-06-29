from flask import Blueprint, request
from action.action import * 
from arms.arms import *


api=Blueprint('api',__name__)

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
  user_input = request.json
  # return actions_conversation(user_input)
  return actions_decission(user_input)






    

  