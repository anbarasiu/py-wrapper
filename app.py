from flask import Flask
from flask_cors import CORS, cross_origin
import xmltodict
import json

app = Flask(__name__)
CORS(app)

def convert(xml_file, xml_attribs=True):
    with open(xml_file, "rb") as f:
        d = xmltodict.parse(f, xml_attribs=xml_attribs)
        return json.dumps(d)

@app.route('/v1/books/')
def hello():
    return convert("mock.xml")

if __name__ == "__main__":
    app.run(debug=True)
