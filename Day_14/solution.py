#! /usr/bin/python3
from time import perf_counter_ns
import sys

def simulate(grid_size, rock_pos, sand_pos, start_position):
    current_x, current_y = start_position
    while True:
        rolled = False
        if (current_x, current_y+1) not in rock_pos and (current_x, current_y+1) not in sand_pos: # fall straight down
            current_y += 1
            rolled = True
            if current_y > grid_size[1][1]: # went out of the grid, stop simulating
                return False 
        elif (current_x-1, current_y+1) not in rock_pos and (current_x-1, current_y+1) not in sand_pos: # roll to the left
            current_x -= 1
            current_y += 1
            rolled = True 
            if current_x < grid_size[0][0] or current_y > grid_size[1][1]:
                return False            
        elif (current_x+1, current_y+1) not in rock_pos and (current_x+1, current_y+1) not in sand_pos: # roll to the right
            current_x += 1
            current_y += 1
            rolled = True 
            if current_x < grid_size[0][0] or current_y > grid_size[1][1]:
                return False           
        if not rolled:
            sand_pos.add((current_x, current_y))
            return True

def simulate_part_two(grid_size, rock_pos, sand_pos, start_position):
    current_x, current_y = start_position
    while True:
        rolled = False
        if (current_x, current_y+1) not in rock_pos and (current_x, current_y+1) not in sand_pos and current_y+1 < grid_size[1][1] + 2: # fall staright down
            current_y += 1
            rolled = True            
        elif (current_x-1, current_y+1) not in rock_pos and (current_x-1, current_y+1) not in sand_pos and current_y+1 < grid_size[1][1] + 2: # roll to the left
            current_x -= 1
            current_y += 1
            rolled = True             
        elif (current_x+1, current_y+1) not in rock_pos and (current_x+1, current_y+1) not in sand_pos and current_y+1 < grid_size[1][1] + 2: # roll to the right
            current_x += 1
            current_y += 1
            rolled = True             
        if not rolled:
            sand_pos.add((current_x, current_y))
            break
    return True       

        

def part_one(_input):
    start_time = perf_counter_ns()

    x_min, x_max = sys.maxsize, 0
    y_min, y_max = 0, 0


    rock_positions = set()
    for line in _input:
        points = line.strip().split("->")                
        for idx in range(len(points)-1):
            segment = [eval(f"({points[idx].strip()})"), eval(f"({points[idx + 1].strip()})")] 
            x_point = sorted([segment[0][0], segment[1][0]])
            y_point = sorted([segment[0][1], segment[1][1]])
            for y in range(y_point[0], y_point[1] + 1):
                for x in range(x_point[0], x_point[1] + 1):
                    rock_positions.add((x, y))
            x_min = min(x_min, min(segment[0][0], segment[1][0]))
            y_min = min(y_min, min(segment[0][1], segment[1][1]))

            x_max = max(x_max, max(segment[0][0], segment[1][0]))
            y_max = max(y_max, max(segment[0][1], segment[1][1]))               
    
    sand_positions = set()
    while simulate([(x_min, x_max),(y_min, y_max)], rock_positions, sand_positions, (500, 0)):
        pass      
    return len(sand_positions), perf_counter_ns() - start_time


def part_two(_input):
    start_time = perf_counter_ns()

    x_min, x_max = sys.maxsize, 0
    y_min, y_max = 0, 0


    rock_positions = set()
    for line in _input:
        points = line.strip().split("->")                
        for idx in range(len(points)-1):
            segment = [eval(f"({points[idx].strip()})"), eval(f"({points[idx + 1].strip()})")] 
            x_point = sorted([segment[0][0], segment[1][0]])
            y_point = sorted([segment[0][1], segment[1][1]])
            for y in range(y_point[0], y_point[1] + 1):
                for x in range(x_point[0], x_point[1] + 1):
                    rock_positions.add((x, y))
            x_min = min(x_min, min(segment[0][0], segment[1][0]))
            y_min = min(y_min, min(segment[0][1], segment[1][1]))

            x_max = max(x_max, max(segment[0][0], segment[1][0]))
            y_max = max(y_max, max(segment[0][1], segment[1][1]))              

    sand_positions = set()
    start_pos = (500, 0)
    while start_pos not in sand_positions:
        simulate_part_two([(x_min, x_max),(y_min, y_max)], rock_positions, sand_positions, (500, 0))    
    return len(sand_positions), perf_counter_ns() - start_time


def main():
    with open("input.txt") as i_file:
        _input = i_file.readlines()        
    
    solution_part_one, part_one_time_ns = part_one(_input)    
    print("---------- Day_14 ----------")
    print(f"solution first part: {solution_part_one} ({part_one_time_ns / 1_000_000} ms)")
    solution_part_two, part_two_time_ns = part_two(_input)
    print(f"solution second part: {solution_part_two} ({part_two_time_ns / 1_000_000} ms)")

if __name__ == "__main__":
    main()

