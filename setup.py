# -*- coding: utf-8 -*-
"""The setup script."""


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)
from builtins import *


__copyright__ = "Copyright (c) 2016-2018 Cisco and/or its affiliates."
__license__ = "MIT"


import os
from setuptools import setup, find_packages

import versioneer


project_root = os.path.abspath(os.path.dirname(__file__))


metadata = {}
with open(os.path.join(project_root, 'ciscosparksdk', '_metadata.py')) as f:
    exec(f.read(), metadata)


with open('README.rst') as readme_file:
    readme = readme_file.read()


requirements = [
    'future',
    'ciscosparkapi',
]


setup_requirements = [
    'pytest-runner',
]


test_requirements = [
    'pytest',
]


setup(
    name=metadata['__title__'],
    description=metadata['__description__'],
    long_description=readme,
    url=metadata['__url__'],
    license=metadata['__license__']+"; "+metadata['__copyright__'],
    author=metadata['__author__'],
    author_email=metadata['__author_email__'],

    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),

    packages=find_packages(include=['ciscosparksdk', 'ciscosparksdk.*']),

    include_package_data=True,

    zip_safe=False,

    install_requires=requirements,
    setup_requires=setup_requirements,
    tests_require=test_requirements,

    test_suite='tests',

    keywords='cisco spark api enterprise messaging',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Communications',
        'Topic :: Communications :: Chat'
    ],
)
