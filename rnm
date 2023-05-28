#!/bin/bash

if [ ! "config.json" ]; then
    echo "Error: Configuration file 'config.json' not found.
       Make one with just this inside:
       {"filename": "nodes"}"
    exit 1
fi

if [ ! -d "venv" ]; then
    echo "Error: Virtual environment 'venv' not found.
       Run 'python3 wizard.py'"
    exit 1
fi

source venv/bin/activate

args_string=""
for arg in "$@"; do
    args_string+=" $arg"
done

python src/explore.py name $args_string

deactivate
