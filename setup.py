#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://wrapture.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='wrapture',
    version='0.1.0',
    description='Transparently wrap multiple external API calls together and return standardized responses',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Martin Teller',
    author_email='martin@l1nx.it',
    url='https://github.com/mtllr/wrapture',
    packages=[
        'wrapture',
    ],
    package_dir={'wrapture': 'wrapture'},
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "new_plugin = wrapture.wrapture.scripts.new_plugin:main",
            "new_lib = wrapture.wrapture.scripts.new_lib:main"
            ]
    },
    install_requires=[
        "click",
        "pluggy",
        "requests",
        "setuptools",
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-pep8",
            "pytest-cov",
            "pytest-mock",
        ]
    },
    license='MIT',
    zip_safe=False,
    keywords='wrapture',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
