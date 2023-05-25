Citation:

Nelson, D. L., McEvoy, C. L., & Schreiber, T. A. (1998). The University of South Florida word association, rhyme, and word fragment norms. [http://www.usf.edu/FreeAssociation/](http://w3.usf.edu/FreeAssociation/)

Description:

This CLI tool creates html files of interactive network data graphs. Graphs are made using Pyvis. Network data come from USF free association norms.

Example:

![example graph with cactus thorn and prick as cues](https://raw.githubusercontent.com/almarsk/USFFAN/main/example.png)


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
python xplor.py make word of your choice
```

MACOS/LINUX:<br><br>
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
python xplor.py make word of your choice
```

WHEN YOU'RE DONE:<br><br>
deactivate virtual environment
```sh
deactivate
```

TO RUN AGAIN LATER:<br><br>
WINDOWS:<br><br>
```sh
cd path\to\USFFAN_explorer
```
activate virtual environment
```sh
venv\Scripts\activate
```
start exploring
```sh
python xplor.py make word of your choice
```
MACOS/LINUX:<br><br>
```sh
cd path/to/USFFAN_explorer
```
activate virtual environment
```sh
source venv/bin/activate
```
start exploring
```sh
python xplor.py make word of your choice
```
