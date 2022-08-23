from Formatter.FileFormatter import FileFormatter
from logging import FileHandler


class FileStreamHandler(FileHandler, object):
    def __init__(self, file_path, fmt="[%(asctime)s] [%(levelname)s] [%(name)s] [%(funcName)s] %(message)s"):
        super(FileStreamHandler, self).__init__(file_path)
        self.formatter = FileFormatter(fmt)

    def makePickle(self, record):
        return self.formatter.format(record) + b'\n'