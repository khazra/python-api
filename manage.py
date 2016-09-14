import unittest
import coverage
import os

from src.app import app
from src import db
from src.model.user import User

from flask_script import Manager

manager = Manager(app)


@manager.command
def test():
    tests = unittest.TestLoader().discover('tests')
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


@manager.command
def create_db_tables():
    if db.create_all():
        return 0

    return 1


@manager.option('-p', '--password', dest='password')
def create_admin(password):
    if not password:
        password = 'password'

    admin = User('admin', password, True, 'ADMIN')
    db.session.add(admin)

    if db.session.commit():
        return 0

    return 1


if __name__ == '__main__':
    manager.run()
