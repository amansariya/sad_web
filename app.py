# app.py
from flask import Flask, render_template, request, Markup, jsonify
from datetime import datetime, timedelta

ist = timedelta(hours=5, minutes=30)

scene = "No Set Scene"
scene_id = 0
log = ""
req_log = ""
app = Flask(__name__)

def add_log(msg):
    global log
    global ist
    # datetime object containing current date and time
    now = datetime.now()
    now = now+ist

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S IST")

    log = log + str("<br>"+dt_string+": "+msg)

def add_req(page,req_h,req_args=None, req_form=None, req_json=None):
    global req_log
    global ist
    # datetime object containing current date and time
    now = datetime.now()
    now = now+ist

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S IST")
    req_log = req_log + str("<br>"+dt_string+" @"+page)
    if req_h!=None:
        req_log = req_log + str("<br>header: "+str(req_h))
    if req_args!=None:
        req_log = req_log + str("<br>args: "+str(req_args))
    if req_form!=None:
        req_log = req_log + str("<br>form: "+str(req_form))
    if req_json!=None:
        req_log = req_log + str("<br>form: "+str(req_json))
    req_log = req_log + "<br>"

# home route
@app.route("/", methods=['GET','POST'])
def home():
    global scene
    # scene = str(request.form)
    # add_req('/',str(request.headers),str(request.args),str(request.form),str(request.json))
    if request.form.get("submit_1"):
        scene = "Scene 1"
        scene_id = 0
        add_log("Changed to Scene 1")
    elif request.form.get("submit_1a"):
        scene = "Scene 1A"
        scene_id = 1
        add_log("Changed to Scene 1A")
    elif request.form.get("submit_1b"):
        scene = "Scene 1B"
        scene_id = 2
        add_log("Changed to Scene 1B")
    elif request.form.get("submit_1a_1"):
        scene = "Scene 1A_1"
        scene_id = 3
        add_log("Changed to Scene 1A_1")
    elif request.form.get("submit_1a_2"):
        scene = "Scene 1A_2"
        scene_id = 4
        add_log("Changed to Scene 1A_2")
    elif request.form.get("submit_1b_1"):
        scene = "Scene 1B_1"
        scene_id = 5
        add_log("Changed to Scene 1B_1")
    elif request.form.get("submit_1b_2"):
        scene = "Scene 1B_2"
        scene_id = 6
        add_log("Changed to Scene 1B_2")
    elif request.form.get("submit_clear"):
        scene = "No Set Scene"
        add_log("Reset scene to blank")
        scene_id = 0
    return render_template('index.html', scene_name=scene)

# log route
@app.route("/log", methods=['GET','POST'])
def log_page():
    global log
    add_req('/log',str(request.headers),str(request.args),str(request.form),str(request.json))
    log_output = Markup(log)
    return render_template('log.html', scene_name=scene, log_report=log_output)

# requests log route
@app.route("/req_log", methods=['GET','POST'])
def log_req():
    global req_log
    # add_req('/req_log',str(request.headers),str(request.args),str(request.form),str(request.json))
    log_output = Markup(req_log)
    return render_template('requests_log.html', scene_name=scene, log_report=log_output)

# requests log route
@app.route("/req_log", methods=['GET','POST'])
def req_point():
    global req_log
    add_req('/req_log',str(request.headers),str(request.args),str(request.form),str(request.json))
    log_output = Markup(req_log)
    return render_template('req_point.html')

# get-scene route
@app.route("/get-scene", methods=['GET','POST'])
def get_scene():
    return jsonify(scene_id=str(scene_id))

if __name__ == '__main__':
    app.run(debug=True)
