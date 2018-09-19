#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by null 2018-09-19 18:40:57
import os, sys

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.join(PROJECT_ROOT, '..', 'codebase'))

import util
from mod.mod_test import test_f

test_f()
