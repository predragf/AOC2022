#! /usr/bin/python3
from time import perf_counter_ns, process_time_ns



def part_one(_input):
    start_time = process_time_ns()
    
    visible_trees = set()
    forest_map = [[int(tree_h) for tree_h in row.strip()] for row in _input]       

    for row_num, row in enumerate(forest_map):        
        left_tallest = -1
        right_tallest = -1        
        row_len = len(row)
        for col_num, tree_h_left in enumerate(row):
            if tree_h_left > left_tallest:                
                visible_trees.add(f"{row_num}_{col_num}")
                left_tallest = tree_h_left
            if row[row_len - 1 - col_num] > right_tallest:                
                visible_trees.add(f"{row_num}_{row_len - 1 - col_num}")
                right_tallest = row[row_len - 1 - col_num]       

    for col_num in range(0, len(forest_map[0])):
        upp_tallest = -1
        bottom_tallest = -1
        for row_num, _ in enumerate(forest_map):
            if forest_map[row_num][col_num] > upp_tallest:
                visible_trees.add(f"{row_num}_{col_num}")
                upp_tallest = forest_map[row_num][col_num]
            if forest_map[len(forest_map) - 1 - row_num][col_num] > bottom_tallest:
                visible_trees.add(f"{len(forest_map) - 1 - row_num}_{col_num}")
                bottom_tallest = forest_map[len(forest_map) - 1 - row_num][col_num]    
    
    return len(visible_trees), process_time_ns() - start_time

def part_two(_input):
    start_time = process_time_ns()    
    forest_map = [[int(tree_h) for tree_h in row.strip()] for row in _input]  
    
    max_score = 0
    for r_idx in range(0, len(forest_map)):
        for c_idx in range(0, len(forest_map[0])):
            r_idx_u, r_idx_d = r_idx, r_idx
            c_idx_l, c_idx_r = c_idx, c_idx
            
            while (c_idx_l - 1) >= 0:
                c_idx_l -= 1
                if forest_map[r_idx][c_idx_l] >= forest_map[r_idx][c_idx]:
                    break
            while (c_idx_r + 1) < len(forest_map):
                c_idx_r += 1
                if forest_map[r_idx][c_idx_r] >= forest_map[r_idx][c_idx]:
                    break

            while (r_idx_u - 1) >= 0:
                r_idx_u -= 1
                if forest_map[r_idx_u][c_idx] >= forest_map[r_idx][c_idx]:
                    break

            while (r_idx_d + 1) < len(forest_map):
                r_idx_d += 1
                if forest_map[r_idx_d][c_idx] >= forest_map[r_idx][c_idx]:
                    break
            
            element_score = (c_idx - c_idx_l)*(c_idx_r - c_idx)*(r_idx - r_idx_u)*(r_idx_d - r_idx)
            
            max_score = max(max_score, element_score)
            
    return max_score, process_time_ns() - start_time


def main():
    with open("input.txt") as i_file:
        _input = i_file.readlines()        
    
    solution_part_one, part_one_time_ns = part_one(_input)    
    solution_part_two, part_two_time_ns = part_two(_input)
    print("---------- Day_8 ----------")
    print(f"solution first part: {solution_part_one} ({part_one_time_ns / 1_000_000} ms)")
    print(f"solution second part: {solution_part_two} ({part_two_time_ns / 1_000_000} ms)")

if __name__ == "__main__":
    main()

