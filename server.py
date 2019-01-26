from logger import Logger 
from flask import Flask, render_template, request, make_response, Response, jsonify
import datetime
import json
import os
import shutil

logger = Logger().get_logger()
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/reset", methods=["POST"])
def reset():
    with open('static/json/text_data.json', 'w') as file:
        file.write("")
    shutil.rmtree("./static/download")
    os.mkdir("./static/download")
    os.defpath
    return ""


@app.route("/download/<file_name>", methods=["POST"])
def download(file_name):

    read = []

    file = open('static/json/text_data.json', 'r')
    file.seek(0, 2)
    if file.tell() == 0:
        file.close()
    else:
        file.seek(0)
        read = json.load(file)
        file.close()

    file = open('static/download/' + file_name + '.txt', 'a', encoding='utf-8')
    for list in read:
        file.write(list['name'] + ":" + list['text'] + "\n")
    file.close()
    open_file = open('static/download/' + file_name + '.txt', "rb").read()
    return open_file


@app.route("/interval", methods=["POST"])
def interval():
    file = open('static/json/text_data.json', 'r')
    file.seek(0, 2)
    if file.tell() == 0:
        file.close()
        return make_response(json.dumps([], ensure_ascii=False))
    else:
        file.seek(0)
        read = json.load(file)
        file.close()
        return make_response(json.dumps(read, ensure_ascii=False))

@app.route("/post", methods=["POST"])
def post():
    if request.method == "POST":
        name = request.form['name']
        text = request.form['text']

        year = int(request.form['year'])
        month = int(request.form['month'])
        day = int(request.form['day'])
        hour = int(request.form['hour'])
        minute = int(request.form['minute'])
        second = int(request.form['second'])
        millisecond = int(request.form['millisecond'])

        time = datetime.datetime(year, month, day, hour, minute, second, millisecond * 1000).strftime("%Y-%m-%d %H:%M:%S.%f")

        write_data = {
            'name' : "Nameless" if name == "" else name,
            'text' : text,
            'time' : time
        }

        with open('static/json/text_data.json', 'ab+') as f:
            f.seek(0, 2)
            if f.tell() == 0:
                f.write(json.dumps([write_data]).encode())
            else:
                f.seek(-1, 2)
                f.truncate()
                f.write(' , '.encode())
                f.write(json.dumps(write_data).encode())
                f.write(']'.encode())
        
        file = open('static/json/text_data.json', 'r')
        json_read = json.load(file)

        print(json_read)
        json_read = sorted(json_read, key=lambda x: x['time'])

        return make_response(json.dumps(json_read, ensure_ascii=False))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000, threaded=True)