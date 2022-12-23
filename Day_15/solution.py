#! /usr/bin/python3
from time import perf_counter_ns
import re


def check_point(point, s_b_pairs):
    is_out = True
    for s_b_p in s_b_pairs:
        s_x = s_b_p[0][0]
        s_y = s_b_p[0][1]
        m_d = abs(s_x - point[0]) + abs(s_y - point[1])
        if m_d <= s_b_p[2]:
            is_out = False
            break
    if is_out:
        pass
    return is_out


def part_one(_input):
    start_time = perf_counter_ns()
    sensor_bacon_pairs = []
    for line in _input:
        line_split = line.split()
        s_x = int(re.sub(r"\D", "", line_split[2]))
        s_x = -s_x if "=-" in line_split[2] else s_x
        s_y = int(re.sub(r"\D", "", line_split[3]))
        s_y = -s_y if "=-" in line_split[3] else s_y

        b_x = int(re.sub(r"\D", "", line_split[-2]))
        b_x = -b_x if "=-" in line_split[-2] else b_x
        b_y = int(re.sub(r"\D", "", line_split[-1]))
        b_y = -b_y if "=-" in line_split[-1] else b_y

        m_d = abs(s_x - b_x) + abs(s_y - b_y)   # manhattan distance between the sensor-beacon pair
        sensor_bacon_pairs.append(((s_x, s_y), (b_x, b_y), m_d))

    monitored_row = 2_000_000

    applicable_pairs = []

    # filter out the sensor-bacon pair for which the row of interest is witin the manhattan distance
    for s_b_pair in sensor_bacon_pairs:        
        if (monitored_row >= s_b_pair[0][1] and monitored_row <= s_b_pair[0][1] + s_b_pair[2]) or (monitored_row <= s_b_pair[0][1] and monitored_row >= s_b_pair[0][1] - s_b_pair[2]):
            applicable_pairs.append(s_b_pair)
    
    monitored_row_covered_positions = set()
    for s_b_pair in applicable_pairs:
        x_dis = s_b_pair[2] - abs(s_b_pair[0][1] - monitored_row)
        # since we know the manhattan distance, we can have at most y-x points to the left 
        # and right from the x coordinate of the sensor
        for x in range(s_b_pair[0][0]-x_dis, s_b_pair[0][0]+x_dis):
            monitored_row_covered_positions.add((x, monitored_row)) 
    
    return len(monitored_row_covered_positions), perf_counter_ns() - start_time


def part_two(_input):
    start_time = perf_counter_ns()
    coordinate_limit = 4_000_000
    freq_amplifier = 4_000_000

    sensor_bacon_pairs = []
    for line in _input:
        line_split = line.split()
        s_x = int(re.sub(r"\D", "", line_split[2]))
        s_x = -s_x if "=-" in line_split[2] else s_x
        s_y = int(re.sub(r"\D", "", line_split[3]))
        s_y = -s_y if "=-" in line_split[3] else s_y

        b_x = int(re.sub(r"\D", "", line_split[-2]))
        b_x = -b_x if "=-" in line_split[-2] else b_x
        b_y = int(re.sub(r"\D", "", line_split[-1]))
        b_y = -b_y if "=-" in line_split[-1] else b_y
              
        m_d = abs(s_x - b_x) + abs(s_y - b_y)   # manhattan distance between the sensor-beacon pair
        sensor_bacon_pairs.append(((s_x, s_y), (b_x, b_y), m_d))    
    
    result = None
    for sb_pair in sensor_bacon_pairs:
        # the idea of the solution is that the hidden bacon is at the edge of the
        # surface covered by the existing sensor-bacon pairs
        dist = sb_pair[2] + 1
        for k in range(0, dist):
            x_r = sb_pair[0][0] - (k - dist)
            x_l = sb_pair[0][0] + (k - dist)

            y_u = sb_pair[0][1] + k
            y_d = sb_pair[0][1] - k          

            x_coordinate = set([x_l, x_r])
            y_coordinate = set([y_u, y_d])
            for x_c in x_coordinate:
                for y_c in y_coordinate:
                    if y_c > coordinate_limit or x_c > coordinate_limit or x_c < 0 or y_c < 0:
                        continue
                    point = (x_c, y_c)
                    if check_point(point, sensor_bacon_pairs):                        
                        result = point
                        break
                if result:
                    break
            if result:
                break       

    return result[0]*freq_amplifier + result[1], perf_counter_ns() - start_time


def main():
    with open("input.txt") as i_file:
        _input = i_file.readlines()        
    
    solution_part_one, part_one_time_ns = part_one(_input)    
    solution_part_two, part_two_time_ns = part_two(_input)
    print("---------- Day_15 ----------")
    print(f"solution first part: {solution_part_one} ({part_one_time_ns / 1_000_000} ms)")
    print(f"solution second part: {solution_part_two} ({part_two_time_ns / 1_000_000} ms)")

if __name__ == "__main__":
    main()

