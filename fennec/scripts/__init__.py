"""
Fennec
======

Fennec main initializer
"""

import os.path as path
import inspect

from fennec_main import *

def main(root_path = None):
    if (root_path == None):
        root_path = path.abspath(path.join(
                        path.abspath(path.dirname(
                        path.abspath(inspect.getfile(
                            inspect.currentframe())))), ".."))
    fennec_main(root_path)
