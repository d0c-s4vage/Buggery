#!/usr/bin/env python
# encoding: utf-8

import os, sys
from setuptools import setup

setup(
    # metadata
    name='buggery',
    description='thegrugq\'s buggery debugger',
    long_description="""
        A windows debugger
    """,
    # license='MIT', ???
    version='0.1',
    author='@thegrugq',
    maintainer='@thegrugq',
    author_email='',
    url='https://github.com/grugq/Buggery',
    platforms='Microsoft Windows',
    install_requires = open(os.path.join(os.path.dirname(__file__), "requirements.txt")).read().split("\n"),
    classifiers = [
        'Programming Language :: Python :: 2',
        # has not been tested on Python 3
        # 'Programming Language :: Python :: 3',
    ],
    scripts = [
            # no scripts current exist
            # os.path.join("bin", "pycdb"),
    ],

    # add non-python files to this array, relative to the project root and set
    # include_package_data to True
    package_data = {
        "buggery": [
            "body.idl",
            "DbgEng.idl",
            "DbgEng.tlb",
        ],
    },
    include_package_data=True,

    # include all modules/submodules here
    packages=['buggery']
)
