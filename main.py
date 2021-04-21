from github.client import GitHubClient
from repo.parser import RepoParser
from repo.report_generator import ReportGenerator
from repo.reports.html_generator import HTMLGenerator
from repo.reports.markdown_generator import MarkdownGenerator

if __name__ == "__main__":
    username = 'rafaelcamarda'
    response = GitHubClient.get_repos_by_user(username)

    if response["status_code"] == 200:
        repos = RepoParser.parse(response["body"])
        markdownReport = ReportGenerator.build(MarkdownGenerator, repos)
        htmlReport = ReportGenerator.build(HTMLGenerator, repos)

        print(markdownReport)
        print(htmlReport)
    else:
        print(response["body"])
