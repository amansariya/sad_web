# app.py
from flask import Flask, render_template, request

scene = "No Set Scene"

app = Flask(__name__)
# home route
@app.route("/")
def intro():
    return render_template('index.html', scene_name=scene)

@app.route("/index", methods=['POST'])
def sim_on():
    global scene
    # scene = str(request.form)
    if request.form.get("submit_1"):
        scene = "Scene 1"
    elif request.form.get("submit_1a"):
        scene = "Scene 1A"
    elif request.form.get("submit_1b"):
        scene = "Scene 1B"
    elif request.form.get("submit_1a_1"):
        scene = "Scene 1A_1"
    elif request.form.get("submit_1a_2"):
        scene = "Scene 1A_2"
    elif request.form.get("submit_1b_1"):
        scene = "Scene 1B_1"
    elif request.form.get("submit_1b_2"):
        scene = "Scene 1B_2"
    elif request.form.get("submit_clear"):
        scene = "No Set Scene"
    return render_template('index.html', scene_name=scene)
app.run(debug = True)