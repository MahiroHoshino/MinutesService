from flask import Flask, render_template, request, json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/post", methods=["GET", "POST"])
def post():
  if request.method == "POST":
    name = request.form['name']
    text = request.form['text']
    time = request.form['time']
    file = open('test.txt', 'a')
    file.write(name + "," + text + "," + time + "\n")
    return ""

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)