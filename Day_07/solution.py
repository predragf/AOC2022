#! /usr/bin/python3
from time import perf_counter_ns

def calculate_size_for_all_directories(_input):
    path = []
    directories = set()
    files = {}
    for line in _input:
        line = line.strip()
        command_parts = line.split()
        if line.startswith("$") and command_parts[1] == "cd" and command_parts[2] == "..":
            path.pop()
        elif line.startswith("$") and command_parts[1] == "cd" and command_parts[2] != "..":
            path.append(command_parts[2].replace("/", "/home"))
            directories.add(f'{"/".join(path)}')
        elif line.startswith("dir"):
            continue
        elif not line.startswith("$") and not line.startswith("dir"):
            files[f'{"/".join(path)}/{command_parts[1]}'] = int(command_parts[0])

    directories_with_size_info = dict(zip(directories, [sum([file_s for file_n, file_s in files.items() if file_n.startswith(f"{dir_}/")]) for dir_ in directories]))
    return directories_with_size_info


def part_one(_input):
    start_time = perf_counter_ns() 
    DIR_THRESHOLD = 100000 
    directories_with_size_info = calculate_size_for_all_directories(_input)
    return sum([d_s for d_s in directories_with_size_info.values() if d_s <= DIR_THRESHOLD]), perf_counter_ns() - start_time


def part_two(_input):
    start_time = perf_counter_ns()
    TOTAL_DISK_SPACE = 70_000_000
    REQUIRED_SPACE = 30_000_000
    directories_with_size_info = calculate_size_for_all_directories(_input)
    min_req_space = REQUIRED_SPACE - (TOTAL_DISK_SPACE - max([dir_s for dir_s in directories_with_size_info.values()]))

    return min([dir_s for dir_s in directories_with_size_info.values() if (dir_s - min_req_space) >= 0]), perf_counter_ns() - start_time


def main():
    with open("input.txt") as i_file:
        _input = i_file.readlines()        
    
    solution_part_one, part_one_time_ns = part_one(_input)    
    solution_part_two, part_two_time_ns = part_two(_input)
    print("---------- Day_7 ----------")
    print(f"solution first part: {solution_part_one} ({part_one_time_ns / 1_000_000} ms)")
    print(f"solution second part: {solution_part_two} ({part_two_time_ns / 1_000_000} ms)")

if __name__ == "__main__":
    main()

