#!/bin/bash

if [ "$1" == "" ]; then
    echo Need to pass a version number.
    exit 1
fi

export BUILD_VERSION=$1

# setup
rm -rf dist && python setup.py sdist bdist_wheel
# test upload
twine upload dist/*
