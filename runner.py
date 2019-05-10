"""
Runner
"""
from HTMLTestRunner import HTMLTestRunner
import unittest
import time
import os,sys,getopt

def get_argv(argv):
    """
    get script parameters : dev, staging, live
    eg: python3 runner.py -e dev
    :param argv:
    :return:
    """
    env = "dev"
    try:
        opts, args = getopt.getopt(argv,"he:",["env="])
    except getopt.GetoptError:
      print('runner.py -e <environment: dev, staging, live>')
      sys.exit(2)
    for opt, arg in opts:
      if opt in ("-h", "--help"):
         print('runner.py -e <environment: dev, staging, live>')
         sys.exit()
      elif opt in ("-e", "--env"):
         env = arg
    return env

if __name__ == "__main__":
    #set env
    os.environ["env"] = get_argv(sys.argv[1:])
    now = time.strftime("%Y%m%d-%H%M%S")
    file_name = "report/{}-result.html".format(now)
    with open(file_name, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title="Auto Testing Report", description="Windows 10 Firefox")
        discovr = unittest.defaultTestLoader.discover("./springdemo/test_case", pattern="M*.py")
        runner.run(discovr)
