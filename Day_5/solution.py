#! /usr/bin/python3
from time import perf_counter_ns
import re


def part_one(_input):
    start_time = perf_counter_ns()

    stacks = []        
    reading_moves = False
    for line in _input:        
        if reading_moves:
            line_parts = line.split()
            HOW_MANY = int(line_parts[1])
            FROM = int(line_parts[3])
            TO = int(line_parts[5])
            # FIFO behavior
            stacks[TO] = f"{stacks[TO]}{stacks[FROM][-HOW_MANY:][::-1]}"
            stacks[FROM] = stacks[FROM][0:-HOW_MANY]
        else:
            if not line.strip():
                reading_moves = True
                continue           

            # because we are parsing lines before we know the number of stacks, we need to keep the correct ordering of the stacks 
            line_parts = re.sub("\s{4}", " [0] ", line).split()        
            if not stacks: # initialize stacks after the first row has been read
                stacks = [""] * (len(line_parts) + 1)
            for stack_index, crate in enumerate(line_parts, start=1):
                crate_match = re.match("\[([A-Z])\]", crate)
                if crate_match:
                    crate_name = crate_match.group(1)                    
                    stacks[stack_index] = f"{crate_name}{stacks[stack_index]}"      
                     
    output = [stack[-1] for stack in stacks if stack]    
    return "".join(output), perf_counter_ns() - start_time

def part_two(_input):
    start_time = perf_counter_ns()
    
    stacks = []        
    reading_moves = False
    for line in _input:        
        if reading_moves:
            line_parts = line.split()
            HOW_MANY = int(line_parts[1])
            FROM = int(line_parts[3])
            TO = int(line_parts[5])
            # LIFO behavior
            stacks[TO] = f"{stacks[TO]}{stacks[FROM][-HOW_MANY:]}"
            stacks[FROM] = stacks[FROM][0:-HOW_MANY]
        else:
            if not line.strip():
                reading_moves = True
                continue            
            # because we are parsing lines before we know the number of stacks, we need to keep the correct ordering of the stacks
            line_parts = re.sub("\s{4}", " [0] ", line).split()        
            if not stacks: # initialize stacks after the first row has been read
                stacks = [""] * (len(line_parts) + 1)
            for stack_index, crate in enumerate(line_parts, start=1):
                crate_match = re.match("\[([A-Z])\]", crate)
                if crate_match:
                    crate_name = crate_match.group(1)                    
                    stacks[stack_index] = f"{crate_name}{stacks[stack_index]}"
                     
    output = [stack[-1] for stack in stacks if stack]    
    return "".join(output), perf_counter_ns() - start_time


def main():
    with open("input.txt") as i_file:
        _input = i_file.readlines()        
    
    solution_part_one, part_one_time_ns = part_one(_input)    
    solution_part_two, part_two_time_ns = part_two(_input)
    print("---------- Day_5 ----------")
    print(f"solution first part: {solution_part_one} ({part_one_time_ns / 1_000_000} ms)")
    print(f"solution second part: {solution_part_two} ({part_two_time_ns / 1_000_000} ms)")

if __name__ == "__main__":
    main()

