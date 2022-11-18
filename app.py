from flask import Flask, render_template

# a python library to fetch APIs -- different from request in the flask library
import requests

app: Flask = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/joke")
def my_jokes():
    a_joke: dict[str, str] = get_a_joke()
    return render_template('joke.html', setup=a_joke["setup"], punchline=a_joke["punchline"])


@app.route("/many-jokes")
def many_jokes():
    ten_jokes: list[dict[str, str]] = get_10_jokes()
    return render_template('many-jokes.html', jokes=ten_jokes)


@app.route("/definition")
def my_definitions():
    # Right now, we are just returning the plain dictionary
    # Look at the jokes example we did earlier if you want to experiment with reformatting the data!
    # Read the Oxford Dictionary API documentation for more information on how to use the API!
    a_definition: dict[str, str] = get_a_def()

    # the dictionary returned from this API call is a lot more complicated than previous examples we've shown, notice the keys and indicing below
    return render_template('definition.html', word=a_definition['id'], definition=a_definition['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])


# API CALLS

@app.route("/api/joke")
def get_a_joke() -> dict[str, str]:

    # Joke API endpoint URLs
    jokes_api_url: str = "https://official-joke-api.appspot.com/random_joke"

    # using the requests library's get function to call the API, store data as a variable
    # don't worry about the type, Python will take care of this
    data = requests.get(jokes_api_url)

    # Parse JSON to a dict[str, str]
    # be careful of json structure -- sometimes it can be formatted within a list!
    response: dict[str, str] = data.json()
    return response


@app.route("/api/ten_jokes")
def get_10_jokes() -> list[dict[str, str]]:

    # Joke API endpoint URLs
    jokes_api_url: str = "https://official-joke-api.appspot.com/random_ten"

    # using the requests library's get function to call the API, store data as a variable
    # don't worry about the type, Python will take care of this
    data = requests.get(jokes_api_url)

    # Parse JSON to a dict[str, str]
    # The response JSON is now a LIST of dictionaries! It's important to know the structure of response JSON!
    response: list[dict[str, str]] = data.json()
    return response


@app.route("/api/definition")
def get_a_def() -> dict[str, str]:
    # Below lines of code are all from the API documentation: https://developer.oxforddictionaries.com/documentation/getting_started
    # Follow along with the documentation and create an account to generate a unique app id and key
    app_id = "<insert your id here>"
    app_key = "<insert your key here>"

    language = "en-gb"  # sets language to English

    word_id = "hackathon"  # change this variable to see different word definitions

    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + \
        language + "/" + word_id.lower()
    data = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    response = data.json()
    return response


if __name__ == '__main__':
    app.run(debug=True)
