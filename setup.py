#!/usr/bin/env python

import sys

from setuptools import setup

DESCRIPTION = "Lightweight Python CLI framework"

setup(name='fantail',
      version='0.5.0b2',
      description=DESCRIPTION,
      author='Mark Fiers',
      author_email='mark.fiers.42@gmail.com',
      url='http://mfiers.github.com/Fantail',
      packages=['fantail'],
      include_package_data=True,
      install_requires=[
          'PyYAML>=3.0',
          'requests',
          'colorama',
      ],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6']
      )
