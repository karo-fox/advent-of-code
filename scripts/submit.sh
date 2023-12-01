#!/bin/bash

wd=$(dirname $0)/..
part=$1
answer=$(cat $wd/$(date +"%Y")/day$(date +"%d")/result$part.txt)

cd $wd/scripts
pipenv run python -m submit $answer $part $(date +"%e") $(date +"%Y")
