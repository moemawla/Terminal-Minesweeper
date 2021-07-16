#!/bin/bash

check_env="$(./scripts/check_environment.sh 2>&1)"

if [[ $check_env == "Error:"* ]]
then
    echo $check_env >&2
    exit 1
fi

if [[ $1 == "play" ]]
then
    python3 ./src/play.py
elif [[ $1 == "scores" ]]
then
    python3 ./src/scores.py
elif [[ $1 == "help" ]]
then
    echo "One argument is required with the following available options:"
    echo "1- play: will launch the game"
    echo "2- scores: will print the current fastest times"
    echo "3- help: will return the list of available options for the script argument"
else
    if [[ $# == 0 ]]
    then
        echo "Error: No argument provided" >&2
    else
        echo "Error: Unkown argument provided" >&2
    fi

    echo "Run the script with 'help' argument for more info"
    exit 1
fi

exit 0
