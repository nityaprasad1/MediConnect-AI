from flask import Flask, render_template, request, jsonify
from safety import check_emergency, check_prescription_request
from triage import classify_triage
import json
from math import radians, cos, sin, asin, sqrt

app = Flask(__name__)

def distance(lat1, lon1, lat2, lon2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371
    return c * r

def get_nearby_pharmacies(user_lat=10.7900, user_lon=78.7040):
    with open("pharmacy_db.json") as f:
        data = json.load(f)

    sorted_pharmacies = sorted(
        data,
        key=lambda x: distance(user_lat, user_lon, x["lat"], x["lon"])
    )

    return sorted_pharmacies[:3]

def generate_reply(text):
    text = text.lower()

    if "throat" in text:
        return "You may take Strepsils lozenges, warm salt water gargle and drink warm fluids."

    if "headache" in text:
        return "You may take Paracetamol and rest. Stay hydrated and avoid screen strain."

    if "cold" in text or "cough" in text:
        return "Steam inhalation, warm fluids and cough syrup can help. Monitor symptoms."

    if "fever" in text:
        return "Take Paracetamol, stay hydrated and monitor temperature."

    return "For mild symptoms you may use OTC medication and rest. If symptoms persist consult a doctor."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    if check_emergency(user_message):
        pharmacies = get_nearby_pharmacies()
        return jsonify({
            "reply": "This may be a medical emergency. Please visit a hospital immediately.",
            "triage": "severe",
            "pharmacies": pharmacies
        })

    if check_prescription_request(user_message):
        return jsonify({
            "reply": "This medication requires a doctor prescription. Please consult a doctor.",
            "triage": "restricted",
            "pharmacies": []
        })

    triage_level = classify_triage(user_message)
    reply = generate_reply(user_message)
    pharmacies = get_nearby_pharmacies()

    return jsonify({
        "reply": reply,
        "triage": triage_level,
        "pharmacies": pharmacies
    })

if __name__ == "__main__":
    app.run(debug=True)