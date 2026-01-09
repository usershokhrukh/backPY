from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/test', methods=['POST']) # Manzil yaratish
def my_function():
    data = request.json # Konvertni ochib, ichidagi ma'lumotni olish
    print(data)         # Terminalda ko'rish
    return jsonify({"status": "olindi"})