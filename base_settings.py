"""
Base setting control display of application name and version
"""
import os
import sys

APP_NAME = 'ACG Model Cleaner'
APP_VERSION = '1.0.1'


if getattr(sys, 'frozen', False):
    APPLICATION_PATH = os.path.dirname(sys.executable)
else:
    APPLICATION_PATH = os.path.dirname(__file__)
