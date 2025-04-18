# WSAA Assignments Repository

This repository contains completed Python assignments for the **Web Services and Application** module. Each assignment demonstrates practical usage of Python for web services, APIs, and GitHub automation.

---

## Table of Contents

- [About](#about)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Assignment Summaries](#assignment-summaries)
  - [Assignment 02 - Card Draw Game](#assignment-02---card-draw-game)
  - [Assignment 03 - CSO Dataset Fetcher](#assignment-03---cso-dataset-fetcher)
  - [Assignment 04 - GitHub File Updater](#assignment-04---github-file-updater)
- [Contributing](#contributing)
- [License](#license)
- [About the Author](#About-the-Author)
- [Reference](#Reference)

---

## About

This project was created as part of the WSAA module to explore and implement core concepts of web-based applications using Python. The repository showcases interaction with REST APIs, handling real-world data, and GitHub automation.

---

## Getting Started

You can clone the repository and run the assignments using any Python 3 environment.

### Prerequisites

- Python 3.x
- `requests` library
- `PyGithub` library
- A GitHub personal access token for assignment 04 (stored in `config.py`)

## Installation

#### Clone the repository

```bash
git clone https://github.com/filipekojak88/wsaa-assignments.git
```

#### Navigate to the project directory

```bash
cd wsaa-assignments
```

#### (Optional) Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

#### Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

You can run each assignment individually:

```bash
python assignment02-carddraw.py
python assignment03-cso.py
python assignment04-github.py
```

Ensure your config.py file is correctly set up before running Assignment 04.

## Features

- Python scripting with real-world API integration
- Practical examples of working with JSON and RESTful APIs
- Automated GitHub repository interaction
- Secure token-based authentication handling

## Assignment Summaries

### Assignment 02 - Card Draw Game

`File`: assignment02-carddraw.py

`Summary`: Simulates drawing 5 cards from the Deck of Cards API and checks for:
- Pairs
- Triples
- Straights (including Ace-low)
- Same suit

`Key Features`:
- Uses Deck of Cards API
- Analyzes hand with collections.Counter
- Detects poker-style combinations
- Prints a clean summary of the hand and its evaluation

`Scrpt`:

This script uses the requests library to talk to the Deck of Cards API online. It sends a request to get a new shuffled deck and then draws five cards from it. The requests.get() function is what actually makes that connection, and .json() helps turn the API response into a Python dictionary so we can easily work with the data [01](#01), [02](#02), [03](#03), [04](#04).

We use the json module to handle the data that comes back from the API in JSON format. This is important because the card info (like the values and suits) comes in that format, and json makes it easy to turn it into something Python can understand and work with [05](#05).

The Counter class from the collections module helps us count how many times each card value and suit shows up in the hand. It’s super useful for figuring out if we have pairs, triples, or all cards of the same suit, without needing to write a lot of code ourselves [06](#06).

### Assignment 03 - CSO Dataset Fetcher

`File`: assignment03-cso.py

`Summary`: Fetches and stores the "Exchequer Account (Historical Series)" dataset from the Irish CSO API.

`Key Features`:
- Uses RESTful API provided by the CSO
- Downloads JSON data
- Provides foundation for further data analysis

`API Endpoint`:
https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en

`Scrpt`:

This script uses the requests library to connect to an online API and get data from it. The requests.get() function is what actually sends the request to the URL and waits for the response. It's like asking the website for information and then waiting for the answer. Once we get a response, we use .json() to convert the data into a format that Python can understand and work with easily, turning it into a dictionary [02](#02), [03](#03), [04](#04).

We use json.dump() to write the data into a .json file so we can store it and maybe use it later without needing to download it again. This is helpful when working with large datasets or when you need to access the data offline [05](#05), [07](#07).

The open() function is used to create or open a file on the computer. In the store_file() function, we open a file called cso.json in write mode and then save the data into it. It’s a simple but powerful way to save stuff from the code to files [08](#08).

Finally, the if __name__ == "__main__": part makes sure that the script only runs the store_file(URL) line if the file is run directly. This is to control how and when code is executed, especially when working with functions that might also be used in other scripts [#09](09).

### Assignment 04 - GitHub File Updater

`File`: assignment04-github.py

`Summary`: Connects to a GitHub repository to:
- Retrieve a file.
- Replace the name "Andrew" with "Filipe" (case-insensitive).
- Push the updated file back to the repo.

`Key Features`:
- Secure API token handling via `.gitignored` and `config.py`
- GitHub automation with PyGithub
- Simple yet powerful text manipulation workflow

`Scrpt`:

The script starts by using the requests library to get the content of a file from a GitHub repository through its direct download URL. Then, by accessing `.text`, we get the file content as a plain string that we can work with [02](#02), [03](#03).

To change the content of the file, the script uses Python’s re module. Specifically, it uses re.sub() to search for the name "Andrew" and replace it with "Filipe". The \b ensures it matches only the full word "Andrew", and re.IGNORECASE makes sure the case (like ANDREW or andrew) doesn’t matter. This is a great example of how regular expressions let you find and edit text in a powerful way [10](#10), [11](#11).

The GitHub interaction happens thanks to the PyGithub library, which makes it easier to connect with GitHub using Python. After logging in with an API key, the script gets a specific repository and the file you want to edit. Using `get_contents()` retrieves the file, and `update_file()` sends the new version of the file back to GitHub. PyGithub handles the hard stuff behind the scenes like authentication and formatting the update request [12](#12), [13](#13).

## Contributing

This project was developed for academic purposes, but contributions or feedback are welcome.
To contribute or provide feedback please email me through the email g00439340@atu.ie.

## License

This project is licensed for academic and personal use.
Feel free to adapt or expand for your own learning.

## About the Author

I am currently a Quality Engineer with a Production Engineering & Management background. Though I have had around 12 years of experience swinging between the medical device and car assembly industry, I am currently chasing a change in my career through this course of Data Analytics in ATU. My long term goal is to move into Artificial Intelligence. If you want to know more about me, please add me on LinkedIn: [Filipe Carvalho](https://www.linkedin.com/in/filipe-carvalho-8146232a/)

## Reference:

<a id="01">[01]</a> Deck of Cards API. (n.d.). Deck of Cards API Documentation. Available at: https://deckofcardsapi.com/ [Accessed 17 Apr. 2025].  

<a id="02">[02]</a> Requests. (n.d.). Requests: HTTP for Humans. Available at: https://docs.python-requests.org/en/latest/ [Accessed 17 Apr. 2025].  

<a id="03">[03]</a> Real Python. (n.d.). Python’s Requests Library (Guide). Available at: https://realpython.com/python-requests/ [Accessed 17 Apr. 2025].

<a id="04">[04]</a> W3Schools. (n.d.). Python Requests Module. Available at: https://www.w3schools.com/python/module_requests.asp [Accessed 17 Apr. 2025].    

<a id="05">[05]</a> GeeksforGeeks. (2023). Working with JSON data in Python. Available at: https://www.geeksforgeeks.org/working-with-json-data-in-python/ [Accessed 17 Apr. 2025]. 

<a id="06">[06]</a> W3Schools. (n.d.). Python Collections Module. Available at: https://www.w3schools.com/python/ref_collections_counter.asp [Accessed 17 Apr. 2025]. 

<a id="07">[07]</a> Real Python. (n.d.). Reading and Writing Files in Python. Available at: https://realpython.com/read-write-files-python/ [Accessed 17 Apr. 2025].
 
<a id="08">[08]</a> Python Software Foundation. (n.d.). open() — Python documentation. Available at: https://docs.python.org/3/library/functions.html#open [Accessed 17 Apr. 2025]. 

<a id="09">[09]</a> GeeksforGeeks. (n.d.). What does if name == “main” do in Python? Available at: https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/ [Accessed 17 Apr. 2025].

<a id="10">[10]</a> GeeksforGeeks. (n.d.). re.sub() in Python. Available at: https://www.geeksforgeeks.org/python-re-sub/ [Accessed 17 Apr. 2025].

<a id="11">[11]</a> Python Software Foundation. (n.d.). re.sub() — Python documentation. Available at: https://docs.python.org/3/library/re.html#re.sub [Accessed 17 Apr. 2025].  

<a id="12">[12]</a> GitHub. (n.d.). PyGithub Documentation. Available at: https://pygithub.readthedocs.io/en/latest/ [Accessed 17 Apr. 2025]. 

<a id="13">[13]</a> GitHub. (n.d.). GitHub Objects — PyGithub Documentation. Available at: https://pygithub.readthedocs.io/en/latest/github_objects/ [Accessed 17 Apr. 2025].  
