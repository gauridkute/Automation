from flask import Flask, request,jsonify
import json

app = Flask(__name__)

mock_method = None
mock_response = None

def get_user_input():
    global mock_method, mock_response
    print("====== MOCK API GENERATOR ======")
    
    # Input for method
    method = input("Enter HTTP method to mock (GET/POST/PUT/DELETE): ").upper()
    while method not in ["GET", "POST", "PUT", "DELETE"]:
        method = input("Invalid method. Enter GET/POST/PUT/DELETE: ").upper()
    mock_method = method

    # Input for Reponse Structure
    print("\n Paste your JSON Response (single line or valid JSON):")
    response_input = input()

    try:
        mock_response = json.loads(response_input)
    except json.JSONDecodeError:
        print("Invalid JSON. Using default response.")
        mmock_response = {"message": "Invalid JSON provided"}

    print("\n✅ Mock API created!")
    print(f"➡️ URL: http://127.0.0.1:5000/mock")
    print(f"➡️ Method: {mock_method}")
    print("====================================\n")

@app.route('/mock', methods=["GET", "POST", "PUT", "DELETE"])
def mock_endpoint():
    if request.method != mock_method:
        return jsonify({
            "error": f"Only {mock_method} method is allowed"
        }), 405

    return jsonify(mock_response), 200


if __name__ == '__main__':
    get_user_input()
    app.run(debug=True, port=5000)