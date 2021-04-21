from .file_writer import ReportFileWriter
from .database_writer import ReportDatabaseWriter


class ReportWriter():

    def write(report, writer):
        writer.write(report)