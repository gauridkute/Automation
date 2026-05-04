from flask import Flask, request,jsonify
import json

app = Flask(_name_)

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