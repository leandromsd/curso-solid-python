from repo.reports.html_generator import HTMLGenerator
from repo.reports.markdown_generator import MarkdownGenerator


class ReportGenerator():

    @classmethod
    def build(cls, type, repos):
        if type == "HTML":
            return HTMLGenerator.build(repos)
        elif type == "MARKDOWN":
            return MarkdownGenerator.build(repos)
        else:
            return "Invalid report type"
