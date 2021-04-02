# app.py
from flask import Flask, render_template, request, Markup, jsonify
from datetime import datetime

scene = "No Set Scene"
log = ""
req_log = ""
app = Flask(__name__)

def add_log(msg):
    global log

    # datetime object containing current date and time
    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    log = log + str("<br>"+dt_string+": "+msg)

def add_req(page,req_h,req_args=None, req_form=None, req_json=None):
    global req_log
    # datetime object containing current date and time
    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
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
        add_log("Changed to Scene 1")
    elif request.form.get("submit_1a"):
        scene = "Scene 1A"
        add_log("Changed to Scene 1A")
    elif request.form.get("submit_1b"):
        scene = "Scene 1B"
        add_log("Changed to Scene 1B")
    elif request.form.get("submit_1a_1"):
        scene = "Scene 1A_1"
        add_log("Changed to Scene 1A_1")
    elif request.form.get("submit_1a_2"):
        scene = "Scene 1A_2"
        add_log("Changed to Scene 1A_2")
    elif request.form.get("submit_1b_1"):
        scene = "Scene 1B_1"
        add_log("Changed to Scene 1B_1")
    elif request.form.get("submit_1b_2"):
        scene = "Scene 1B_2"
        add_log("Changed to Scene 1B_2")
    elif request.form.get("submit_clear"):
        scene = "No Set Scene"
        add_log("Reset scene to blank")
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
@app.route("/req_point", methods=['GET','POST'])
def req_point():
    global req_log
    add_req('/req_point',str(request.headers),str(request.args),str(request.form),str(request.json))
    log_output = Markup(req_log)
    return render_template('req_point.html')

if __name__ == '__main__':
    app.run(debug=True)