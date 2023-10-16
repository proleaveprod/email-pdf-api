# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for
from form_settings import *
import post_example

app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template("index.html")

# # Запуск flask
# if __name__ == "__main__":
#     app.run(debug=True)

post_text = post_example.post_example

author = post_text[AUTHOR_NAME]







