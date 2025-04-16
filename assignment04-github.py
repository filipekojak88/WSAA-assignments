# Title: Assignment 04 - GitHub File Updater
# Description: This program retrieves a file from a GitHub repository, 
# modifies its content by replacing the name "Andrew" with "Filipe",
# and updates the file in the repository.
# Author: Filipe Carvalho

## Import the necessary libraries
import requests
import re
from github import Github
from config import config as cfg

# Retrieve the GitHub API key from the config file
apikey = cfg['githubkey']

# Authenticate with GitHub
git_aut = Github(apikey)

# Get the specific repository
repo = git_aut.get_repo("filipekojak88/aprivateone")

# Retrieve file info for "wikipedia.txt"
file_info = repo.get_contents("wikipedia.txt")

# Get file content
url_of_file = file_info.download_url
response = requests.get(url_of_file)
content_of_file = response.text

# Replace "Andrew" with "Filipe" (case-insensitive)
replace_content = re.sub(r"\bAndrew\b", "Filipe", content_of_file, flags=re.IGNORECASE)

# Update the file with the modified content
git_hub_response = repo.update_file(file_info.path, "updated by python program assignment04-github.py", replace_content, file_info.sha)
# Print the response from GitHub
print(git_hub_response)
