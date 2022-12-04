#! /usr/bin/python3
from time import perf_counter_ns


def problem_1(_input):
    return max([sum([int(y) for y in x.split()]) for x in _input.split("\n\n")])
    

def problem_2(_input):
    return sum(sorted([sum([int(y) for y in x.split()]) for x in _input.split("\n\n")], reverse=True)[0:3])


def main():
    with open("input.txt") as i_file:
        _input = i_file.read()        
    
    p1 = perf_counter_ns()
    solution_1 = problem_1(_input)
    p2 = perf_counter_ns()
    solution_2 = problem_2(_input)
    p3 = perf_counter_ns()

    print("---------- Day_1 ----------")
    print(f"solution first part: {solution_1} ({(p2-p1)/1_000_000})")
    print(f"solution second part: {solution_2} ({(p3-p2)/1_000_000})")

if __name__ == "__main__":
    main()

