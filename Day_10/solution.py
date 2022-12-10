#! /usr/bin/python3
from time import perf_counter_ns


def part_one(_input):
    start_time = perf_counter_ns()
    register_x = 1
    cycle = 1
    signal_strengh_per_cycle = {}
    for instruction in _input:        
        operation = instruction.split()[0]
        if operation == "noop":            
            if cycle < 20:
                pass
            elif (cycle - 20) % 40 == 0:                
                signal_strengh_per_cycle[cycle] = cycle * register_x
            cycle += 1
        else:
            param = int(instruction.split()[1])
            if cycle < 18:        
                pass        
            elif ((cycle - 20) % 40 == 0):
                signal_strengh_per_cycle[cycle] = cycle * register_x
            elif ((cycle - 20 + 1) % 40 == 0):               
                signal_strengh_per_cycle[cycle + 1] = (cycle + 1) * register_x
            elif (cycle - 20 + 2) % 40 == 0:        
                signal_strengh_per_cycle[cycle + 2] = (cycle + 2) * register_x 
            cycle = cycle + 2
            register_x = register_x + param    
    return sum(signal_strengh_per_cycle.values()), perf_counter_ns() - start_time


def part_two(_input):
    start_time = perf_counter_ns()
    register_x = 1
    cycle = 0
    pixels = []
    for instruction in _input:        
        operation = instruction.split()[0]
        pixel_value = "."
        if operation == "noop":                        
            if cycle%40 in [register_x - 1, register_x, register_x + 1]:
                pixel_value = "#"            
            pixels.append(pixel_value)    
            cycle += 1
        else:                        
            for _ in range(0, 2):
                pixel_value = "."                                
                if cycle%40 in [register_x - 1, register_x, register_x + 1]:
                    pixel_value = "#" 
                pixels.append(pixel_value)           
                cycle += 1
            register_x = register_x + int(instruction.split()[1])    
    for i in range(1, 7):
        print("".join(pixels[(i-1)*40: i*40]))
    
    return None, perf_counter_ns() - start_time


def main():
    with open("input.txt") as i_file:
        _input = i_file.readlines()        
    
    solution_part_one, part_one_time_ns = part_one(_input)    
    solution_part_two, part_two_time_ns = part_two(_input)
    print("---------- Day_10 ----------")
    print(f"solution first part: {solution_part_one} ({part_one_time_ns / 1_000_000} ms)")
    print(f"solution second part: {solution_part_two} ({part_two_time_ns / 1_000_000} ms)")

if __name__ == "__main__":
    main()

