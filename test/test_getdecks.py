import requests

# Define the URL for the get-decks endpoint
url = "http://localhost:5000/users/get-decks"

# Prompt the user to enter the JWT token
jwt_token = input("Enter your JWT token: ")

# Send the POST request with the Authorization header
headers = {
    "Authorization": f"Bearer {jwt_token}"
}
response = requests.post(url, headers=headers)

# Print the response status and JSON data
print("Status Code:", response.status_code)
print("Response JSON:", response.json())