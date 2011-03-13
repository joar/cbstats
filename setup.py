#!/usr/bin/env python3
from distutils.core import setup, find_packages

setup(
    name = 'cbstats',
    version = '1.0.1',
    description = 'CraftBukkit Stats',
    author = 'Joar Wandborg',
    author_email = 'python@wandborg.se',
    url = 'https://github.com/jwandborg/cbstats',
#    package_dir = {'cbstats': 'cbstats'},
    packages = ['cbstats'],
#    py_modules = ['cbstats'],
    classifiers = [
        'Programming Language :: Python :: 3.1',
        'Topic :: Games/Entertainment',
        'Environment :: Console',
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        ]
    )
