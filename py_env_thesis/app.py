from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    itemm =[
        {"id": 111, "name": "item111"},
        {"id": 222, "name": "item222"}
    ]
    return jsonify(itemm)

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/items")
def get_items():
    items = [
        {"id": 1, "name": "item1"},
        {"id": 2, "name": "item2"}
    ]
    return jsonify(items)