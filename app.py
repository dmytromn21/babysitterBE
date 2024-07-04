from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GOOGLE_APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbz-fi8F_hH0zm7I4XfRKRFXqPIok0-GYPTH4er4VmqMMGHBPl_vO3JZ8tCR8FUGR9dG/exec'

@app.route('/identify', methods=['POST'] )
def identify():
    data = request.json
    action = 'identify'
    phone_number = data.get('phone_number')
    payload = {
        'action': action,
        'phoneNumber': phone_number
    }
    response = requests.post(GOOGLE_APPS_SCRIPT_URL, json=payload)
    return jsonify(response.json())

@app.route('/register', methods=['POST'] )
def register():
    data = request.json
    action = 'register'
    phone_number = data.get('phone_number')
    name = data.get('name')
    payload = {
        'action': action,
        'phoneNumber': phone_number,
        'name': name
    }
    response = requests.post(GOOGLE_APPS_SCRIPT_URL, json=payload)
    return jsonify(response.json())

@app.route('/add_request', methods=['POST'] )
def add_request():
    data = request.json
    action = 'add_request'
    phone_number = data.get('phone_number')
    details = data.get('details')
    payload = {
        'action': action,
        'phoneNumber': phone_number,
        'details': details
    }
    response = requests.post(GOOGLE_APPS_SCRIPT_URL, json=payload)
    return jsonify(response.json())

@app.route('/open_requests', methods=['GET'] )
def open_requests():
    action = 'open_requests'
    payload = {
        'action': action
    }
    response = requests.post(GOOGLE_APPS_SCRIPT_URL, json=payload)
    return jsonify(response.json())

@app.route('/claim_request', methods=['POST'])
def claim_request():
    data = request.json
    action = 'claim_request'
    phone_number = data.get('phone_number')
    request_id = data.get('request_id')

    payload = {
        'action': action,
        'phoneNumber': phone_number,
        'requestId': request_id
    }

    response = requests.post(GOOGLE_APPS_SCRIPT_URL, json=payload)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=False)
