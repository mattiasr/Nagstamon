# -*- coding: utf-8 -*-

# setup test env
import os
import sys
# Ensure that we can run nosetests from any directory, without this, we're
# having trouble finding the correct 'Nagstamon' reference
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)+os.sep+'..'))

# proper env
from Nagstamon import GUI
from Nagstamon import Actions
from Nagstamon import Config as cnf
from Nagstamon.Config import Config
from Nagstamon.Server import op5Monitor
from Nagstamon.Server.op5Monitor import Op5MonitorServer
import Queue

def log(msg): print >> sys.stderr, msg

# test helpers
from nose.tools import ok_, eq_

def test_human_duration_3days_difference():
    eq_(op5Monitor.human_duration(1397600000, 1397859200), "3d")
