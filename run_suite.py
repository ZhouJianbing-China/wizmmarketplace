import os
import unittest
from htmltestreport import HTMLTestReport

from config import DIR_PATH

suite = unittest.defaultTestLoader.discover("./script")
file_path = DIR_PATH + os.sep + "report" + os.sep + "wizmarketplace_auto.html"
HTMLTestReport(file_path).run(suite)
