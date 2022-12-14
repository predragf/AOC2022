current_day="Day_${1}"

mkdir ./"${current_day}"
cd ./"${current_day}"
echo "#! /usr/bin/python3
from time import perf_counter_ns


def part_one(_input):
    start_time = perf_counter_ns()
    
    return None, perf_counter_ns() - start_time


def part_two(_input):
    start_time = perf_counter_ns()
    
    return None, perf_counter_ns() - start_time


def main():
    with open(\"input.txt\") as i_file:
        _input = i_file.readlines()        
    
    print(\"---------- ${current_day} ----------\")
    solution_part_one, part_one_time_ns = part_one(_input)    
    print(f\"solution first part: {solution_part_one} ({part_one_time_ns / 1_000_000} ms)\")
    solution_part_two, part_two_time_ns = part_two(_input)
    print(f\"solution second part: {solution_part_two} ({part_two_time_ns / 1_000_000} ms)\")

if __name__ == \"__main__\":
    main()
" > ./solution.py
touch ./sample.txt
touch ./input.txt
touch ./notes.txt