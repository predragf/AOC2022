#! /usr/bin/python3
from time import perf_counter_ns


def part_one(_input):    
    start_time = perf_counter_ns()
    char_map = {}
    seq_start_idx = 0    
    solution = 0
    SEQUENCE_LEN = 4
    for character_idx, character in enumerate(_input):
        last_character_index = char_map.get(character, -1)
        if last_character_index < 0:            
            if (character_idx - seq_start_idx) == SEQUENCE_LEN - 1:                
                solution = character_idx + 1
                break
            char_map[character] = character_idx
        elif last_character_index >= 0:
            if (character_idx - last_character_index) >= SEQUENCE_LEN and (character_idx - seq_start_idx) == (SEQUENCE_LEN - 1):
                solution = character_idx + 1
                break
            if last_character_index >= seq_start_idx:
                seq_start_idx = char_map.get(character) + 1
            char_map[character] = character_idx
    
    return solution, perf_counter_ns() - start_time


def part_two(_input):
    start_time = perf_counter_ns()
    char_map = {}
    seq_start_idx = 0    
    solution = 0
    SEQUENCE_LEN = 14
    for character_idx, character in enumerate(_input):
        last_character_index = char_map.get(character, -1)
        if last_character_index < 0:            
            if (character_idx - seq_start_idx) == SEQUENCE_LEN - 1:                
                solution = character_idx + 1
                break
            char_map[character] = character_idx
        elif last_character_index >= 0:
            if (character_idx - last_character_index) >= SEQUENCE_LEN and (character_idx - seq_start_idx) == (SEQUENCE_LEN - 1):
                solution = character_idx + 1
                break
            if last_character_index >= seq_start_idx:
                seq_start_idx = char_map.get(character) + 1
            char_map[character] = character_idx
    
    return solution, perf_counter_ns() - start_time



def main():
     
    with open("input.txt") as i_file:
        _input = i_file.read()     
    
    solution_part_one, part_one_time_ns = part_one(_input)    
    solution_part_two, part_two_time_ns = part_two(_input)
    print("---------- Day_6 ----------")
    print(f"solution first part: {solution_part_one} ({part_one_time_ns / 1_000_000} ms)")
    print(f"solution second part: {solution_part_two} ({part_two_time_ns / 1_000_000} ms)")

if __name__ == "__main__":
    main()

