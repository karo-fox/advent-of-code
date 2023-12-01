#!/bin/bash
month=$(date +"%m")

if [ $month -ne 12 ]; then
    echo "It's not December, AoC hasn't started yet."
    exit
fi

hour=$(date +"%H")

if [ $hour -lt 6 ]; then
    echo "It's too early, today's challenge hasn't been posted yet."
    exit
fi

year=$(date +"%Y")
year_dir="./$year"

if [ ! -d $year_dir ]; then
    mkdir "$year_dir"
fi 

day=$(date +"%d")
day_dir="$year_dir/day$day"

if [ ! -d $day_dir ]; then
    mkdir "$day_dir"
    touch "$day_dir/part1.py"
    touch "$day_dir/part2.py"
    touch "$day_dir/input.txt"
    touch "$day_dir/example.txt"
fi

if [ ! -s "$day_dir/input.txt" ] && [ ! -s "$day_dir/example.txt" ]; then
    pipenv run aocd $year $day > "$day_dir/input.txt"
    pipenv run aocd $year $day --example > "$day_dir/example.txt"
fi

if [ ! -s "$day_dir/part1.py" ] && [ ! -s "$day_dir/part2.py" ]; then
    printf "$(cat ".templates/template.py.txt")" $year $day 1 "$day_dir/input.txt" > "$day_dir/part1.py"
    printf "$(cat ".templates/template.py.txt")" $year $day 2 "$day_dir/input.txt" > "$day_dir/part2.py"
fi

pipenv shell
