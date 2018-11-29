from flask import Flask, flash, redirect, render_template, request, session, abort
from printinfo import SysInfo
import json

obj1 = SysInfo("gb")

app = Flask(__name__)


@app.route('/')
def index():
    var = json.loads(obj1.displayInfo())
    return render_template('index.html',**locals())

@app.route('/healthcheck')
def healthcheck():
    return "Ok"

@app.route("/api/cpu")
def cpu():
    var = json.loads(obj1.displayInfo())
    return str(var['payload']['CpuUsage'])

@app.route("/api/mem")
def mem():
    var = json.loads(obj1.displayInfo())
    return str(var['payload']['TotalMemory'])

@app.route("/api/disk")
def disk():
    var = json.loads(obj1.displayInfo())
    return str(var['payload']['DiskSize'])

@app.route("/api/all")
def all():
    return obj1.displayInfo()

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)

del obj1
