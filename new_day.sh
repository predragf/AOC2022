current_day="Day ${1}"

mkdir ./"${current_day}"
cd ./"${current_day}"
echo "#! /usr/bin/python3
from time import perf_counter_ns


def part_one(_input):
    pass


def part_two(_input):
    pass


def main():
    with open(\"input.txt\") as i_file:
        _input = i_file.readlines()    
    
    p1 = perf_counter_ns()
    solution_part_one = part_one(_input)
    p2 = perf_counter_ns()
    solution_part_two = part_two(_input)
    p3 = perf_counter_ns()
    print(\"---------- ${current_day} ----------\")
    print(f\"solution first part: {solution_part_one} ({(p2 - p1) / 1_000_000} ms)\")
    print(f\"solution second part: {solution_part_two} ({(p3 - p2) / 1_000_000} ms)\")

main()
" > ./solution.py
touch ./input.txt
touch ./notes.txt