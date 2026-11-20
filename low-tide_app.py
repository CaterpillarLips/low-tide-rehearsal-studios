from flask import Flask, render_template, request

app = Flask(__name__, template_folder=".", static_folder=".", static_url_path="")
app.secret_key = "change-me-to-anything"

@app.route("/")
def shop():
    return render_template("index.html")

@app.route("/book")
def flask():
    rooms = ["Room1", "Room2", "Room3"]
    return render_template("flask.html", rooms=rooms)

@app.route("/about")
def bread():
    return "About us"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)