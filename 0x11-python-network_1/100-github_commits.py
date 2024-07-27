#!/usr/bin/python3
"""
take in 2 arguments in order to list 10 commits
(from the most recent to oldest) of a repository
using use the GitHub API. and Print
"""
import requests
import sys

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {
        'per_page': 10
    }
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Error: Unable to fetch commits")

    commits = response.json()

    for commit in commits:
        sha = commit.get('sha')
        author_name = commit.get('commit', {}).get('author', {}).get('name')
        print(f"{sha}: {author_name}")
