""" Log output class
    Created by mahiro hoshino

    How to use:
    logger = Logger().get_logger()
    logger.error("error msg")
    logger.debug("debug msg")  etc...
    @see https://docs.python.jp/3/howto/logging.html

    Log output format:
    time(year-month-day hour-minute-seconds,millisecond): function name: line number: log name: massage
"""
import logging


class Logger:

    def __init__(self):
        self._logger = logging.getLogger(__name__)

        self._logger.setLevel(10)

        # output file log.txt
        file_handler = logging.FileHandler('log.txt')
        self._logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        self._logger.addHandler(stream_handler)

        # time(year-month-day hour-minute-seconds,millisecond): function name: line number: log name: massage
        formatter = logging.Formatter('%(asctime)s:\t%(funcName)s:\t%(lineno)d:\t%(levelname)s:\t%(message)s')

        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

    def get_logger(self):
        return self._logger
