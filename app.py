from flask import Flask, render_template

# a python library to fetch APIs -- different from request in the flask library
import requests
import random

app: Flask = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/joke")
def my_jokes():
    # intialize a variable a_joke and call the API function get_a_joke()
    a_joke: dict[str, str] = ...

    # Now, we'll render the designated HTML template, 'jokes.html' . Then will the setup and punchline values to the template
    # use the keys "setup" and "punchline" to access the value associated with that key -- this is the informat we want to display!

    # Ex: setup=a_joke["setup"]
    return render_template('joke.html', setup= a_joke[...], punchline=a_joke[...])


@app.route("/many-jokes")
def many_jokes():
    # intialize a variable ten_jokes and call the API function get_10_jokes() (TAKE NOTE OF THE TYPE IT RETURNS)
    ten_jokes: list[dict[str, str]] = ...

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
    data = ...

    # call .json() on the data variable - this will parse the JSON to a dict[str,str]
    # be careful of json structure -- sometimes it can be formatted within a list!
    response: dict[str, str] = ...

    return response


@app.route("/api/ten_jokes")
def get_10_jokes() -> list[dict[str, str]]:

    # Joke API endpoint URLs
    jokes_api_url: str = "https://official-joke-api.appspot.com/random_ten"

    # using the requests library's get function to call the API, store data as a variable
    # don't worry about the type, Python will take care of this

    # use requests.get() and pass in the API URL variable -- this will fetch a JSON
    data = ...

    # # call .json() on the data variable - this will parse the JSON
    # The response JSON is now a LIST of dictionaries! It's important to know the structure of response JSON!
    response: list[dict[str, str]] = ...

    return response


@app.route("/api/pictures")
def get_pictures() -> dict[str, str]:
    # We'll be using Mars Rover images from NASA: https://api.nasa.gov/index.html

    # Follow along with the documentation and create an account to generate a unique app id and key
    app_key = "<API KEY>"



    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=<API KEY>"
    data = ...

    # call .json() on data
    response = ...

    return response


@app.route("/mars")
def my_pictures():
    # Right now, we are just returning the image and date of a random index in a JSON full of mars rover images
    # Look at the jokes example we did earlier if you want to experiment with reformatting the data!
    
    # Read the NASA Mars Rover Pictures API documentation for more information on how to use the API!

    num = random.randint(1, 3)

    # Call get_pictures()
    pictures: dict[str, str] = ...
    # the dictionary returned from this API call is a lot more complicated than previous examples we've shown, notice the keys and indicing below
    return render_template('mars.html', source=pictures['photos'][num]['img_src'], date=pictures['photos'][num]['earth_date'])


if __name__ == '__main__':
    app.run(debug=True)
