from flask import Flask, request, jsonify, send_from_directory
import json, os

app = Flask(__name__, static_folder='')

DATA_FILE = "data.json"

def load_users():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_users(users):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)

# HTML sayfalarını sun
@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/register.html')
def register_page():
    return send_from_directory('', 'register.html')

# Kayıt endpoint
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        return jsonify({"status": "error", "message": "Eksik bilgiler"}), 400

    users = load_users()
    
    # Kullanıcı adı mevcut mu?
    if any(u["username"] == username for u in users):
        return jsonify({"status": "error", "message": "Kullanıcı adı mevcut"}), 400

    # Yeni kullanıcı ekle
    users.append({"username": username, "password": password})
    save_users(users)

    return jsonify({"status": "success", "message": "Kayıt başarılı"}), 200

# Giriş endpoint
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    users = load_users()
    user = next((u for u in users if u["username"] == username and u["password"] == password), None)

    if user:
        return jsonify({"status": "success", "message": "Giriş başarılı"}), 200
    else:
        return jsonify({"status": "error", "message": "Kullanıcı adı veya şifre yanlış"}), 400

if __name__ == "__main__":
    app.run(debug=True)
