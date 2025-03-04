from flask import Flask, render_template, jsonify
import firebase_admin
from firebase_admin import credentials, db
from waitress import serve

app = Flask(__name__, template_folder='templates')

# Inisialisasi Firebase
cred = credentials.Certificate("rumes-32c4e-firebase-adminsdk-fbsvc-be1552e49b.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://rumes-32c4e-default-rtdb.firebaseio.com/'
})

# Route untuk mendapatkan data dari Firebase
@app.route('/get_data')
def get_data():
    # Ambil data dari Firebase (misalnya di path 'sensor_data')
    ref = db.reference('sensor_data')  # Ganti dengan path yang sesuai di Firebase
    data = ref.get()  # Ambil semua data di path tersebut

    if data is None:
        return jsonify({"error": "Data not found"}), 404

    print(data)  # Debug: Cek apakah data sudah benar
    return jsonify(data)


# Route untuk halaman utama yang akan menampilkan web.html pertama kali
@app.route('/')
def index():
    return render_template('web.html')  # Merender web.html pertama kali

# Route untuk halaman web (web.html)
@app.route('/web')
def web():
    return render_template('web.html')  # Merender web.html jika diakses secara eksplisit

# Route untuk halaman index.html (jika Anda ingin mengaksesnya secara terpisah)
@app.route('/index')
def index_page():
    return render_template('index.html')  # Merender index.html jika diakses secara eksplisit

if __name__ == '__main__':
    # Untuk pengembangan lokal, gunakan app.run(debug=True)
    app.run(debug=True)
