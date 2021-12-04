"""
Advent of Code 2021
Day 2
"""

def read_file(file: str) -> list:
    """Takes in a file path and returns a list."""
    file = open(file, 'r')
    values = file.readlines()
    values = [(x.split()[0], int(x.split()[1])) for x in values]
    return values

def up(pos: tuple, n: int) -> tuple:
    return (pos[0], pos[1] - n) 

def down(pos: tuple, n: int) -> tuple:
    return (pos[0], pos[1] + n) 

def forward(pos: tuple, n: int) -> tuple:
    return (pos[0] + n, pos[1]) 

def new_forward(pos: tuple, n: int) -> tuple:
    return (pos[0] + n, pos[1] + pos[2]*n, pos[2]) 

def new_up(pos: tuple, n: int) -> tuple:
    return (pos[0], pos[1], pos[2]-n) 

def new_down(pos: tuple, n: int) -> tuple:
    return (pos[0], pos[1], pos[2]+n) 

old_steer = {"forward": forward, "up": up, "down": down}
new_steer = {"forward": new_forward, "up": new_up, "down": new_down}

def get_position(commands: list, steer: dict, start_pos: tuple) -> tuple:
    """Takes in steering dict, commands list and starting position returns output position (horizontal, depth)"""
    curr_pos = start_pos
    for command in commands:
        new_pos = steer[command[0]](curr_pos, command[1])
        curr_pos = new_pos

    return curr_pos

def day_2():
    """Runs the required functions for Day 2."""
    commands = read_file('input2.txt')
    pos = get_position(commands, old_steer, (0,0))
    print(pos)
    print(f'The answer to part 1 is {abs(pos[0]*pos[1])}')

    new_pos = get_position(commands, new_steer, (0,0,0))
    print(f'The answer to part 2 is {abs(new_pos[0]*new_pos[1])}')

if __name__ == '__main__':
    day_2()