import requests

# Define the URL for the logout endpoint
url = "http://localhost:5000/users/logout"
# Use the JWT token you received from the signup or login response
jwt_token = input()
# Send the POST request with the Authorization header
headers = {
    "Authorization": f"Bearer {jwt_token}"
}
response = requests.post(url, headers=headers)

# Print the response status and JSON data
print("Status Code:", response.status_code)
print("Response JSON:", response.json())