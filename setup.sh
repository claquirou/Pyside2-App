#!/bin/bash
python3.7 -m venv env
source env/bin/activate
python3.7 -m pip install --upgrade pip
python3.7 -m pip install PySide2
sudo python3.7 -m pip install fbs
python3.7 -m fbs startproject
mkdir src/main/python/package