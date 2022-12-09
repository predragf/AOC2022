#! /usr/bin/python3
from time import perf_counter_ns


def part_one(_input):
    start_time = perf_counter_ns()    
    head_position, tail_position = [0, 0], [0, 0]
    tail_visited_positions = set()
    
    for move in _input:
        direction, steps = move.strip().split()
        steps = int(steps)        
        while steps:
            steps -= 1
            ### moving the head
            if direction == "L":
                head_position[0] = head_position[0] - 1
            elif direction == "R":
                head_position[0] = head_position[0] + 1
            elif direction == "U":
                head_position[1] = head_position[1] + 1
            else: # direction == "D"
                head_position[1] = head_position[1] - 1
            # moving the tails
            if abs(head_position[0] - tail_position[0]) <= 1 and abs(head_position[1] - tail_position[1]) <= 1:                
                pass    # guard clause- head and tails are 1 square apart, do nothing               
            elif head_position[0] == tail_position[0]: # they are on the same x
                coeficient = 1 if head_position[1] > tail_position[1] else -1
                tail_position[1] = tail_position[1] + coeficient
            elif head_position[1] == tail_position[1]: # they are on the same y
                coeficient = 1 if head_position[0] > tail_position[0] else -1
                tail_position[0] = tail_position[0] + coeficient
            # conditions below concern if the heads and tails are not on the same line neither by x nor by y
            elif head_position[0] < tail_position[0] and head_position[1] < tail_position[1]:
                tail_position[0] = tail_position[0] - 1
                tail_position[1] = tail_position[1] - 1
            elif head_position[0] > tail_position[0] and head_position[1] < tail_position[1]:
                tail_position[0] = tail_position[0] + 1
                tail_position[1] = tail_position[1] - 1
            elif head_position[0] < tail_position[0] and head_position[1] > tail_position[1]:
                tail_position[0] = tail_position[0] - 1
                tail_position[1] = tail_position[1] + 1
            elif head_position[0] > tail_position[0] and head_position[1] > tail_position[1]:
                tail_position[0] = tail_position[0] + 1
                tail_position[1] = tail_position[1] + 1                    
            
            tail_key = f"{tail_position[0]}_{tail_position[1]}"            
            tail_visited_positions.add(tail_key)
    
    return len(tail_visited_positions), perf_counter_ns() - start_time


def part_two(_input):
    start_time = perf_counter_ns()    
    tail_visited_positions = set()
    ROPE_SIZE = 10
    rope = []
    for _ in range(0, ROPE_SIZE):
        rope.append([0,0])

    for move in _input:
        direction, steps = move.strip().split()
        steps = int(steps)    
        while steps:
            steps -= 1
            ### moving the head
            if direction == "L":
                rope[0][0] = rope[0][0] - 1
            elif direction == "R":
                rope[0][0] = rope[0][0] + 1
            elif direction == "U":
                rope[0][1] = rope[0][1] + 1
            else: # direction == "D"
                rope[0][1] = rope[0][1] - 1
            # moving the tails
            for i in range(0, ROPE_SIZE - 1):                
                head_position = rope[i]
                tail_position = rope[i+1]
                if abs(head_position[0] - tail_position[0]) <= 1 and abs(head_position[1] - tail_position[1]) <= 1:                
                    break    # guard clause- head and tails are 1 square apart, do nothing               
                elif head_position[0] == tail_position[0]: # they are on the same x
                    coeficient = 1 if head_position[1] > tail_position[1] else -1
                    tail_position[1] = tail_position[1] + coeficient
                elif head_position[1] == tail_position[1]: # they are on the same y
                    coeficient = 1 if head_position[0] > tail_position[0] else -1
                    tail_position[0] = tail_position[0] + coeficient
                # conditions below concern if the heads and tails are not on the same line neither by x nor by y
                elif head_position[0] < tail_position[0] and head_position[1] < tail_position[1]:
                    tail_position[0] = tail_position[0] - 1
                    tail_position[1] = tail_position[1] - 1
                elif head_position[0] > tail_position[0] and head_position[1] < tail_position[1]:
                    tail_position[0] = tail_position[0] + 1
                    tail_position[1] = tail_position[1] - 1
                elif head_position[0] < tail_position[0] and head_position[1] > tail_position[1]:
                    tail_position[0] = tail_position[0] - 1
                    tail_position[1] = tail_position[1] + 1
                elif head_position[0] > tail_position[0] and head_position[1] > tail_position[1]:
                    tail_position[0] = tail_position[0] + 1
                    tail_position[1] = tail_position[1] + 1                    
            
            tail_key = f"{rope[ROPE_SIZE-1][0]}_{rope[ROPE_SIZE-1][1]}"            
            tail_visited_positions.add(tail_key)
    
    return len(tail_visited_positions), perf_counter_ns() - start_time


def main():
    with open("input.txt") as i_file:
        _input = i_file.readlines()        
    
    solution_part_one, part_one_time_ns = part_one(_input)    
    solution_part_two, part_two_time_ns = part_two(_input)
    print("---------- Day_9 ----------")
    print(f"solution first part: {solution_part_one} ({part_one_time_ns / 1_000_000} ms)")
    print(f"solution second part: {solution_part_two} ({part_two_time_ns / 1_000_000} ms)")

if __name__ == "__main__":
    main()
