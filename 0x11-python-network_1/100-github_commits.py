#!/usr/bin/python3
"""
take in 2 arguments in order to list 10 commits
(from the most recent to oldest) of a repository
using use the GitHub API. and Print
"""
import requests
import sys

if __name__ == "__main__":

    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    response = requests.get(url)
    json_resp = response.json()

for commit in json_resp[:10]:
    commit_data = commit['commit']
    sha = commit_data.get('sha')
    author = commit_data.get('author').get('name')
    print(f"{sha}: {author}")
    pass
