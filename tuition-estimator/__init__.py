from flask import request, Flask, render_template, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name=None):
    url_for('static', filename='style.css')
    return render_template("hello.html", person=name)

