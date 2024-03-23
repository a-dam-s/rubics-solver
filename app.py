from flask import Flask, render_template, Response
from solver import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/solve/<scramble>', methods=['GET'])
def solve(scramble):
    solution = start_solve(scramble)
    if solution == -1:
        return Response(status=400, response='Invalid scramble')
    moves = list(solution[0].lower().replace(" ", "").replace("'", "p"))
    images = ""
    moves_copy = []
    for i in moves:
        if i in list("rludfb"):
            moves_copy.append(i)
        elif i == "2":
            moves_copy.append(moves_copy[-1])
        else:
            moves_copy[-1] += i
    for i in moves_copy:
        images += "<img src='/static/" + i + ".png'>"
    response_string = "<style>img{width:100px;height:100px;}</style><h3>Before applying the solution, apply those rotations:</h3><br><img src='/static/x.png'><img src='/static/x.png'><img src='/static/y.png'> <br> solution: " + \
        solution[0] + "<br>" + images + "<br> solve time: " + \
        str(solution[1]) + \
        "<br><a href='http://truet0123.eu.pythonanywhere.com'>Try again</a>"
    return Response(status=200, response=response_string)
