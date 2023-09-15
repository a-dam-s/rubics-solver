from flask import Flask, render_template, Response
from main import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('indexik.html')

@app.route('/solve/<scramble>', methods=['GET'])
def solve(scramble):
    solution = start_solve(scramble)
    if solution == -1:
        return Response(status=400, response={'error': 'Invalid scramble'})
    return Response(status=200, response={'solution': solution[0], 'time': solution[1]})