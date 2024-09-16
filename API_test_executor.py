import os
import xmlrunner
import unittest
from API_TestCases import APITesting

if __name__ == '__main__':
    # Make sure the test-reports directory exists
    if not os.path.exists('test-reports'):
        os.makedirs('test-reports')
    # Create an XMLTestRunner instance and run the tests
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    suite = unittest.TestLoader().loadTestsFromTestCase(TSAPITesting)
    runner.run(suite)
