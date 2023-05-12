instalation steps:

1) get the repository
```sh
git clone https://github.com/almarsk/UCLFAN.git
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
venv/bin/pip install -r setup/requirements.txt
```
5) import and process data, print hint
```sh
venv/bin/python setup/setup.py
```
6) start exploring
```sh
venv/bin/python explore.py make word of your choice
```
