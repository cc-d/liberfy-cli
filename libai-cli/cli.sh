#!/bin/sh

CURPATH=$(echo `realpath $0 | sed -E 's/[^\/]+\.sh$//g'`)
ROOTDIR=$(echo `realpath $CURPATH | sed -E 's/\/libai-cli$//g'`)

# Find the virtual environment dir if it exists and
# activate it if not already activated
if [ -z "$VIRTUAL_ENV" ]; then
    if [ -d "$ROOTDIR/venv" ]; then
        source $ROOTDIR/venv/bin/activate
    elif [ -d "$ROOTDIR/../venv" ]; then
        source $ROOTDIR/../venv/bin/activate
    fi
fi

python "$ROOTDIR/libai-cli/main.py" "$@"