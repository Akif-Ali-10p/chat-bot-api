def actions_conversation(user_input):
    user_input=user_input.lower()
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

