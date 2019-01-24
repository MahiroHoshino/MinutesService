from flask import Flask, render_template, request, make_response
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/getminutes")
def get_minutes():
    dirList = os.listdir("./minutes")
    return render_template('getminutes.html', list=dirList)


@app.route('/download/<file_name>', methods=['GET'])
def download(file_name):
    response = make_response()
    response.data = open("./minutes/" + file_name, "rb").read()
    downloadFileName = file_name
    response.headers['Content-Disposition'] = 'attachment; filename=' + downloadFileName
    return response


@app.route("/post", methods=["GET", "POST"])
def post():
    if request.method == "POST":
        name = request.form['name']
        text = request.form['text']
        time = request.form['time']
        file = open('minutes/test.txt', 'a', encoding='utf-8')
        file.write(name + "," + text + "," + time + "\n")
        return ""


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000, threaded=True)
