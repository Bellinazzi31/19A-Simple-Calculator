def divideNumbers(userOne, userTwo):
    try:
        answer = userOne / userTwo
        print("User Result: " + str(answer))
    except ZeroDivisionError:
        print("You cant divide by zero!")  
