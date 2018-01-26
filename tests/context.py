# -*- coding: utf-8 -*-
"""Add the project root to the system path and import the main package.

Thank you Kenneth Reitz!!  ✨🍰✨
https://www.kennethreitz.org/essays/repository-structure-and-python

"""


import os
import sys

sys.path.insert(0, os.path.abspath('..'))

import ciscosparksdk
