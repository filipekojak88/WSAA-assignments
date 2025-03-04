import requests
import re
from github import Github
from config import config as cfg

# Retrieve the GitHub API key from the config file
apikey = cfg['githubkey']

# Authenticate with GitHub using the API key
g = Github(apikey)  

# Uncommented -> list all repositories of the authenticated user
#for repo in g.get_user().get_repos():
#   print(repo.name)

# Get specific repository by my github user account and the repository name
repo = g.get_repo("filipekojak88/aprivateone")
#print(repo.clone_url)

# Retrieve the file information for "wikipedia.txt" from the repository aprivateone
file_info = repo.get_contents("wikipedia.txt")

# Get the direct URL to download the file content
url_of_file = file_info.download_url
#print(url_of_file)

# # Fetch the file content from the URL
response = requests.get(url_of_file)
content_of_file = response.text
#print (content_of_file)

# Replace occurrences of "Andrew" with "Filipe" where case is ignored
replace_content = re.sub(r"\bAndrew\b", "Filipe", content_of_file, flags=re.IGNORECASE)
#print(replace_content)

# Update the file in the repository with the modified content
git_hub_response = repo.update_file(file_info.path, "updated by python program assignment04-github.py", replace_content, file_info.sha)
print(git_hub_response)