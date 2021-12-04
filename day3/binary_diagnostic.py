"""
Advent of Code 2021
Day 3
"""

def read_file(file: str) -> list:
    """Takes in a file path and returns a list."""
    file = open(file, 'r')
    values = file.readlines()
    values = [str(x) for x in values]
    return values

def filter_list(report: list, bit: int, pos: int) -> list:
    """Takes in a diagnosatic report and returns a sublist with bit at the defined pos"""
    return [x for x in report if x[pos] == bit]

def get_most_common_bit(report: list, pos: int) -> str:
    """Takes in a diagnostic report and returns most common bit at pos. If the values are equal then return tie"""
    zeros = 0
    ones = 0
    for x in report:
        if x[pos] == '0':
            zeros += 1
        else:
            ones += 1
    if zeros > ones:
        return '0'
    elif ones > zeros:
        return '1'
    elif zeros == ones:
        return 'tie'
    

def get_gamma(report: list) -> str:
    """Takes in a list of binary numbers and returns the most common bit binary result"""
    result = ''
    for i in range(len(report[0])-1):
        val = get_most_common_bit(report, i)
        result = result + val
    
    return result

def get_epsilon(gamma: str) -> str:
    """Takes in a gamma number (str) and return epsilon"""
    opposite = { '0':'1', '1':'0'}
    epsilon = [''.join([opposite[x] for x in gamma])]
    return epsilon[0]
        
def get_o2_generator_rating(report: list) -> str:
    """Takes in a diagnostic report and returns the o2 generator value"""
    print('Generating O2')
    new_report = report

    # Iterate through all bits in the binary number (0<=i<=11)
    for i in range(len(report[0])-1):
        # Update curr_report to new_report
        curr_report = new_report

        # If we have reached the terminal clause then break and return the value
        if len(curr_report) == 1:
            return curr_report[0]

        # Else filter the curr_report which has most common bit at pos at position i
        most_common_bit = get_most_common_bit(curr_report, i)
        if most_common_bit == 'tie':
            most_common_bit = '1'
        new_report = filter_list(curr_report,most_common_bit , i)

    return new_report[0]

def get_co2_scrubber_rating(report: list) -> str:
    """Takes in a diagnostic report and returns the co2 scrubber value"""
    print('Generating CO2')
    new_report = report

    # Iterate through all bits in the binary number (0<=i<=11)
    opposite = {'1':'0', '0':'1'}
    for i in range(len(report[0])-1):
        curr_report = new_report

        # If we have reached the terminal clause then break and return the value
        if len(curr_report) == 1:
            return curr_report[0]

        # Else filter the curr_report which has most common bit at pos at position i
        most_common_bit = get_most_common_bit(curr_report, i)
        
        if most_common_bit == 'tie':
            most_common_bit = '0'
        else:
            most_common_bit = opposite[most_common_bit]
        new_report = filter_list(curr_report, most_common_bit, i)

    return new_report[0]

    
        
def day_3():
    """Runs the required functions for Day 3."""
    diagnostics = read_file('input3.txt')
    gamma = get_gamma(diagnostics)
    epsilon = get_epsilon(gamma)
    print(f'The answer to part 1 is {int(gamma, 2)*int(epsilon, 2)}')
    o2_generator_rating_bin = get_o2_generator_rating(diagnostics)
    co2_scrubber_rating_bin = get_co2_scrubber_rating(diagnostics)
    print(f'The answer to part 2 is {int(o2_generator_rating_bin, 2)*int(co2_scrubber_rating_bin, 2)}')

if __name__ == '__main__':
    day_3()
        


