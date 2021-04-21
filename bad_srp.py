import requests
import json

class ListRepositories():
    API_BASE_URL = "https://api.github.com"

    def __init__(self, user):
        self.user = user

    def get_repos_by_user(self):
        response = requests.get(f'{self.API_BASE_URL}/users/{self.user}/repos')
        if response.status_code == 200:
            return {"status_code":200, "body": response.json()}
        else:
            return {"status_code":response.status_code, "body":  "Erro"}

    def parse_response(self):
        response = self.get_repos_by_user()
        body = response["body"]

        if response["status_code"] == 200:
            for i in range(len(body)):
                print(f'{body[i]["id"]}\t- {body[i]["name"]} | {body[i]["stargazers_count"]}')

repos = ListRepositories("rafaelcamarda")

responde = repos.get_repos_by_user()
responseParse = repos.parse_response()

