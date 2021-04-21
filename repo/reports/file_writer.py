
class ReportFileWriter():

    @staticmethod
    def write(report):
        file = open('report.txt', 'a+')
        file.write(report)
        file.close()