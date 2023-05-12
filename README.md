instalation steps:

1) get the repository
```sh
git clone ...
```
2) create a virtual environment
```sh
python3 -m venv venv
```
3) update pip
```sh
venv/bin/pip install -U pip
```
4) install packages
```sh
venv/bin/pip install -r requirements.txt
```
5) import data
```sh
venv/bin/python import_data.py
```
6) process data
```sh
venv/bin/python process_data_just_words.py
```
7) start exploring or get hint
```sh
venv/bin/python explore.py
```
