from flask import Flask
import xmltodict
import json

app = Flask(__name__)

def convert(xml_file, xml_attribs=True):
    with open(xml_file, "rb") as f:
        d = xmltodict.parse(f, xml_attribs=xml_attribs)
        return json.dumps(d, indent=4)

@app.route('/')
def hello():
    return convert("mock.xml")

if __name__ == "__main__":
    app.run(debug=True)
