# WSAA Assignments Repository

This repository contains completed Python assignments for the **Web Services and Application module. Each assignment demonstrates practical usage of Python for web services, APIs, and GitHub automation.

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
- [Contact](#contact)
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

Python scripting with real-world API integration
Practical examples of working with JSON and RESTful APIs
Automated GitHub repository interaction
Secure token-based authentication handling

## Assignment Summaries

### Assignment 02 - Card Draw Game

`File`: assignment02-carddraw.py

`Summary`: Simulates drawing 5 cards from the Deck of Cards API and checks for:
- Pairs
- Triples
- Straights (including Ace-low)
- Flushes (same suit)

`Key Features`:
- Uses Deck of Cards API
- Analyzes hand with collections.Counter
- Detects poker-style combinations
- Prints a clean summary of the hand and its evaluation

`Scrpt`:
The requests module is used to send HTTP requests to the Deck of Cards API. The requests.get() function is referenced in the script to fetch the shuffled deck and draw cards from it [01](#01) [04](#04). The response.json() function is used to parse the response from the API [05]#(05).
The json module is employed to handle the JSON responses returned by the API. The json method is used to decode the API responses into Python dictionaries [02](#02).
The collections.Counter is utilized to count the occurrences of values and suits among the drawn cards. The Counter class helps identify pairs and triples in the deck [03](#03).
The sorted() function is used to sort the card values' indices to check if they form a straight [07](#07).
The set data structure is used to check if all the drawn cards are of the same suit by ensuring the set of suits has only one unique value [08](#08).

### Assignment 03 - CSO Dataset Fetcher

`File`: assignment03-cso.py

`Summary`: Fetches and stores the "Exchequer Account (Historical Series)" dataset from the Irish CSO API.

`Key Features`:
- Uses RESTful API provided by the CSO
- Downloads JSON data
- Provides foundation for further data analysis

`API Endpoint`:
https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en

### Assignment 04 - GitHub File Updater

`File`: assignment04-github.py

`Summary`: Connects to a GitHub repository to:
- Retrieve a file.
- Replace the name "Andrew" with "Filipe" (case-insensitive).
- Push the updated file back to the repo.

`Key Features`:
- Secure API token handling via .gitignored config.py
- GitHub automation with PyGithub
- Simple yet powerful text manipulation workflow

## Contributing

This project was developed for academic purposes, but contributions or feedback are welcome.
To contribute or provide feedback please email me through the email g00439340@atu.ie.

## License

This project is licensed for academic and personal use.
Feel free to adapt or expand for your own learning.

## About the Author

I am currently a Quality Engineer with a Production Engineering & Management background. Though I have had around 12 years of experience swinging between the medical device and car assembly industry, I am currently chasing a change in my career through this course of Data Analytics in ATU. My long term goal is to move into Artificial Intelligence. If you want to know more about me, please add me on LinkedIn: [Filipe Carvalho](https://www.linkedin.com/in/filipe-carvalho-8146232a/)

## Reference:

<a id="01">[01]</a> Requests. (n.d.). Requests: HTTP for Humans. Available at: https://docs.python-requests.org/en/latest/ [Accessed 17 Apr. 2025].  

<a id="02">[02]</a> Python Software Foundation. (n.d.). json — JSON encoder and decoder. Available at: https://docs.python.org/3/library/json.html [Accessed 17 Apr. 2025]. 

<a id="03">[03]</a> Python Software Foundation. (n.d.). collections — High-performance container datatypes. Available at: https://docs.python.org/3/library/collections.html#collections.Counter [Accessed 17 Apr. 2025].  

<a id="04">[04]</a> Requests. (n.d.). Requests Quickstart. Available at: https://docs.python-requests.org/en/latest/user/quickstart/#make-a-request [Accessed 17 Apr. 2025].  

<a id="05">[05]</a> Requests. (n.d.). Response.json() — Requests 2.x documentation. Available at: https://docs.python-requests.org/en/latest/api/#requests.Response.json [Accessed 17 Apr. 2025].  

<a id="06">[06]</a> Python Software Foundation. (n.d.). Data Structures. Available at: https://docs.python.org/3/tutorial/datastructures.html [Accessed 17 Apr. 2025].  

<a id="07">[07]</a> Python Software Foundation. (n.d.). sorted() — Python documentation. Available at: https://docs.python.org/3/library/functions.html#sorted [Accessed 17 Apr. 2025].  

<a id="08">[08]</a> Python Software Foundation. (n.d.). set — Set types. Available at: https://docs.python.org/3/library/stdtypes.html#set [Accessed 17 Apr. 2025].  

<a id="09">[09]</a> Python Software Foundation. (n.d.). len() — Python documentation. Available at: https://docs.python.org/3/library/functions.html#len [Accessed 17 Apr. 2025].  

<a id="10">[10]</a> Python Software Foundation. (n.d.). print() — Python documentation. Available at: https://docs.python.org/3/library/functions.html#print [Accessed 17 Apr. 2025].  

<a id="11">[11]</a> Python Software Foundation. (n.d.). for Statements — Python documentation. Available at: https://docs.python.org/3/tutorial/controlflow.html#for-statements [Accessed 17 Apr. 2025].  

<a id="12">[12]</a> Python Software Foundation. (n.d.). if Statements — Python documentation. Available at: https://docs.python.org/3/tutorial/controlflow.html#if-statements [Accessed 17 Apr. 2025].  

<a id="13">[13]</a> Deck of Cards API. (n.d.). Deck of Cards API Documentation. Available at: https://deckofcardsapi.com/ [Accessed 17 Apr. 2025].  

<a id="14">[14]</a> Python Software Foundation. (n.d.). open() — Python documentation. Available at: https://docs.python.org/3/library/functions.html#open [Accessed 17 Apr. 2025].  

<a id="15">[15]</a> Python Software Foundation. (n.d.). json.dump() — Python documentation. Available at: https://docs.python.org/3/library/json.html#json.dump [Accessed 17 Apr. 2025].  

<a id="16">[16]</a> Python Software Foundation. (n.d.). main — Top-level script environment. Available at: https://docs.python.org/3/library/__main__.html [Accessed 17 Apr. 2025].  

<a id="17">[17]</a> Python Software Foundation. (n.d.). re — Regular expression operations. Available at: https://docs.python.org/3/library/re.html [Accessed 17 Apr. 2025].  

<a id="18">[18]</a> GitHub. (n.d.). PyGithub Documentation. Available at: https://pygithub.readthedocs.io/en/latest/ [Accessed 17 Apr. 2025].  

<a id="19">[19]</a> Python Software Foundation. (n.d.). getattr() — Python documentation. Available at: https://docs.python.org/3/library/functions.html#getattr [Accessed 17 Apr. 2025].  

<a id="20">[20]</a> Python Software Foundation. (n.d.). re.sub() — Python documentation. Available at: https://docs.python.org/3/library/re.html#re.sub [Accessed 17 Apr. 2025].  

<a id="21">[21]</a> GitHub. (n.d.). GitHub Objects — PyGithub Documentation. Available at: https://pygithub.readthedocs.io/en/latest/github_objects/ [Accessed 17 Apr. 2025].  
 
