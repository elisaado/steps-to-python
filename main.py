# This file is part of elisaado/steps-to-python, licensed under the BSD 3-Clause License, if you have not got a copy of 
# that license with this software, you can find it here: 
# https://raw.githubusercontent.com/elisaado/steps-to-python/master/LICENSE

from glob import glob
from re import sub
from flask import Flask

app = Flask(__name__)
# app.run(debug=True)

# My own markup language's parser
def guideParser(path):
  with open(path, "r") as f:
    content = f.read() 

  name = path.split("/")[1:][0]
  title = content.split("#t")[1].split("\n")[1]
  by = content.split("#b")[1].split("\n")[1]

  # now comes the real stuff :v
  needed_raws = "".join(content.split("#n")[1:]).split("\n")
  needed = []

  for needed_raw in needed_raws[1:]:
    if len(needed_raw) <= 0:
      continue
    elif needed_raw[0] != "*":
      break
    elif needed_raw[1] == " ":
      needed.append(needed_raw[2:])
    else:
      needed.append(needed_raw[1:])

  steps_raw = "".join(content.split("#s")[1:]).split("\n")[1:]
  steps = []
  for step_raw in steps_raw:
    steps.append(sub(r'(\d+)\. ', '', step_raw, 1))

  return {"name": name, "title": title, "by": by, "needed": needed, "steps": steps}

guides = []
guides_paths = glob("guides/*")

for guide_path in guides_paths:
  guides.append(guideParser(guide_path))

@app.route("/")
def index():
  return str(guides)

# @app.route("")