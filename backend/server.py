from flask import Flask, jsonify, request
import json, os
app = Flask(__name__)

DATA_FILE = 'data/noticias.json'

@app.get('/api/noticias')
def get_noticias():
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return jsonify(json.load(f))

@app.post('/api/noticias')
def add_noticia():
    nueva = request.json
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    data.append(nueva)
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    return {"status": "ok"}

if __name__ == '__main__':
    app.run(debug=True)
