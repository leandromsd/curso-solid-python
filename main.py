from github.client import GitHubClient
from repo.parser import RepoParser
from repo.report_generator import ReportGenerator
from repo.reports.html_generator import HTMLGenerator
from repo.reports.markdown_generator import MarkdownGenerator
from repo.reports.write import ReportWriter
from models.member import Member
from models.manager import Manager

if __name__ == "__main__":
    username = 'rafaelcamarda'
    response = GitHubClient.get_repos_by_user(username)

    if response["status_code"] == 200:
        repos = RepoParser.parse(response["body"])
        markdownReport = ReportGenerator.build(MarkdownGenerator, repos)
        htmlReport = ReportGenerator.build(HTMLGenerator, repos)

        ReportWriter.write(markdownReport, "file")
        ReportWriter.write(htmlReport, "database")

        print(markdownReport)
        print(htmlReport)
    else:
        print(response["body"])

    member = Member("leandromsd", "caixeta.leandro@gmail.com")
    manager = Manager("mtcoliveira", "mtcoliveira@gmail.com")

    print(member.members())

    member.work()
    manager.work()

