#!/bin/bash

python3 -m pip install --user --upgrade setuptools wheel
python3 setup.py build --verbose
python3 setup.py sdist bdist_wheel



