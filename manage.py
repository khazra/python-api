import unittest
import coverage
import os

from src.app import app

from flask_script import Manager

manager = Manager(app)


@manager.command
def test():
    """Runs the unit tests without coverage."""

    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if result.wasSuccessful():
        return 0

    return 1


@manager.command
def cov():
    """Runs the unit tests with coverage."""
    cov = coverage.Coverage(
        branch=True,
        cover_pylib=False,
        data_file='.coverage',
        include=[
            'tests/*',
            'app/api/*'
        ],
        omit='.venv/*'
    )
    cov.start()

    tests = unittest.TestLoader().discover('tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if result.wasSuccessful():
        cov.stop()
        cov.save()
        print('\n\nCoverage Summary:\n')
        cov.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, '.tmp/coverage')
        cov.html_report(directory=covdir)
        print('\n\nHTML version: file://%s/index.html\n' % covdir)
        cov.erase()
        return 0

    return 1

if __name__ == '__main__':
    manager.run()
