from flask import Flask, request, jsonify, abort
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://promise-kappa.vercel.app/"}})
@app.route('/test', methods=['POST']) # Manzil yaratish
def my_function():
    data = request.json # Konvertni ochib, ichidagi ma'lumotni olish
    print(data)         # Terminalda ko'rish
    return jsonify({"status": "olindi"})

@app.route('/products', methods=['GET'])
def get_function():
    auth_headers = request.headers.get('X-men');
    if(auth_headers != 'XMLhttpshokhrukh'):
        abort(403);
    return "Mahsulot"