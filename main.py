# This file is part of elisaado/steps-to-python, licensed under the BSD 3-Clause License, if you have not got a copy of 
# that license with this software, you can find it here: 
# https://raw.githubusercontent.com/elisaado/steps-to-python/master/LICENSE

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
