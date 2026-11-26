from flask import Flask, render_template, request

app = Flask(__name__, template_folder=".", static_folder=".", static_url_path="")
app.secret_key = "change-me-to-anything"

@app.route("/")
def shop():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/account")
def account():
    return render_template("account.html")

@app.route("/booking")
def booking():
    rooms = ["Room1", "Room2", "Room3"]
    return render_template("booking.html", rooms=rooms)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)