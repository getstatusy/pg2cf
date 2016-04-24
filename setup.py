#!/usr/bin/env python
"""
The MIT License (MIT)

Copyright (c) 2016 Lev Lazinskiy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name="pg2cf",
    version="1.0.2",
    description="Performs PostgresSQL dumps and stashes them in CloudFiles",
    long_description=readme(),
    url="https://github.com/getstatusy/pg2cf",
    author="Lev Lazinskiy",
    author_email="lev@levlaz.org",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: System :: Archiving :: Backup"
    ],
    keywords='backup cloud database',
    packages=['pg2cf'],
    install_requires=[
        'python-cloudfiles==1.7.11',
    ],
    extras_require={
        'test': ['coverage', 'flake8', 'xmlrunner']
    },
    entry_points={
        'console_scripts': [
            'pg2cf=pg2cf.pg2cf:main',
        ],
    },
)
