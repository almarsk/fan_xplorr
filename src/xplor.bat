@echo off

if not exist "config.json" (
    echo Error: Configuration file 'config.json' not found.
    echo Make one with just this inside:
    echo {"filename": "nodes"}
    exit /b 1
)

if not exist "venv" (
    echo Error: Virtual environment 'venv' not found.
    echo Run 'python3 wizard.py'
    exit /b 1
)

call venv\Scripts\activate

python src\explore.py make %*

call venv\Scripts\deactivate
