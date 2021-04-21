from github.client import GitHubClient
from repo.parser import RepoParser
from repo.report_generator import ReportGenerator

if __name__ == "__main__":
    username = 'rafaelcamarda'
    response = GitHubClient.get_repos_by_user(username)

    if response["status_code"] == 200:
        repos = RepoParser.parse(response["body"])
        markdownReport = ReportGenerator.build("MARKDOWN", repos)
        htmlReport = ReportGenerator.build("HTML", repos)

        print(markdownReport)
        print(htmlReport)
    else:
        print(response["body"])
