import time
import os
import logging

ReportDir = None

# report
def get_report_info(suites_path):
    global ReportDir
    route_folder = suites_path.split('\\testsuite\\')[1]
    suite_name = route_folder.split('.')[0]
    nowtime = time.strftime("%Y%m%d%H%M%S")
    report_folder_name = suite_name + '_' + nowtime
    report_folder_path = suites_path.split(r'\testsuite')[0]

    description = suite_name
    report_name = "TestReport"
    ReportDir = os.path.join(report_folder_path,'testresult', report_folder_name)
    return description, report_name, ReportDir


def take_screenshot(driver,case_name):
    try:
        if ReportDir == None:
            pass
        nowtime = time.strftime("%Y%m%d%H%M%S")
        screenshot_dir = os.path.join(ReportDir, case_name)
        os.makedirs(screenshot_dir, exist_ok=True)
        driver.save_screenshot(screenshot_dir + "/screenshot_" + nowtime + ".png")
    except Exception as error:
        print("Error happened during take the screenshot. %s" % error)


class Log(object):

    def __init__(self,case_name):
        # Log path
        # if ReportDir == None:
        #     pass
        # log_path = os.path.join(ReportDir, case_name)
        log_path=case_name
        if not os.path.exists(log_path):os.mkdir(log_path)
        # Log file name
        self.logname = os.path.join(log_path, 'log_%s.log' % time.strftime("%Y%m%d%H%M%S"))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # log format
        self.formatter = logging.Formatter('[%(levelname)s] : %(message)s')

    def __console(self, level, message):

        # Create a FileHandler for storing local data
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # Create a StreamHandler for displaying on console
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.exception(message)
        elif level == 'critical':
            self.logger.critical(message)
        # Avoid log duplicate
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # Close the file
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

    def critical(self,message):
        self.__console('error', message)
