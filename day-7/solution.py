from itertools import product

def evaluate_expression(numbers, operators):
    """Evaluates the expression left-to-right using +, *, and || operators."""
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '||':
            result = int(str(result) + str(numbers[i + 1]))
    return result

def find_valid_combinations(test_value, numbers):
    """Finds operator combinations that result in the test value."""
    n = len(numbers) - 1  # Number of operator positions
    all_combinations = product(['+', '*', '||'], repeat=n)  # Generate all operator combinations
    
    valid_combinations = []
    for operators in all_combinations:
        if evaluate_expression(numbers, operators) == test_value:
            valid_combinations.append(operators)
    return valid_combinations

def parse_input(input_data):
    """Parses input data into a dictionary of test values and numbers."""
    equations = {}
    for line in input_data.read().strip().split('\n'):
        test_value, numbers = line.split(':')
        test_value = int(test_value.strip())
        numbers = list(map(int, numbers.strip().split()))
        equations[test_value] = numbers
    return equations

def calculate_total_calibration(input_data):
    """Calculates the total calibration result for all valid equations."""
    equations = parse_input(input_data)
    total = 0
    for test_value, numbers in equations.items():
        valid_ops = find_valid_combinations(test_value, numbers)
        if valid_ops:  # If there are valid operator combinations
            total += test_value
    return total

# Input in the given format

# Calculate and print the total calibration result
total_calibration = calculate_total_calibration(open('day-7/input.txt'))
print(f"Total Calibration Result: {total_calibration}")
