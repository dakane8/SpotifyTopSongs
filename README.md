# Hack110 Fall 2022 API Workshop

## What are you APIs?

An API (Application Programming Interface) is a way to send data between computers, usually through the Internet through "requests" and "responses". A program sends a request to an API on the web, which fetches that data and sends it back to the program in a simple file format. APIs are very powerful and have many real-world applications.

## Setup

Open VSCode and click on **Clone Git Repository...**

Then, paste `git clone https://github.com/VitorInserra/apiworkshop`

<img width="338" alt="Screen Shot 2022-11-16 at 4 00 40 PM" src="https://user-images.githubusercontent.com/69722735/202293238-cdc8207a-2f84-451f-ad15-4c6100507669.png">

This is a demo for APIs using Python's requests library. Before we get started, you should download the library.

Open the terminal in VSCode and run:

`pip install requests`

If prompted, you should update pip to the latest version, use

`python3 -m pip install --upgrade pip`

Once that's done you can import the requests library into your Python file using import requests.

## What We'll Be Working On

We will be using the Offical Joke API: https://github.com/15Dkatz/official_joke_api

**Our application will have two tabs that:**

- calls a random single joke using GET https://official-joke-api.appspot.com/random_joke
- calls for ten random joke using GET https://official-joke-api.appspot.com/random_ten

**BONUS CHALLENGE:**

- Oxford Dictionaries GET call using App Id & API Key: https://developer.oxforddictionaries.com/documentation

**This is what the final product should look like:**

<img width="500" src="https://github.com/VitorInserra/apiworkshop/blob/jokes-tab/Screen%20Recording%202022-11-16%20at%204.07.50%20PM.gif" />

## Finished Demo

https://github.com/meghansun322/api-workshop-demo/tree/finished-demo

## Contributors

Vitor Inserra, Jessica Bring, Shefali Pai
