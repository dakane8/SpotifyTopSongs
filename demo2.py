import requests
import base64

# Set up authorization headers
CLIENT_ID = "e5b9e5a6fffc46e48d2eaa469a525139"
CLIENT_SECRET = "642a823ebb834dca8cb7e455f12331dd"
REDIRECT_URI = "http://127.0.0.1:5000"
AUTH_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"
auth_header = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode("ascii")).decode("ascii")
auth_params = {
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    "scope": "user-top-read",
    "client_id": CLIENT_ID
}

# Get authorization code from user
def get_auth_token(client_id, client_secret):
    # Encode the client ID and secret as Base64
    client_creds = f"{client_id}:{client_secret}"
    encoded_client_creds = base64.b64encode(client_creds.encode())

    # Set up the headers and data for the request
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {encoded_client_creds.decode()}"
    }
    data = {
        "grant_type": "client_credentials"
    }

    # Make the request to the Spotify API
    response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the access token from the response
        access_token = response.json()["access_token"]
        return access_token
    else:
        print("Failed to obtain access token.")
        return None

auth_token = get_auth_token(CLIENT_ID, CLIENT_SECRET)
print(auth_token) 
# Get access token using authorization code
token_params = {
    "grant_type": "authorization_code",
    "code": auth_token,
    "redirect_uri": REDIRECT_URI
}
token_response = requests.post(
    TOKEN_URL,
    headers={"Authorization": f"Basic {auth_header}"},
    data=token_params
).json()
access_token = token_response.get("access_token")

# Get user's top 10 played songs of the month
top_songs_url = "https://api.spotify.com/v1/me/top/tracks"
top_songs_params = {
    "time_range": "month",
    "limit": 10
}
top_songs_response = requests.get(
    top_songs_url,
    headers={"Authorization": f"Bearer {access_token}"},
    params=top_songs_params
).json()
top_songs = [song["name"] for song in top_songs_response["items"]]
print(f"Your top 10 played songs of the month are:\n{', '.join(top_songs)}")
