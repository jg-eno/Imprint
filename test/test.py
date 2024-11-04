import requests

# Define the URL for the protected endpoint
url = "http://localhost:5000/protected2"

# Prompt the user to enter the JWT token
jwt_token = input("Enter your JWT token: ")

# Send the GET request with the Authorization header
headers = {
    "Authorization": f"Bearer {jwt_token}"
}
response = requests.get(url, headers=headers)

# Print the response status and JSON data
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
