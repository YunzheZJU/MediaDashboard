# -*- coding: utf-8 -*-
from flask import Flask, request, session, g, redirect, url_for, abort, render_template
from scan import scan_data
from PIL import Image

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    if request.method == "GET":
        return render_template('overview.html'), 200, {'Cache-Control': 'no-cache'}


@app.route('/a', methods=['GET'])
def a_side():
    if request.method == "GET":
        song_list = scan_data("a", 100)
        return render_template('detail.html', song_list=song_list, active='a'), 200, {'Cache-Control': 'no-cache'}


@app.route('/b', methods=['GET'])
def b_side():
    if request.method == "GET":
        song_list = scan_data("b", 100)
        return render_template('detail.html', song_list=song_list, active='b'), 200, {'Cache-Control': 'no-cache'}


@app.route('/convertImage', methods=['GET'])
def get_converted():
    type = request.args.get('type')
    order = request.args.get('order')
    origin = "images/" + type + "/" + "0" * (3 - len(str(order))) + order + ".jpg"
    new = "images/" + type + "/" + "0" * (3 - len(str(order))) + order + ".png"
    Image.open("static/" + origin).save("static/" + new)
    return url_for('static', filename=new)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
