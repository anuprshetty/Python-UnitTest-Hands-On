import unittest
import coverage
import os


class TestcaseRunner():

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
			include=['./*'],
			omit=['*/test_*', 'venv/*']
		)
		cov.start()
		tests = unittest.TestLoader().discover('.')
		unittest.TextTestRunner(verbosity=2).run(tests)
		cov.stop()
		cov.save()
		print('\nCoverage Summary: ')
		cov.report()
		covdir = os.path.join(os.path.dirname(__file__), "test_coverage")
		cov.html_report(directory=covdir)
		cov.erase()


if __name__ == "__main__":
	testcase_runner = TestcaseRunner()
	testcase_runner.run_testcase_without_coverage()
	testcase_runner.run_testcase_with_coverage()
