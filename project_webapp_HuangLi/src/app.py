"""
Simple "Hello, World" application using Flask
"""
from flask import Flask, render_template, request

from mbta_helper import *

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/station/', methods =['GET', 'POST'])
def nearest():
    if request.method =='POST':
        location = str(request.form['location'])
        if type (find_stop_near(location)) != tuple:
            return render_template("error.html", error= None)
        else: 
            busstop,distance = find_stop_near(location)
        # if busstop == "No stops nearby":
        #     return render_template('location_result.html')
            return render_template("location_result.html", location=location, busstop=busstop, distance = distance)
    return render_template("location_form.html", error=None)



if __name__ == '__main__':
    app.run()
