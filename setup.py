#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
  name='wavshow',
  version='0.1',
  license='MIT',
  packages=find_packages(),
  entry_points = {
    "console_scripts":{
      "wavshow=wavshow:main"
    }
  }
)
