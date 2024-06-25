from flask import Flask, request, render_template
import qrcode

app = Flask(__name__)

@app.route("/")
def home():
    return(render_template("index.html"))

@app.route("/qr", methods = ["POST"])
def gen_qr():
    url = request.form["url"]
    image = qrcode.make(url)
    filename = "image.png"
    image.save("./static/" + filename)
    return(render_template("image.html", filename = filename))
