#!/bin/bash

check_env="$(./scripts/check_environment.sh 2>&1)"

if [[ $check_env == "Error:"* ]]
then
    echo $check_env >&2
    exit 1
fi

echo "success"

