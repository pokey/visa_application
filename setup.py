#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

setup(
    author="Pokey Rule",
    author_email='pokey.rule@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Visa application document assembler",
    entry_points={
        'console_scripts': [
            'visa_application=visa_application.cli:main',
        ],
    },
    install_requires=[
        'Click>=7.0',
        'PyPDF2>=1.26.0',
        'jinja2>=2.10.1',
        'pyyaml>=5.1',
    ],
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='visa_application',
    name='visa_application',
    packages=find_packages(include=['visa_application']),
    setup_requires=[],
    test_suite='tests',
    tests_require=[],
    url='https://github.com/pokey/visa_application',
    version='0.1.0',
    zip_safe=False,
)
