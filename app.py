from flask import Flask, render_template
import os
import base64
# a python library to fetch APIs -- different from request in the flask library
import spotipy
import requests
import random
import json
from requests import post, get
from dotenv import load_dotenv



app: Flask = Flask(__name__)



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/after_login")
def top_ten():
    return render_template('after_login.html', songs=songs)




@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/joke")
def my_jokes():
    # intialize a variable a_joke and call the API function get_a_joke()
    a_joke: dict[str, str] = get_a_joke()


    # Now, we'll render the designated HTML template, 'jokes.html' . Then will the setup and punchline values to the template
    # use the keys "setup" and "punchline" to access the value associated with that key -- this is the informat we want to display!

    # Ex: setup=a_joke["setup"]
    return render_template('joke.html', setup= a_joke["setup"], punchline=a_joke["punchline"])




@app.route("/many-jokes")
def many_jokes():
    # intialize a variable ten_jokes and call the API function get_10_jokes() (TAKE NOTE OF THE TYPE IT RETURNS)
    ten_jokes: list[dict[str, str]] = get_10_jokes()

    # Now, we'll render the designated HTML template, 'many-jokes.html' . Then will the setup and punchline values to the template
    # This time, we'll pass in the whole list / ten_jokes variable to the template

    return render_template('many-jokes.html', jokes=ten_jokes)

# API CALLS

@app.route("/api/joke")
def get_a_joke() -> dict[str, str]:

    # Joke API endpoint URLs
    jokes_api_url: str = "https://official-joke-api.appspot.com/random_joke"

    # using the requests library's get function to call the API, store data as a variable
    # don't worry about the type, Python will take care of this

    # use requests.get() and pass in the API URL variable -- this will fetch a JSON
    data = requests.get(jokes_api_url)

    # call .json() on the data variable - this will parse the JSON to a dict[str,str]
    # be careful of json structure -- sometimes it can be formatted within a list!
    response: dict[str, str] = data.json()

    return response


@app.route("/api/ten_jokes")
def get_10_jokes() -> list[dict[str, str]]:

    # Joke API endpoint URLs
    jokes_api_url: str = "https://official-joke-api.appspot.com/random_ten"

    # using the requests library's get function to call the API, store data as a variable
    # don't worry about the type, Python will take care of this

    # use requests.get() and pass in the API URL variable -- this will fetch a JSON
    data = requests.get(jokes_api_url)

    # # call .json() on the data variable - this will parse the JSON
    # The response JSON is now a LIST of dictionaries! It's important to know the structure of response JSON!
    response: list[dict[str, str]] = data.json()

    return response


@app.route("/api/pictures")
def get_pictures() -> dict[str, str]:
    # We'll be using Mars Rover images from NASA: https://api.nasa.gov/index.html

    # Follow along with the documentation and create an account to generate a unique app id and key
    app_key = "C7np35s7SBYuprv3s9cdzJmRomx2wx0B1HQzmtHz"
    


    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key={app_key}"
    data = requests.get(url)

    # call .json() on data
    response = data.json()

    return response


@app.route("/mars")
def my_pictures():
    # Right now, we are just returning the image and date of a random index in a JSON full of mars rover images
    # Look at the jokes example we did earlier if you want to experiment with reformatting the data!
    
    # Read the NASA Mars Rover Pictures API documentation for more information on how to use the API!

    num = random.randint(1, 3)

    # Call get_pictures()
    pictures: dict[str, str] = get_pictures()
    # the dictionary returned from this API call is a lot more complicated than previous examples we've shown, notice the keys and indicing below
    return render_template('mars.html', source=pictures['photos'][num]['img_src'], date=pictures['photos'][num]['earth_date'])



load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
REDIRECT_URI = "http://localhost:8000/callback"
AUTH_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"
auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode("ascii")).decode("ascii")
auth_params = {
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    "scope": "user-top-read",
    "client_id": client_id
}
auth_url = f"{AUTH_URL}?{'&'.join([f'{k}={v}' for k, v in auth_params.items()])}"
print(f"Please visit this URL to authorize the app:\n{auth_url}")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
        }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        print("No artist with this name exists")
        return None

    return json_result[0]
    
def get_song_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result


token = get_token()
result = search_for_artist(token, "100 gecs")
artist_id = result["id"]
songs = get_song_by_artist(token, artist_id)





if __name__ == '__main__':
    app.run(debug=True)


