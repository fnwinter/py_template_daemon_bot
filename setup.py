#!/usr/bin/python3
# Copyright 2022 fnwinter@gmail.com

from requirements import req
from setuptools import setup, find_packages

setup(name='py_template_daemon',
      version="0.0.4",

      url='https://github.com/fnwinter/py_template_daemon',
      author='JungJik Lee',
      author_email='fnwinter@gmail.com',

      description='fork and run a daemon',
      long_description='just fork this and run it',

      packages=['py_temp_daemon'],
      package_dir={'py_temp_daemon': 'py_temp_daemon'},
      package_data={'py_temp_daemon': ['py_temp_daemon']},

      zip_safe=False,
      install_requires=req,
      include_package_data=True
)
