from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/v2/en/country/<country>/indicator/<indicator>')
def mock_gini(country, indicator):
    year = request.args.get("date")
    format_type = request.args.get("format", "json")
    mock_data = [
        {},
        [{
            "indicator": {"id": indicator, "value": "GINI index"},
            "country": {"id": country, "value": "Mock Country"},
            "value": 38.7,  # mock value
            "date": year
        }]
    ]

    return jsonify(mock_data)

if __name__ == '__main__':
    app.run(port=5001)
