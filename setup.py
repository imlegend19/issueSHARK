#!/usr/bin/env python

import sys

from setuptools import setup, find_packages

if not sys.version_info[0] == 3:
    print('only python3 supported!')
    sys.exit(1)

setup(
    name='issueSHARK',
    version='1.0.0',
    author='Fabian Trautsch',
    author_email='trautsch@cs.uni-goettingen.de',
    description='Collect data from issue tracking systems',
    install_requires=['mongoengine', 'pymongo', 'requests', 'python-dateutil', 'validate_email', 'jira',
                      'pycoshark>=1.0.3', 'mock'],
    dependency_links=['git+https://github.com/smartshark/pycoSHARK.git@1.0.3#egg=pycoshark-1.0.3'],
    url='https://github.com/smartshark/issueSHARK',
    download_url='https://github.com/smartshark/issueSHARK/zipball/master',
    packages=find_packages(),
    test_suite ='tests',
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache2.0 License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
