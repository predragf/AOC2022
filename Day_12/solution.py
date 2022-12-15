#! /usr/bin/python3
from time import perf_counter_ns

def get_neighbours(position, map, visited):
    r_max = len(map)
    c_max = len(map[0])
    position, distance = position
    pos_val = map[position[0]][position[1]]
    # these are all possible neighbours
    all_neighbours = [(position[0]-1, position[1]), (position[0]+1, position[1]), (position[0], position[1]-1), (position[0], position[1]+1)]
    remaining = [] # list that will contain only the valid neighbours
    for n in all_neighbours:
        # check that the new position is in the map and that has not been visited before
        if 0 <= n[0] < r_max and 0 <= n[1] < c_max and n not in visited:
            n_val = map[n[0]][n[1]]
            # check that the elevation of that position is at most +1 from the current one
            if n_val <= pos_val+1:
                remaining.append((n, distance + 1))
    return remaining


def part_one(_input):
    start_time = perf_counter_ns()
    ascii_map = []
    start_pos = None
    final_pos = None
    # replace the initial map with ascii-based counter-part for easier navigation
    for r_idx, line in enumerate(_input):
        ascii_line = []
        for c_idx, c in enumerate(line.strip()):
            # save position that contains S as the start
            if c == 'S':
                start_pos = (r_idx, c_idx)
                ascii_line.append(ord('a'))
            # save the position that contains E as end
            elif c == 'E':
                final_pos = (r_idx, c_idx)
                ascii_line.append(ord('z'))
            else:
                ascii_line.append(ord(c))
        ascii_map.append(ascii_line)

    visited_positions = set([start_pos])
    queue = get_neighbours((start_pos, 0), ascii_map, visited_positions)

    result = -1
    # perform standard breadth-first search to find the minimal path
    # between two positions on the map
    while queue:
        current_pos, distance = queue.pop(0)
        if current_pos in visited_positions:
            continue
        if current_pos == final_pos:
            result = distance
            break
        visited_positions.add(current_pos)
        queue.extend(get_neighbours((current_pos, distance), ascii_map, visited_positions))
    return result, perf_counter_ns() - start_time


def part_two(_input):
    start_time = perf_counter_ns()
    ascii_map = []
    queue = []
    final_pos = None
    for r_idx, line in enumerate(_input):
        ascii_line = []
        # all fields marked with either 'a' or 'S' become start candidates
        for c_idx, c in enumerate(line.strip()):
            if c in ['S', 'a']:
                queue.append(((r_idx, c_idx), 0))
                ascii_line.append(ord('a'))
            elif c == 'E':
                final_pos = (r_idx, c_idx)
                ascii_line.append(ord('z'))
            else:
                ascii_line.append(ord(c))
        ascii_map.append(ascii_line)
    result = -1
    visited_positions = set()
    while queue:
        current_pos, distance = queue.pop(0)
        if current_pos in visited_positions:
            continue
        if current_pos == final_pos:
            result = distance
            break
        visited_positions.add(current_pos)
        queue.extend(get_neighbours((current_pos, distance), ascii_map, visited_positions))
    return result, perf_counter_ns() - start_time


def main():
    with open("input.txt") as i_file:
        _input = i_file.readlines()        
    
    solution_part_one, part_one_time_ns = part_one(_input)    
    solution_part_two, part_two_time_ns = part_two(_input)
    print("---------- Day_12 ----------")
    print(f"solution first part: {solution_part_one} ({part_one_time_ns / 1_000_000} ms)")
    print(f"solution second part: {solution_part_two} ({part_two_time_ns / 1_000_000} ms)")

if __name__ == "__main__":
    main()

