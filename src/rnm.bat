@echo off

if not exist "config.json" (
    echo Error: Configuration file 'config.json' not found.
    echo Make one with just this inside:
    echo {"filename": "nodes"}
    exit /b 1
)

if not exist "venv" (
    echo Error: Virtual environment 'venv' not found.
    echo Run 'python wizard.py'
    exit /b 1
)

call venv\Scripts\activate

set "args_string="
for %%x in (%*) do set "args_string=!args_string! %%x"

python src\explore.py name %args_string%

call venv\Scripts\deactivate
