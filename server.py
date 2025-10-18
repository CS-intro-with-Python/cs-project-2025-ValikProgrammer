from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, world!"})

@app.route('/user/<username>', methods=['GET'])
def user(username):
    return jsonify({"message": f"Hello, {username}!"})

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '') 
    return jsonify({
        "query": query,
        "length": len(query)
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
