import os

import replicate
from flask import Flask, request

app = Flask(__name__)
os.environ.get("REPLICATE_API_TOKEN")

@app.route('/')
def index():
    return '<h3> enter image url </h3> <form method="POST"><input name="text"><input type="submit"></form>'

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text
    return '<a href=' '/generate?imageUrl=' + processed_text + '>Generate Alt Text</a>'

@app.route('/generate')
def home():
  # Get imageUrl query param
  args = request.args
  imageUrl = args.to_dict().get('imageUrl')

  # Run ML Model with imageUrl
  model = replicate.models.get("salesforce/blip")
  version = model.versions.get("2e1dddc8621f72155f24cf2e0adbde548458d3cab9f00c0139eea840d0ac4746")

  # Get the alt text result and return it
  return version.predict(image=imageUrl)
