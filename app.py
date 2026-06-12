from flask import Flask, render_template, request, jsonify
from checker import check_password_strength

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    password = data.get('password', '')

    if not password:
        return jsonify({"error": "No password provided"}), 400

    result = check_password_strength(password)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
