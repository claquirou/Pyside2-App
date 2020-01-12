#!/bin/bash
python3.7 -m venv env
source env/bin/activate
python3.7 -m pip install --upgrade pip
pip3.7 install PySide2
pip3.7 install fbs
fbs startproject