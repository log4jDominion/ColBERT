import json

from flask import Flask, jsonify, request

import train_colbert

app = Flask(__name__)


def train():
    with open("updated_influencers.json", "r") as f:
        data = json.load(f)

    # Extract full names and descriptions
    full_names = [entry.get("full_name") for entry in data]
    descriptions = [entry.get("description") for entry in data]

    train_colbert.train_colbert(descriptions, full_names)

# Sample route
@app.route('/')
def home():
    return 'Hello, Flaskasdasd!'


@app.route('/api/recommend', methods=['POST'])
def generate():
    with open("../updated_influencers.json", "r") as f:
        data = json.load(f)

    recommended_names = ['KIARA', 'Sara Kapoor', 'Rhea Malhotra', 'Ananya Desai']
    # Extract full names and descriptions
    matched_entries = [entry for entry in data if entry.get("full_name") in recommended_names]

    return matched_entries

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)
