
import requests

# Define the URL and the test data
url = "http://localhost:5000/users/login"
data = {
    "email": "test@example.com",
    "password": "securepassword123"
}

# Send the POST request to the /users/signup endpoint
response = requests.post(url, json=data)

# Print the response status and JSON data
print("Status Code:", response.status_code)
print("Response JSON:", response.json())