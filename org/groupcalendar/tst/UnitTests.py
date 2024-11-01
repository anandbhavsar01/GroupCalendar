# Runs all the unit tests for the project
import unittest

loader = unittest.TestLoader()
suite = loader.discover(start_dir="groupcalendar/tst")
runner = unittest.TextTestRunner()
runner.run(suite)