"""
Runner
"""
#from HTMLTestRunner import HTMLTestRunner
from BeautifulReport import BeautifulReport
import unittest
import time
import os,sys,getopt

def get_argv(argv):
    """
    get script parameters : dev, staging, live
    eg: python runner.py -e dev
    :param argv:
    :return:
    """
    env = "dev"
    try:
        opts, args = getopt.getopt(argv,"he:",["env="])
    except getopt.GetoptError:
      print('runnerTouring.py -e <environment: dev, staging, live>')
      sys.exit(2)
    for opt, arg in opts:
      if opt in ("-h", "--help"):
         print('runnerTouring.py -e <environment: dev, staging, live>')
         sys.exit()
      elif opt in ("-e", "--env"):
         env = arg
    return env

if __name__ == "__main__":
    #set env from script parameter
    os.environ["env"] = get_argv(sys.argv[1:])
    file_name = "{}-result.html".format(time.strftime("%Y%m%d-%H%M%S"))
    """
    with open(file_name, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title="Auto Testing Report", description="Windows 10 Firefox")
        discovr = unittest.defaultTestLoader.discover("./proj05_touring/test_case", pattern="T*.py")
        runner.run(discovr)
    """
    #custom define BeautifulReport.img_path
    BeautifulReport.img_path = "report/screenshot"
    #Generate Html Report
    discovr = unittest.defaultTestLoader.discover(".", pattern="m0600_check_landing_page.py")
    BeautifulReport(discovr).report(filename=file_name, description="Auto Testing Report", log_path="report")