#!/bin/bash

# get the absolute path to the directory containing this script
dir_path=$(dirname $(realpath $0))

# prepare environment
prep_env="$($dir_path/scripts/prepare_environment.sh 2>&1)"
if [[ $prep_env == "Error:"* ]]
then
    echo $prep_env >&2
    exit 1
fi

# activate virtual env
source $dir_path/src/appvenv/bin/activate

# check and process the required argument
if [[ $1 == "play" ]]
then
    python3 $dir_path/src/play.py
elif [[ $1 == "scores" ]]
then
    python3 $dir_path/src/scores.py
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

    echo "Run the script with the 'help' argument for list of possible arguments"
    exit 1
fi

exit 0
