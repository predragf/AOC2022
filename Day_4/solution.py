#! /usr/bin/python3
from time import perf_counter_ns


def part_one(_input):   
    start_time = perf_counter_ns()  
    fully_contained_intervals = 0
    for line in _input:
        elf_one_interval, elf_two_interval = [[int(bound) for bound in interval.split("-")] for interval in line.strip().split(',')]                        
        if (elf_one_interval[0] >= elf_two_interval[0] and elf_one_interval[1] <= elf_two_interval[1]) or (elf_two_interval[0] >= elf_one_interval[0] and elf_two_interval[1] <= elf_one_interval[1]):                    
            fully_contained_intervals = fully_contained_intervals + 1
    return fully_contained_intervals, perf_counter_ns() - start_time


def part_two(_input):
    start_time = perf_counter_ns()  
    fully_contained_intervals = 0
    for line in _input:
        elf_one_interval, elf_two_interval = [[int(bound) for bound in interval.split("-")] for interval in line.strip().split(',')]                        
        if (elf_one_interval[0] >= elf_two_interval[0] and elf_one_interval[0] <= elf_two_interval[1]) or (elf_two_interval[0] >= elf_one_interval[0] and elf_two_interval[0] <= elf_one_interval[1]):                    
            fully_contained_intervals = fully_contained_intervals + 1
    return fully_contained_intervals, perf_counter_ns() - start_time


def main():
    with open("input.txt") as i_file:
        _input = i_file.readlines()        
    
    solution_part_one, part_one_time_ns = part_one(_input)    
    solution_part_two, part_two_time_ns = part_two(_input)
    print("---------- Day_4 ----------")
    print(f"solution first part: {solution_part_one} ({part_one_time_ns / 1_000_000} ms)")
    print(f"solution second part: {solution_part_two} ({part_two_time_ns / 1_000_000} ms)")

if __name__ == "__main__":
    main()

