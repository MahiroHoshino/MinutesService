from flask import Flask, render_template, request, make_response, Response, jsonify
import datetime
import json
import os

app = Flask(__name__)
text_list = []

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/reset", methods=["POST"])
def reset():
    text_list.clear()
    return ""


@app.route("/post", methods=["POST"])
def post():
    if request.method == "POST":
        global text_list
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

        file = open('minutes/test.txt', 'a', encoding='utf-8')
        file.write(name + "," + text + "," + time + "\n")

        text_list.append({
                'name' : name,
                'text' : text,
                'time' : time
        })
        text_list = sorted(text_list, key=lambda x: x['time'])

        return make_response(json.dumps(text_list, ensure_ascii=False))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000, threaded=True)