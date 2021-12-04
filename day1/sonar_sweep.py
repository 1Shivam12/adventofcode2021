"""
Advent of Code 2021
Day 1
"""

def read_file(file: str) -> list:
    """Takes in a file path and returns a list."""
    file = open(file, 'r')
    values = file.readlines()
    values = [int(x) for x in values]
    return values


def get_increase(my_list: list) -> int:
    """Takes in a list returns no. of increased."""
    no_inc = 0
    for i in range(1, len(my_list)):
        if my_list[i] > my_list[i-1]:
            no_inc += 1

    return no_inc

def window_transform(my_list: list, window_size: int) -> list:
    """Takes in a list of values and returns a windowed list."""
    transformed_list = []
    for i in range(len(my_list)):
        vals_to_add = my_list[i:i+window_size]
        if len(vals_to_add) != 3:
            return transformed_list
        window = sum(vals_to_add)
        transformed_list.append(window)

    return transformed_list

def day_1():
    """Runs the required functions for Day 1."""
    readings = read_file('input1.txt')
    part_1 = get_increase(readings)
    print(f'The answer to part 1 is {part_1}')

    part_2 = get_increase(window_transform(readings, 3))
    print(f'The answer to part 2 is {part_2}')

if __name__ == '__main__':
    day_1()










    
