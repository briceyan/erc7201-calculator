from flask import Flask, render_template, request, make_response
from erc7201 import erc7201, format_solidity

app = Flask(__name__)


def is_browser(user_agent):
    """Check if the request comes from a browser"""
    browsers = ("mozilla", "chrome", "safari", "webkit", "opera", "msie")
    return user_agent and any(b in user_agent.lower() for b in browsers)


@app.route("/")
def index():
    if is_browser(request.user_agent.string):
        return render_template("index.html", host_url=request.host_url)
    return render_template("index.text")


@app.route("/<namespace>")
def calculate(namespace):
    slot = erc7201(namespace)
    solidity_code = format_solidity(namespace, slot)

    if is_browser(request.user_agent.string):
        return render_template(
            "result.html", namespace=namespace, slot=slot, solidity_code=solidity_code
        )

    return render_template("result.text", namespace=namespace, slot=slot, solidity_code=solidity_code)
