from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get JSON data from the POST request
    # Logic for making a prediction (example)
    if 'Age' not in data or 'EstimatedSalary' not in data:
        return jsonify({"error": "Missing data"}), 400
    prediction = "Will Purchase" if data['Age'] > 30 and data['EstimatedSalary'] > 50000 else "Will Not Purchase"
    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    app.run(debug=True)
