import unittest
import os

import coverage
from flask import Flask, render_template
import flask

TEST_COVERAGE_FILE_DIR = "test_coverage"
TEST_COVERAGE_FILE_NAME = "index.html"
TEST_COVERAGE_FILE = os.path.join(TEST_COVERAGE_FILE_DIR, TEST_COVERAGE_FILE_NAME)

app = Flask(__name__, template_folder=TEST_COVERAGE_FILE_DIR, static_folder=TEST_COVERAGE_FILE_DIR, static_url_path='/test-coverage')


@app.route('/', methods=['GET'])
def home():
	return flask.redirect("/test-coverage")


@app.route('/test-coverage/', methods=['GET'])
def test_coverage():
	testcase_runner = TestcaseRunner()
	# testcase_runner.run_testcase_without_coverage()
	testcase_runner.run_testcase_with_coverage()
	global TEST_COVERAGE_FILE_NAME
	return render_template(TEST_COVERAGE_FILE_NAME)


class TestcaseRunner():

	_FILE_INCLUDE_PATTERNS = ['./*']
	_FILE_OMIT_PATTERNS = ['*/test_*', 'venv/*']

	def run_testcase_without_coverage(self):
		"""Runs the testcases without coverage"""

		print(self.run_testcase_without_coverage.__name__)
		tests = unittest.TestLoader().discover('.')
		unittest.TextTestRunner(verbosity=2).run(tests)


	def run_testcase_with_coverage(self):
		"""Runs the testcases with coverage"""

		print(self.run_testcase_with_coverage.__name__)
		cov = coverage.Coverage(
			branch=True,
			include=TestcaseRunner._FILE_INCLUDE_PATTERNS,
			omit=TestcaseRunner._FILE_OMIT_PATTERNS
		)
		cov.start()
		tests = unittest.TestLoader().discover('.')
		unittest.TextTestRunner(verbosity=2).run(tests)
		cov.stop()
		cov.save()
		print('\nCoverage Summary: ')
		cov.report()
		global TEST_COVERAGE_FILE
		covdir = os.path.dirname(TEST_COVERAGE_FILE)
		cov.html_report(directory=covdir)
		cov.erase()


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5050, debug=True)
