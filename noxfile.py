import nox

@nox.session
def lint(session):
    session.install("flake8")
    session.run("flake8", "tempest.py")


@nox.session
def tests(session):
    session.install("pytest")
    session.run("pytest", "test_tempest.py")
