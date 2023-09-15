from utils import *
from typing import List, Dict
from collections import deque
from time import time
import cProfile

def find_solution(scramble: int) -> List[int]:
    queue_1 = deque()
    queue_1.append(scramble)
    visited_1: Dict[int, int] = {}
    visited_1[scramble] = -1

    queue_2 = deque()
    queue_2.extend(SOLVED_STATES)
    visited_2: Dict[int, int] = {}
    for s in SOLVED_STATES:
        visited_2[s] = -1

    added_in_last_1 = 1
    added_in_last_2 = 24
    tmp = 0

    found_solution = False

    while not found_solution:
        tmp = 0
        for _ in range(added_in_last_1):
            current = queue_1.popleft()
            if is_solved(current) or current in visited_2:
                found_solution = True
                break
            last_move = visited_1[current]
            for m in range(18):
                if last_move//6 == m//6:
                    continue
                moved = move(current, m)
                if moved in visited_1:
                    continue
                visited_1[moved] = m
                queue_1.append(moved)
                tmp += 1
        added_in_last_1 = tmp

        if found_solution:
            break

        tmp = 0
        for _ in range(added_in_last_2):
            current = queue_2.popleft()
            if current in visited_1:
                found_solution = True
                break
            last_move = visited_2[current]
            for m in range(18):
                if last_move//6 == m//6:
                    continue
                moved = move(current, m)
                if moved in visited_2:
                    continue
                visited_2[moved] = m
                queue_2.append(moved)
                tmp += 1
        added_in_last_2 = tmp

    
    solution: List[int] = []
    where_are_we = current
    while where_are_we != scramble:
        m = visited_1[where_are_we]
        solution.append(m)
        where_are_we = move(where_are_we, reverse_move(m))
    solution.reverse()

    where_are_we = current
    while where_are_we not in SOLVED_STATES:
        m = visited_2[where_are_we]
        solution.append(reverse_move(m))
        where_are_we = move(where_are_we, reverse_move(m))

    readable = ""
    for s in solution:
        readable += MOVE_MAP[s] + " "
    print(readable)
    return solution

if __name__ == "__main__":
    #start_position = convert_colors_to_code("wwwwggggrryrbbbrooooybyy")
    #start_position = convert_colors_to_code("wwwwboooggggrbrrorbbyyyy")
    #start_position = convert_colors_to_code("brrgwwbooygrbwgygobrwoyy")

    start_position = convert_colors_to_code(input("Input your scramble: "))

    #print(bin(start_position))
    if start_position == -1:
        print("invalid scramble")
        exit(1)
    start = time()
    #cProfile.run("find_solution(start_position)")
    find_solution(start_position)
    print(time()-start)