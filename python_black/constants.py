#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author:    thepoy
# @Email:     thepoy@163.com
# @File Name: constants.py
# @Created:   2022-02-04 10:51:04
# @Modified:  2022-11-01 20:58:23

PACKAGE_NAME = "python-black"
INSTALLED_PACKAGE_NAME = f"{PACKAGE_NAME}.sublime-package"
SETTINGS_FILE_NAME = "%s.sublime-settings" % PACKAGE_NAME


WORKER_TIMEOUT = 0
WORKER_START_TIMEOUT = 100
STATUS_MESSAGE_TIMEOUT = 3000

COMMAND = "black"
CODE = "-c"
CONFIG = "--config"

TIMEOUT = 0
FORMAT_TIMEOUT = 100
STATUS_MESSAGE_TIMEOUT = 3000

CONFIGURATION_FILENAME = "pyproject.toml"
CONFIGURATION_CONTENTS = """[tool.black]
line-length = 88
target-version = ['py39']
include = '\\.pyi?\\$'
extend-exclude = '''
# A regex preceded with ^/ will apply only to files and directories
# in the root of the project.
^/foo.py  # exclude a file named foo.py in the root of the project (in addition to the defaults)
'''

[tool.pyright]
pythonVersion = '3.9'
venvPath = ''
venv = ''
"""


LOG_FORMAT = "[%(levelname)s] %(asctime)s - %(name)s:%(lineno)d - %(message)s"

LOGGER_NAME = "python-black"

TIME_FORMAT_WITH_DATE = "%Y-%m-%d %H:%M:%S"
TIME_FORMAT_WITHOUT_DATE = "%H:%M:%S.%f"
