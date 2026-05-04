--> Mock API Generator (Python + Flask)



A simple interactive Python-based tool to dynamically create mock APIs for testing purposes.
It allows users to define HTTP methods and response structures at runtime and exposes a local endpoint for testing API flows without backend dependency.


--> Features  


Interactive CLI-based API generator
Supports GET, POST, PUT, DELETE methods
Accepts custom JSON response structure
Automatically creates a local mock endpoint
Useful for QA, automation testing, and frontend development


--> Tech Stack  


Python
Flask (Web Framework)

--> How It Works  


Run the Python script
Enter the HTTP method you want to mock
Paste the JSON response structure
The tool starts a local server
Use the generated endpoint for testing

--> Installation & Setup  


pip3 install flask

--> Run the application  


python3 MockAPI.py
