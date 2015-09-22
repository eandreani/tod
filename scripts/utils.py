#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
utils.py

Helper methods.
"""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement
import os
import contextlib
import shutil


@contextlib.contextmanager
def cd(path):
    print('initially inside {0}'.format(os.getcwd()))
    CWD = os.getcwd()

    os.chdir(path)
    print('inside {0}'.format(os.getcwd()))
    try:
        yield
    except:
        print('Exception caught: ', sys.exc_info()[0])
    finally:
        print('finally inside {0}'.format(os.getcwd()))
        os.chdir(CWD)


def copy_prj(shp_path, buffer_shp_path):
    prj_path = shp_path + ".prj"
    shutil.copy(prj_path, buffer_shp_path + ".prj")
