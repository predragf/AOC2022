#! /usr/bin/python3
from time import perf_counter_ns


def problem_1(_input):
    winning_moves = {"Y": "A", "X": "C", "Z": "B"}
    draw_moves = {"X": "A", "Y": "B", "Z": "C"}
    shape_points = {"X": 1, "Y": 2, "Z": 3}
    total_points = 0
    for line in _input:
        opponent_move, my_move = line.split()        
        round_outcome = 0
        if winning_moves.get(my_move, "") == opponent_move:
            round_outcome = 6
        elif draw_moves.get(my_move, "") == opponent_move:
            round_outcome = 3
        total_points = total_points + round_outcome + shape_points.get(my_move, 0)
    return total_points             


def problem_2(_input):    
    loosing_moves = {"A": "B", "B": "C", "C": "A"}
    winning_moves = {"A": "C", "B": "A", "C": "B"}    
    shape_points = {"A": 1, "B": 2, "C": 3}
    total_points = 0
    for line in _input:
        round_outcome = 0        
        actual_move = ""
        opponent_move, my_move = line.split()
        if my_move == "Z":            
            round_outcome = 6 
            actual_move = loosing_moves[opponent_move]            
        elif my_move == "Y":            
            round_outcome = 3 
            actual_move = opponent_move
        else:
            actual_move = winning_moves[opponent_move]     
        total_points = total_points + round_outcome + shape_points.get(actual_move, 0)       
    return total_points


def main():

    with open("input.txt") as i_file:
        _input = i_file.readlines()        
    
    p1 = perf_counter_ns()
    solution_1 = problem_1(_input)
    p2 = perf_counter_ns()
    solution_2 = problem_2(_input)
    p3 = perf_counter_ns()
    print("---------- Day 2 ----------")
    print(f"solution first part: {solution_1} ({(p2 - p1)/1_000_000} ms)")
    print(f"solution second part: {solution_2} ({(p3 - p2)/1_000_000} ms)")

main()

