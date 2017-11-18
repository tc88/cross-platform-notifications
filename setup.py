import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "cross-platform-notifications",
    version = "0.0.2",
    author = "Thorben Casper",
    author_email = "thorben.casper@gmx.de",
    description = ("A tool to use for cross-platform notifications."),
    license = "GPL",
    keywords = "notifications, cross platform",
    url = "http://packages.python.org/cross-platform-notifications",
    packages=['cross-platform-notifications', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
)
