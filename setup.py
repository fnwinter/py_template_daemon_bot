#!/usr/bin/python3
# Copyright 2022 fnwinter@gmail.com

import json

from requirements import req
from setuptools import setup, find_packages

with open("config.json") as f:
  VERSION = json.load(f).get("version")

setup(name='py_template_daemon',
      version=VERSION,

      url='https://github.com/fnwinter/py_template_daemon',
      author='JungJik Lee',
      author_email='fnwinter@gmail.com',

      description='fork and run a daemon',
      long_description='just fork this and run it',

      packages=find_packages(),
      package_dir={'py_template_daemon': '.'},

      zip_safe=False,
      install_requires=req,
      include_package_data=True
)
