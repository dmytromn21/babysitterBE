from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GOOGLE_APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbz-fi8F_hH0zm7I4XfRKRFXqPIok0-GYPTH4er4VmqMMGHBPl_vO3JZ8tCR8FUGR9dG/exec'

@app.route('/gpt-webhook', methods=['POST'])
def gpt_webhook():
    data = request.json
    action = data.get('action')
    phone_number = data.get('phone_number')
    name = data.get('name')
    details = data.get('details')
    request_id = data.get('request_id')

    payload = {
        'action': action,
        'phoneNumber': phone_number,
        'name': name,
        'details': details,
        'requestId': request_id
    }

    response = requests.post(GOOGLE_APPS_SCRIPT_URL, json=payload)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=False)
