"""
These are Pytest hooks that are necessary to ensure that no build artifacts are
leftover from previous runs. See the tests/README.md file for more info.
"""

# Hilariously, this has a pretty important role in the testing of this project.
# Without this line, deeply nested tests importing the local development copy
# of `nimporter` would fail without some PYTHONPATH manipulation. Better to
# just import and cache it in `sys.modules` at the project root. ;)
import nimporter


# import pathlib, nimporter_cli


# def pytest_sessionstart(session):
#     nimporter_cli.clean(pathlib.Path())
