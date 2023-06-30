from flask import Flask, request
import werkzeug
#from flask_frozen import Freezer

app=Flask(__name__)
#freezer=Freezer(app)

@app.route('/')
def index():
    return "Hello from flask"

@app.route('/tst')
def tst():
    try:
        cmd=request.args['cmd'].split()
    except werkzeug.exceptions.BadRequestKeyError:
        return "Hello This is a test page"
    import subprocess
    out=(subprocess.check_output(cmd)).decode('utf-8')
    return f"cmd was : {' '.join(cmd)} <br> output is:<br> {out}"

if __name__=="__main__":
    app.run(debug="True")
    #freeze.run()
