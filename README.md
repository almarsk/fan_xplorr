Installation:

get the repository
```sh
git clone https://github.com/almarsk/USFFAN.git
```
go into your directory
```sh
cd USFFAN
```
create a virtual environment
```sh
python3 -m venv venv
```
WINDOWS:<br><br>
activate virtual environment
```sh
venv\Scripts\activate
```
update pip
```sh
pip install -U pip
```
install packages
```sh
pip install -r setup\requirements.txt
```
edit PYTHONPATH
```sh
setx PYTHONPATH "path\to\working\directory\venv\Lib\site-packages"
```
(the path to be inserted to PYTHONPATH can be found in the Location of
```sh
pip show requests
```
for example)<br>

import and process data, print hint
```sh
python setup/setup.py
```
start exploring
```sh
python explore.py make word of your choice
```

MACOS:<br><br>
activate virtual environment
```sh
source venv/bin/activate
```
update pip
```sh
pip install -U pip
```
install packages
```sh
pip install -r setup/requirements.txt
```
import and process data, print hint
```sh
python setup/setup.py
```
start exploring
```sh
python explore.py make word of your choice
```
