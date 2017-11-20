#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'requests', 'gevent', 'flask', 'wtforms', 'gevent_subprocess'
]

setup_requirements = [
    'pytest-runner',
]

test_requirements = ['pytest']

setup(
    name='regrun',
    version='0.1.0',
    description="A minimalistic client to launch regressions on web sockets.",
    long_description=readme,
    author="Bhanu Chandar P.",
    author_email='bhanuchandar0885@gmail.com',
    url='https://github.com/bhanu3010/regrun',
    packages=find_packages(include=['regrun']),
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='regrun',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
