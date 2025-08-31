import os
from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv

load_dotenv() 

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("upload.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)