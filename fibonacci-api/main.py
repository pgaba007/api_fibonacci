from flask import Flask, request
app = Flask(__name__)

def fibonacci(order: int):
    if order == 1:
        return 1
    previous = 0
    current = 1
    for i in range(order-1):
        new = previous + current
        previous = current
        current = new
    return current

def recursive_fibonacci(order: int):
    if order < 1:
        return 0
    elif order == 1:
        return 1
    else:
        return(recursive_fibonacci(order-1)+recursive_fibonacci(order-2))

@app.route("/fibonacci")
def send_fibo():      #error handling
    try:
        return str(fibonacci(int(request.args['order'])))
    except ValueError:
        return "Please use a number for the order argument"

@app.route("/recursive_fibonacci")
def send_rec_fibo():
    try:
        return str(recursive_fibonacci(int(request.args['order'])))
    except ValueError:
        return "Please use a number for the order argument"
