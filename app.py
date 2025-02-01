from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_cors import CORS
import qrcode
import pyotp
from datetime import datetime

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///seats.db'  # Change for PostgreSQL/MySQL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model
class Seat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    qr_code = db.Column(db.String(255), unique=True, nullable=False)
    status = db.Column(db.String(50), default="Available")
    check_in_time = db.Column(db.DateTime, nullable=True)

def generate_qr(seat_id):
    qr = qrcode.make(f"http://localhost:3000/checkin/{seat_id}")
    qr.save(f"static/qrcodes/seat_{seat_id}.png")
    return f"static/qrcodes/seat_{seat_id}.png"

# Generate OTP
otp_secret = pyotp.random_base32()

def verify_otp(user_otp):
    return pyotp.TOTP(otp_secret).verify(user_otp)

@app.route('/generate_qr/<int:seat_id>', methods=['GET'])
def generate_qr_code(seat_id):
    seat = Seat.query.get(seat_id)
    if seat:
        qr_path = generate_qr(seat_id)
        return jsonify({"qr_code": qr_path})
    return jsonify({"error": "Seat not found"}), 404

@app.route('/checkin', methods=['POST'])
def checkin():
    data = request.json
    seat = Seat.query.get(data['seat_id'])
    if seat and verify_otp(data['otp']):
        seat.status = "Occupied"
        seat.check_in_time = datetime.now()
        db.session.commit()
        socketio.emit("update_seat", {"seat_id": seat.id, "status": "Occupied"})
        return jsonify({"message": "Check-in successful"})
    return jsonify({"error": "Invalid OTP or seat"}), 400

@app.route('/seats', methods=['GET'])
def get_seats():
    seats = Seat.query.all()
    return jsonify([{"id": s.id, "status": s.status} for s in seats])

@socketio.on("seat_update")
def handle_seat_update(data):
    seat = Seat.query.get(data['seat_id'])
    if seat:
        seat.status = data['status']
        db.session.commit()
        socketio.emit("update_seat", {"seat_id": seat.id, "status": seat.status})

# Ensure to create the tables inside the application context
if __name__ == '__main__':
    with app.app_context():  # Wrap db.create_all() within the application context
        db.create_all()
    socketio.run(app, debug=True, port=5000)
