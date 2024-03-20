from flask import Flask

app = Flask(__name__)

a=10
b=20
@app.route('/',methods=['GET'])
def welcome():
    return 'i can perform maths ops'

@app.route('/add',methods=['GET'])
def addition():
    return f"addition of {a} and {b} is {(a+b)}"

@app.route('/sub',methods=['GET'])
def substaction():
    return f"substraction of {a} and {b} is {a-b}"

@app.route('/mul',methods=['GET'])
def multiplication():
    return f"multiplication of {a} and {b} is {a*b}"

@app.route('/div',methods=['GET'])
def division():
    return f"division of {a} and {b} is {a//b}"

@app.route('/add/<a>/<b>',methods=['GET'])
def addition2(a,b):
    a=int(a)
    b=int(b)
    return f"addition of {a} and {b} is {a+b}"


@app.route('/sub/<a>/<b>',methods=['GET'])
def substarction2(a,b):
    a=int(a)
    b=int(b)
    return f"substraction of {a} and {b} is {a-b}"

@app.route('/mul/<a>/<b>',methods=['GET'])
def mutltiplication2(a,b):
    a=int(a)
    b=int(b)
    return f"substraction of {a} and {b} is {a*b}"

@app.route('/div/<a>/<b>',methods=['GET'])
def division2(a,b):
    a=int(a)
    b=int(b)
    return f"division of {a} and {b} is {a//b}"
app.run()