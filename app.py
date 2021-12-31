import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def query_records():
    return jsonify({'name': 'alice',
                    'email': 'alice@outlook.com'})

app.run()

if __name__ == "__main__":
    app.run(ssl_context=('./cert/cert.pem', './cert/key.pem'))