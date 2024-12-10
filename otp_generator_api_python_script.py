from flask import Flask, jsonify, request
import random

app = Flask(__name__)

def generate_otp(length=4):
    """
    Generate a one-time password (OTP) consisting of digits.
    
    :param length: Length of the OTP (default is 4).
    :return: A string representing the OTP.
    """
    return ''.join(random.choices("0123456789", k=length))

@app.route('/generate-otp', methods=['GET'])
def generate_otp_api():
    """
    API endpoint to generate and return a 4-digit OTP.
    
    :return: JSON response with the generated OTP.
    """
    otp = generate_otp()
    response = {
        "otp": otp,
        "message": "OTP generated successfully"
    }
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
