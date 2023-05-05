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

if __name__ == '__main__':
    app.run(debug=True)
