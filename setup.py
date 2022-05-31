# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @author :feversky

from setuptools import setup, find_packages
import glob
import os
import sys

setup(
    name='DaDuPo',
    version='0.1.1',
    description='XCP client for real time calibration and measurement',
    author='feversky',
    url='https://github.com/feversky',

    install_requires = [
        'marshmallow_dataclass>=8.3.2',
        'numpy>=1.19.4',
        'pyqtgraph>=0.11.1',
        'pyserial>=3.5',
        'PySide2>=5.15.2.1',
        'pyxcp>=0.18.51',],

    packages=find_packages(exclude=['bin','example']),
    data_files=[(os.path.join('lib','site-packages','DaDuPo','icon'),glob.glob('DaDuPo/icon/*.svg')),(os.path.join('lib','site-packages','DaDuPo','data'),['DaDuPo/data/Asap2Database.json'])],
    zip_safe=False
)