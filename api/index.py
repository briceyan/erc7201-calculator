from flask import Flask, render_template, request
from .erc7201 import erc7201, format_solidity

app = Flask(__name__, template_folder='templates')


@app.route("/")
def index():
    tmpl = (
        "index.html"
        if is_browser(request.user_agent.string)
        else "index.text"
    )
    return render_template(tmpl, host_url=request.host_url)


@app.route("/<namespace>")
def calculate(namespace):
    slot = erc7201(namespace)
    solidity_code = format_solidity(namespace, slot)
    tmpl = (
        "result.html"
        if is_browser(request.user_agent.string)
        else "result.text"
    )
    return render_template(
        tmpl, namespace=namespace, slot=slot, solidity_code=solidity_code
    )


def is_browser(user_agent):
    browsers = ("mozilla", "chrome", "safari", "webkit", "opera", "msie")
    return user_agent and any(b in user_agent.lower() for b in browsers)
