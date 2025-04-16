from flask import Flask, render_template, request, redirect, url_for, make_response
from erc7201 import erc7201, format_solidity

app = Flask(__name__)

def is_browser(user_agent):
    """Check if the request comes from a browser"""
    browsers = ('mozilla', 'chrome', 'safari', 'webkit', 'opera', 'msie')
    return user_agent and any(b in user_agent.lower() for b in browsers)

@app.route('/')
def index():
    if is_browser(request.user_agent.string):
        return render_template('index.html')
    return "ERC-7201 Namespace Calculator\n\nSend POST request to /submit with 'namespace' parameter or visit /<namespace>"

@app.route('/<namespace>')
def calculate(namespace):
    slot = erc7201(namespace)
    solidity_code = format_solidity(namespace, slot)
    
    if is_browser(request.user_agent.string):
        return render_template('result.html',
                            namespace=namespace,
                            slot=slot,
                            solidity_code=solidity_code)
    
    response = make_response(
        f"ERC-7201 Result for: {namespace}\n\n"
        f"Storage Slot: {slot}\n\n"
        f"Solidity Code:\n{solidity_code}"
    )
    response.headers['Content-Type'] = 'text/plain'
    return response

@app.route('/submit', methods=['POST'])
def submit():
    namespace = request.form['namespace']
    if is_browser(request.user_agent.string):
        return redirect(url_for('calculate', namespace=namespace))
    return calculate(namespace)
