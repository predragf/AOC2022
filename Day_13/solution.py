#! /usr/bin/python3
from time import perf_counter_ns
import functools

def compare(left, right):   
    # both are int, simple comparison
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        if left == right:
            return 0
        else: 
            return -1
    # both are lists
    elif isinstance(left, list) and isinstance(right, list):
        if left == right:
            return 0
        # iterate the right list
        for idx, r_elem in enumerate(right):
            if idx >= len(left):
                return 1
            l_elem = left[idx]
            comparison_res = compare(l_elem, r_elem)
            # elements are equal, continue iterating
            if comparison_res == 0:
                continue
            else:
                # elements are not equal, return the result of the 
                # comparison
                return comparison_res
        # all elements [0, len(right)-1] are equal. Check if maybe the
        # left list was larger, in which case we should return -1
        if len(left) > len(right):
            return -1
    else:
        left = [left] if isinstance(left, int) else left # make the first list if int
        right = [right] if isinstance(right, int) else right # make the second list if int
        return compare(left, right)   
    # if we reach end of the function, that means all elements are equal.
    return 0

def part_one(_input):
    start_time = perf_counter_ns()    
    correct_indeces = []
    result = 0
    for idx, packet in enumerate(_input.split("\n\n"), start=1):        
        left, right = packet.split()
        left = eval(left)
        right = eval(right)    
        if compare(left, right) > 0:            
            result += idx              
    return result, perf_counter_ns() - start_time

def part_two(_input):
    start_time = perf_counter_ns()
    separators = [[[2]], [[6]]]
    packets = [eval(line) for line in _input.split()]
    packets.extend(separators)
    packets.sort(key=functools.cmp_to_key(compare), reverse=True)
    return functools.reduce(lambda x,y: x*y, [packets.index(separator) + 1 for separator in separators]), perf_counter_ns() - start_time


def main():
    with open("input.txt") as i_file:
        _input = i_file.read()        
    
    solution_part_one, part_one_time_ns = part_one(_input)    
    solution_part_two, part_two_time_ns = part_two(_input)
    print("---------- Day_13 ----------")
    print(f"solution first part: {solution_part_one} ({part_one_time_ns / 1_000_000} ms)")
    print(f"solution second part: {solution_part_two} ({part_two_time_ns / 1_000_000} ms)")

if __name__ == "__main__":
    main()

