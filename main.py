import os
import subprocess

import requests


def clone_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    repos = response.json()

    for number, repo in enumerate(repos):
        repo_name = repo["name"]
        repo_url = repo["clone_url"]
        repo_path = os.path.join("cloned-repos", repo_name)

        subprocess.run(["git", "clone", repo_url, repo_path])
        print("-" * 50 + f' {number + 1} : cloned "{repo_name}" successfully')

    print("cloning complete")


username = input("username > ")
clone_repos(username)
