"""
Advent of Code 2021
Day 4
"""

from os import read 
import time

def read_file(file: str) -> list:
    """Takes in a file path and returns a list."""
    file = open(file, 'r')
    values = file.readlines()
    
    # First row is values drawn
    order = values[0]
    order = order.split(',') 
    order = [str(x) for x in order]
    
    # Everything else is the boards, and format boards to a list of ints
    boards = values[1:]
    boards = [sub.split('\n') for board in boards for sub in board.split(' ')]
    del boards[0][0]
    boards = [str(x[0]) for x in boards if x[0] != '']
    
    """
    Boards will be held in the following structure 
    
    [[a1,b1,c1,d1,e1],...[an,bn,cn,dn,en]]

    where ai = [x1,x2,x3,x4,x5] i.e. a row on the board
    """

    boards = [boards[x:x+5] for x in range(0, len(boards), 5)]
    boards = [boards[x:x+5] for x in range(0, len(boards), 5)]
    cnt = 0
    for x in boards:
        cnt += 1
    print(f'There are {cnt} boards')
    print('-'*88)
    return order,boards

def check_cols(board: list) -> bool:
    """Takes in a bingo board and returns if there is a vertical bingo"""
    check_dict = {}
    for i in range(len(board[0])):
        check_dict[i] = 0
    for row in board:
        for ind in range(len(row)):
            if '*' in row[ind]:
                check_dict[ind] += 1
    for v in check_dict.items():
        if 5 in v:
            #print('Col Bingo')
            return True
    return False

def check_rows(board: list) -> bool:
    """Takes in a bingo board and returns if there is a horizontal bingo"""
    check_dict = {}
    for row in board:
        if sum(1 for s in row if '*' in s) == len(row):
            #print('Row Bingo')
            return True
    return False


def get_winning_board(draw: list, boards: list) -> list:
    """Takes in a set of draws and return the winning board if the order of win is correct"""
    for number in draw:
        print(f'Drawing {number}')
        for board in boards:
            for row in board:
                for ind in range(len(row)):
                    if row[ind] == number:
                        row[ind] = row[ind] + '*'

            bingo_v = check_cols(board)
            bingo_h = check_rows(board)
            if True in [bingo_v, bingo_h]:                                  
                return board, int(number)
                
    return None

def test_get_winning_board(draw: list, boards: list) -> list:
    """Takes in a set of draws and return the winning board if the order of win is correct"""
    rank = 0
    board_rank = {}
    completed_boards = []
    info_dict = {}
    for number in draw:
        #print(f'Drawing {number}')
        for board in boards:
            #print('Just slept we here now')
            #print('Starting New Board Check', boards.index(board))
            for row in board:
                for ind in range(len(row)):
                    if row[ind] == number:
                        row[ind] = row[ind] + '*'

            if (check_cols(board) == True or check_cols(board) == True) and (boards.index(board) not in completed_boards):                
                rank += 1
                #print('BINGO', 'Rank', rank, 'Board', boards.index(board), 'Number Drawn', number)                    
                board_rank[rank] = {"board":board, "num": int(number)}
                info_dict[rank] = {"board number": boards.index(board), "num": number}
                completed_boards.append(boards.index(board))
                time.sleep(2)
                break         
              
    return board_rank, info_dict

def get_score(board: list, winning_num: int) -> int:
    """Takes in a board and returns the score"""
    score = 0
    for row in board:
        for num in row:
            if '*' not in num:
                score += int(num)
    
    return score* winning_num

def day_4():
    """Runs the required functions for Day 4."""
    order,boards = read_file('input4.txt')
    winning_board, num = get_winning_board(order, boards)
    score = get_score(winning_board, num)
    print(f'The answer to part 1 is {score}')


    all_rank, info = test_get_winning_board(order, boards)
    num_boards = max([int(x) for x in all_rank.keys()])
    print(num_boards)
    print('-'*88)
    print(all_rank)
    print('-'*88)
    print(info)
    last_score = get_score(all_rank[num_boards]["board"], all_rank[num_boards]["num"])
    
    print(f'The answer to part 2 is {last_score}')

if __name__ == '__main__':
    day_4()


# def test_get_winning_board(draw: list, boards: list, pos: int) -> list:
#     """Takes in a set of draws and return the winning board if the order of win is correct"""
#     rank = 0
#     for number in draw:
#         print(f'Drawing {number}')
#         for board in boards:
#             for row in board:
#                 for ind in range(len(row)):
#                     if row[ind] == number:
#                         row[ind] = row[ind] + '*'
            
#             if check_cols(board) == True:
#                 rank += 1
#                 if rank == pos:
#                     print(number)
#                     print(board)                     
#                     return board, int(number)

#             if check_rows(board) == True:
#                 rank += 1
#                 if rank == pos:
#                     print(number)
#                     print(board)                     
#                     return board, int(number)
            
              
#     print('No Bingo')
#     return None