import logging

class LogFunc:


    def get_log(self):

        # create a logger
        logger = logging.getLogger('report_log')
        logger.setLevel(logging.DEBUG)
        # create console handler
        fh = logging.FileHandler("C:\\python-selenium\\orangeHR\\Logs\\log_report.log")
        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s' , datefmt='%m/%d/%Y %I:%M:%S %p')
        # add formatter to console or file handler
        fh.setFormatter(formatter)
        # add console handler to logger
        logger.addHandler(fh)

        return logger

