from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    with open('tasks-hard-collection.europlan.ru-20230505T091738-040.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    results = [item for item in data if query.lower() in item['name'].lower()]
    return jsonify(results)



@app.route('/statistics', methods=['GET'])
def statistics():
    with open('tasks-hard-collection.europlan.ru-20230505T091738-040.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    unique_inn = set()
    contract_count = 0
    total_delay_sum = 0

    for item in data:
        unique_inn.add(item["inn"])
        for contract in item["contractInfo"]:
            contract_count += 1
            total_delay_sum += contract["paymentDelaySumNdsInContractCurrency"]

    return jsonify({
        "unique_inn_count": len(unique_inn),
        "contract_count": contract_count,
        "total_delay_sum": total_delay_sum
    })

if __name__ == '__main__':
    app.run(debug=True)