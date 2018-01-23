from flask import Flask
from flask_cors import CORS, cross_origin
import xmltodict
import json
import requests

app = Flask(__name__)
CORS(app)
# undefined entity - from some chars in goodreads response
def convert(xml_file, xml_attribs=True):
    # with open(xml_file, "rb") as f:
    f = requests.get('https://www.goodreads.com/review/list/11879872.xml?key=key&v=2&id=anbarasiu&shelf=to-read&per_page=200')
    d = xmltodict.parse(f.text, xml_attribs=xml_attribs)
    return json.dumps(d['GoodreadsResponse']['reviews'])

@app.route('/v1/books/')
def hello():
    return convert("mock.xml")

if __name__ == "__main__":
    app.run(debug=True)
