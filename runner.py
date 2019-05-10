"""
Runner
"""
from HTMLTestRunner import HTMLTestRunner
import unittest
import time


if __name__ == "__main__":
    now = time.strftime("%Y%m%d-%H%M%S")
    file_name = "report/{}-result.html".format(now)
    with open(file_name, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title="Auto Testing Report", description="Windows 10 Firefox")
        discovr = unittest.defaultTestLoader.discover("./springdemo/test_case", pattern="M*.py")
        runner.run(discovr)
