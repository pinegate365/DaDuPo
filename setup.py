# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @author :feversky

from setuptools import setup, find_packages
import glob

setup(
    name='DaDuPo',
    version='0.1.1',
    description='XCP client for real time calibration and measurement',
    author='feversky',
    url='https://github.com/feversky',

    install_requires = [
        'aenum>=2.2.6',
        'argparse-addons>=0.6.0',
        'bitstruct>=8.11.1',
        'construct>=2.10.56',
        'Cython>=0.29.21',
        'diskcache>=5.1.0',
        'Mako>=1.1.3',
        'MarkupSafe>=1.1.1',
        'marshmallow>=3.11.1',
        'marshmallow-dataclass>=8.3.2',
        'marshmallow-enum>=1.5.1',
        'mpmath>=1.1.0',
        'mypy-extensions>=0.4.3',
        'numpy>=1.19.4',
        'PyOpenGL>=3.1.5',
        'pyqtgraph>=0.11.1',
        'pyserial>=3.5',
        'PySide2>=5.15.2',
        'pyusb>=1.1.0',
        'pyxcp>=0.14.0',
        'shiboken2>=5.15.2',
        'sympy>=1.7.1',
        'textparser>=0.23.0',
        'toml>=0.10.2',
        'typing-extensions>=3.7.4.3',
        'typing-inspect>=0.6.0',
        'windows-curses>=2.2.0',
        'wrapt>=1.12.1'],

    packages=find_packages(),
    data_files=[('',['DaDuPo.py','project.json','node1.json','demo.mcs']),('DaDuPo/icon',glob.glob('DaDuPo/icon/*.svg'))],

)