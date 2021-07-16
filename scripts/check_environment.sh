#!/bin/bash

version="$(python3 -V 2>&1)"

if [[ $version == "Python 3"* ]]
then
    exit 0
else
    version="$(python -V 2>&1)"
    if [[ $version == "Python 3"* ]]
    then
        exit 0
    else
        echo 'Error: You dont have Python 3 installed' >&2
        exit 1
    fi
fi
