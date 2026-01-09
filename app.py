from flask import Flask, request, jsonify, abort
from flask_cors import CORS

app = Flask(__name__)

# 1-tuzatish: Manzil oxiridagi / olib tashlandi
# CORS(app, resources={r"/*": {"origins": "https://promise-kappa.vercel.app"}})
# CORS(app, resources={r"/*": {"origins": "*"}})
CORS(app, resources={r"/*": {
    "origins": "*", 
    "methods": ["GET", "POST", "OPTIONS"],
    "allow_headers": ["Content-Type", "X-men"]
}})
@app.route('/test', methods=['POST'])
def my_function():
    data = request.json
    print(data)
    return jsonify({"status": "olindi"})

@app.route('/products', methods=['GET'])
def get_function():
    # 2-tuzatish: Header nomi va qiymatini tekshirish
    auth_header = request.headers.get('X-men')
    if auth_header != 'XMLhttpshokhrukh':
        abort(403)
    
    return "Mahsulot"