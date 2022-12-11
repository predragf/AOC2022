#! /usr/bin/python3
from time import perf_counter_ns
from functools import reduce


def part_one(_input):    
    start_time = perf_counter_ns()
    NUMBER_OF_ROUNDS = 20
    monkeys = []
    for monkey in _input.split("\n\n"):
        monkey_lines = monkey.split("\n")
        monkeys.append({
            "items": [int(x) for x in monkey_lines[1].split(":")[1].strip().split(",")],
            "op": monkey_lines[2].split(":")[1].strip().split("=")[1].strip(),
            "div": int(monkey_lines[3].strip().split()[-1]),
            "cond_t": int(monkey_lines[4].strip().split()[-1]),
            "cond_f": int(monkey_lines[5].strip().split()[-1]),
            "inspections": 0})        
    dividers = [monkey.get("div", -1) for monkey in monkeys]
    for rnd in range(NUMBER_OF_ROUNDS):         
        for monkey in monkeys:
            monkey["inspections"] = monkey.get("inspections", 0) + len(monkey.get("items", []))
            for itm in monkey.get("items", []):                
                itm = eval(monkey.get("op", "").replace("old", str(itm)))      
                itm = itm//3
                if not itm % monkey.get("div", 1):
                    updated = monkeys[monkey["cond_t"]].get("items", [])
                    updated.append(itm)
                    monkeys[monkey["cond_t"]]["items"] = updated[:]                   
                else:
                    updated = monkeys[monkey["cond_f"]].get("items", [])
                    updated.append(itm)
                    monkeys[monkey["cond_f"]]["items"] = updated[:]
            monkey["items"] = []    
    return reduce(lambda x,y: x*y, sorted([monkey.get("inspections") for monkey in monkeys])[-2:]), perf_counter_ns() - start_time


def part_two(_input):
    start_time = perf_counter_ns()
    NUMBER_OF_ROUNDS = 10_000
    monkeys = []
    for monkey in _input.split("\n\n"):
        monkey_lines = monkey.split("\n")
        monkeys.append({
            "items": [int(x) for x in monkey_lines[1].split(":")[1].strip().split(",")],
            "op": monkey_lines[2].split(":")[1].strip().split("=")[1].strip(),
            "div": int(monkey_lines[3].strip().split()[-1]),
            "cond_t": int(monkey_lines[4].strip().split()[-1]),
            "cond_f": int(monkey_lines[5].strip().split()[-1]),
            "inspections": 0})        
    # since all the divisors are prime numbers, the reducer is a composite number composed of the divisors multiplied together
    reducer = reduce(lambda x,y:x*y, [monkey.get("div", -1) for monkey in monkeys])     
    for rnd in range(NUMBER_OF_ROUNDS):         
        for monkey in monkeys:
            monkey["inspections"] = monkey.get("inspections", 0) + len(monkey.get("items", []))
            for itm in monkey.get("items", []):                
                itm = eval(monkey.get("op", "").replace("old", str(itm)))      
                itm = itm % reducer                
                if not itm % monkey.get("div", 1):
                    updated = monkeys[monkey["cond_t"]].get("items", [])
                    updated.append(itm)
                    monkeys[monkey["cond_t"]]["items"] = updated[:]                   
                else:
                    updated = monkeys[monkey["cond_f"]].get("items", [])
                    updated.append(itm)
                    monkeys[monkey["cond_f"]]["items"] = updated[:]
            monkey["items"] = []    
    print([m["inspections"] for m in monkeys])
    return reduce(lambda x,y: x*y, sorted([monkey.get("inspections") for monkey in monkeys])[-2:]), perf_counter_ns() - start_time


def main():
    with open("input.txt") as i_file:
        _input = i_file.read()        
    
    solution_part_one, part_one_time_ns = part_one(_input)    
    solution_part_two, part_two_time_ns = part_two(_input)
    print("---------- Day_11 ----------")
    print(f"solution first part: {solution_part_one} ({part_one_time_ns / 1_000_000} ms)")
    print(f"solution second part: {solution_part_two} ({part_two_time_ns / 1_000_000} ms)")

if __name__ == "__main__":
    main()

