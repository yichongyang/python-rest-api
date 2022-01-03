import json
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/users')
def query_records():
    with open('./data/records', 'r') as f:
        data = f.read()
        records = json.loads(data)
        return jsonify(records)
        
 
@app.route('/user', methods=['GET'])
def get_record_query():
    name = request.args.get('name')
    with open('./data/records', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for record in records:
            if record['name'] == name:
                return jsonify(record)
        return jsonify({'error': 'data not found'})


@app.route('/user/<name>')
def get_record_path(name):
    with open('./data/records', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for record in records:
            if record['name'] == name:
                return jsonify(record)
        return jsonify({'error': 'data not found'})


@app.route('/user', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    new_records = []
    with open('./data/records', 'r') as f:
        data = f.read()
        records = json.loads(data)
    for r in records:
        if r['name'] == record['name']:
            r['email'] = record['email']
        new_records.append(r)

    new_records.append(record)
    with open('./data/records', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)


@app.route('/user', methods=['DELETE'])
def delte_record_query():
    record = json.loads(request.data)
    result = record['name'] + ' not found'
    new_records = []
    with open('./data/records', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['name'] == record['name']:
                result = 'Record for ' + record['name'] + ' deleted'
                print(result)
                continue
            new_records.append(r)
    with open('./data/records', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(result)


@app.route('/user/<name>', methods=['DELETE'])
def delete_record_path(name):
    new_records = []
    result = 'Record ' + name + ' not found'
    with open('./data/records', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['name'] == name:
                result = 'Record for ' + name + ' deleted'
                print(result)
                continue
            new_records.append(r)
    with open('./data/records', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(result)

#app.run()


if __name__ == "__main__":
    app.config['DEBUG'] = True
    app.run(ssl_context=('./cert/cert.pem', './cert/key.pem'), host='0.0.0.0', port=5443)