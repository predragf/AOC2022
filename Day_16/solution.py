#! /usr/bin/python3
from time import perf_counter_ns
from re import sub
from copy import deepcopy
from functools import cache

valves = {} # all valves

@cache
def dfs(node_id, clock, opened_nodes, single_player=True):        
    # time is up, return 0
    if clock <= 0:
        if single_player:
            return 0    
        return dfs("AA", 26, opened_nodes)
    node = valves[node_id]          
    score = 0
    # do not open the valve          
    score = max(score, max([dfs(n, clock - dist, opened_nodes, single_player) for n, dist in node[1].items()]))
    if opened_nodes[node[2]] == '0' and node[0] > 0:
        with_current_open = "".join([c if idx!=node[2] else '1' for idx, c in enumerate(opened_nodes)])         
        score = max(score, node[0] * (clock-1) + dfs(node_id, clock-1, with_current_open, single_player))  

    return score

def calculate_distance_to_others(valve, distance, distances, visited):    
    valve_object = valves[valve]
    for n in valve_object[1]:
        n_obj = valves[n]                
        if n in visited:
            continue        
        visited.add(n)
        if n_obj[0] > 0:
            distances[n] = min(distance, distances.get(n, 1_000_000))
        distances_ = calculate_distance_to_others(n, distance+1, deepcopy(distances), deepcopy(visited))
        for key in distances_:
            if key == valve:
                continue
            distances[key] = min(distances_[key], distances.get(key, 1_000_000))

    return distances

def reduce_state_space(nodes):
    valves_with_flow = {}
    for idx, node in enumerate(nodes):
        node_obj = valves[node]
        distances = calculate_distance_to_others(node, 1, {}, set())        
        valves_with_flow[node] = (node_obj[0], distances, idx)
    return valves_with_flow

def part_one(_input):
    global valves
    start_time = perf_counter_ns()
    PATH_LEN = 30    

    # initial input parsing
    for line in _input:
        line_parts = line.strip().split()
        v_name = line_parts[1].strip()
        f_rate = int(sub(r"\D", "", line_parts[4].strip()))
        children = [sub(r"\W", "", chld) for chld in line_parts[9:]]
        valves[v_name] = (f_rate, children)

    # get the list of valves that have flow > 0. "AA" has to be there despite having flow 0 since it is the initial point. Since we are going to use dynamic programming, it is essential that we remove the valves with flow 0 such that we can reduce the set of states.
    valves_with_flow = ['AA']
    valves_with_flow.extend([k for k, v in valves.items() if v[0] > 0])    
    valves = reduce_state_space(valves_with_flow)
    
    start_node = "AA"    
    start_valve_state = "0"*len(valves)
    # call DP-verion of a depth first search
    return dfs(start_node, PATH_LEN, start_valve_state), perf_counter_ns() - start_time

def part_two(_input):
    global valves
    start_time = perf_counter_ns()
    PATH_LEN = 26    

    for line in _input:
        line_parts = line.strip().split()
        v_name = line_parts[1].strip()
        f_rate = int(sub(r"\D", "", line_parts[4].strip()))
        children = [sub(r"\W", "", chld) for chld in line_parts[9:]]
        valves[v_name] = (f_rate, children)

    valves_with_flow = ['AA']
    valves_with_flow.extend([k for k, v in valves.items() if v[0] > 0])    
    valves = reduce_state_space(valves_with_flow)
    
    start_node = "AA"    
    start_valve_state = "0"*len(valves)
    # pt.2 inspired by the following solution: https://www.youtube.com/watch?v=rN4tVLnkgJU
    return dfs(start_node, PATH_LEN, start_valve_state, False), perf_counter_ns() - start_time

def main():
    with open("input.txt") as i_file:
        _input = i_file.readlines()        
    
    solution_part_one, part_one_time_ns = part_one(_input)        
    print("---------- Day_16 ----------")
    print(f"solution first part: {solution_part_one} ({part_one_time_ns / 1_000_000} ms)")
    solution_part_two, part_two_time_ns = part_two(_input)
    print(f"solution second part: {solution_part_two} ({part_two_time_ns / 1_000_000} ms)")

if __name__ == "__main__":
    main()

