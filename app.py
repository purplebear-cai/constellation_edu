from flask import Flask, render_template, request, jsonify
from constellation_data import constellation_data

app = Flask(__name__)

# Fetch constellation information from the dataset
def fetch_constellation_info(constellation_name):
    constellation = constellation_data.get(constellation_name)
    if constellation:
        return constellation["info"]
    return None

# Fetch constellation map from the dataset
def fetch_constellation_map(constellation_name):
    constellation = constellation_data.get(constellation_name)
    if constellation:
        return constellation["map_url"]
    return None

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/get_constellation_info', methods=['POST'])
def get_constellation_info():
    constellation_name = request.form['constellation_name']
    constellation_info = fetch_constellation_info(constellation_name)
    constellation_map = fetch_constellation_map(constellation_name)

    if constellation_info and constellation_map:
        return jsonify({
            'constellation_info': constellation_info,
            'constellation_map': constellation_map
        })
    else:
        return jsonify({
            'error': 'Constellation not found. Please try another name.'
        }), 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)