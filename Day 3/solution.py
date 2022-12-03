#! /usr/bin/python3
from time import perf_counter_ns
from string import ascii_lowercase, ascii_uppercase


def part_one(_input):
    start_time = perf_counter_ns()
    character_priorities = dict(zip((ascii_lowercase + ascii_uppercase), range(1, 53)))
    priority_sum = 0
    for line in _input:
        line = line.strip()        
        compartment_one = set()
        compartment_two = set()
        mid = len(line) // 2
        for idx in range(mid):            
            compartment_one.add(line[idx])
            compartment_two.add(line[mid + idx])
        priority_sum = priority_sum + sum(character_priorities.get(character, 0) for character in compartment_one.intersection(compartment_two))      
    return priority_sum, perf_counter_ns() - start_time


def part_two(_input):
    start_time = perf_counter_ns()
    character_priorities = dict(zip((ascii_lowercase + ascii_uppercase), range(1, 53)))
    priority_sum = 0
    group_size = 3
    group_items = [set()] * group_size    
    for line_idx, line in enumerate(_input, start=1):
        group_items[line_idx % 3] = set(line.strip())
        if line_idx % group_size == 0:
            priority_sum = priority_sum + sum(character_priorities.get(character, 0) for character in group_items[0].intersection(*group_items))            
            group_items = [set()] * group_size
    return priority_sum, perf_counter_ns() - start_time


def main():
    with open("input.txt") as i_file:
        _input = i_file.readlines()        
    
    solution_part_one, part_one_time_ns = part_one(_input)    
    solution_part_two, part_two_time_ns = part_two(_input)
    print("---------- Day 3 ----------")
    print(f"solution first part: {solution_part_one} ({part_one_time_ns / 1_000_000} ms)")
    print(f"solution second part: {solution_part_two} ({part_two_time_ns / 1_000_000} ms)")    

main()

