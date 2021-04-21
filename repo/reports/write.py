from .file_writer import ReportFileWriter
from .database_writer import ReportDatabaseWriter


class ReportWriter():

    def write(report, type):
        if type == "database":
            ReportDatabaseWriter.write_file(report)
        elif type == "file":
            ReportFileWriter.write_file(report)