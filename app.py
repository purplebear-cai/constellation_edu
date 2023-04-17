from flask import Flask, render_template, request, jsonify
from src.fetch_constellation_data import ConstellationData

app = Flask(__name__)
constellation_data = ConstellationData()


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/get_constellation_info', methods=['POST'])
def get_constellation_info():
    constellation_name = request.form.get('constellation_name', '')
    constellation_info = constellation_data.fetch_constellation_info(constellation_name)
    constellation_map = constellation_data.fetch_constellation_map(constellation_name)
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