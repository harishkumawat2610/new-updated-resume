from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def home():
    rows_no=len(yt_list)
    return render_template("index.html")


if __name__ == '__main__':
    app.run(threaded=True, debug=True, port=5000)
