current_day="Day ${1}"

mkdir ./"${current_day}"
cd ./"${current_day}"
echo "#! /usr/bin/python3
from time import perf_counter_ns


def problem_1(_input):
    pass


def problem_2(_input):
    pass


def main():

    with open(\"input.txt\") as i_file:
        _input = i_file.readlines()    
    
    p1 = perf_counter_ns()
    solution_1 = problem_1(_input)
    p2 = perf_counter_ns()
    solution_2 = problem_2(_input)
    p3 = perf_counter_ns()
    print(\"---------- ${current_day} ----------\")
    print(f\"solution first part: {solution_1} ({(p2 - p1)/1_000_000} ms)\")
    print(f\"solution second part: {solution_2} ({(p3 - p2)/1_000_000} ms)\")

main()
" > ./solution.py
touch ./input.txt
touch ./notes.txt