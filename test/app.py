from flask import Flask


app_instance = Flask(__name__)


@app_instance.route("/")
def index():
    return "<h1> Hello, World!</h1>"

from .hello import *

if __name__ == "__main__":
    app_instance.run()