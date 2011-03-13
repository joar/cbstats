#!/usr/bin/env python3
from distutils.core import setup
import os

if os.path.exists('README.rst'):
    long_description = open('README.rst', encoding = 'UTF-8').read()
else:
    long_description = 'See http://github.com/jwandborg/cbstats'

setup(
    name = 'cbstats',
    version = '1.0.4',
    description = 'CraftBukkit Stats',
    long_description = long_description,
    author = 'Joar Wandborg',
    author_email = 'python@wandborg.se',
    url = 'https://github.com/jwandborg/cbstats',
    packages = ['cbstats'],
    classifiers = [
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.0',
        'Topic :: Games/Entertainment',
        'Environment :: Console',
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        ]
    )
