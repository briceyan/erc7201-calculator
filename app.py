from flask import Flask, render_template, request, redirect, url_for
from erc7201 import erc7201, format_solidity

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<namespace>')
def calculate(namespace):
    slot = erc7201(namespace)
    solidity_code = format_solidity(namespace, slot)
    return render_template('result.html', 
                         namespace=namespace,
                         slot=slot,
                         solidity_code=solidity_code)

@app.route('/submit', methods=['POST'])
def submit():
    namespace = request.form['namespace']
    return redirect(url_for('calculate', namespace=namespace))
