
class ReportFileWriter():

    @staticmethod
    def write_file(report):
        file = open('report.txt', 'a+')
        file.write(report)
        file.close()