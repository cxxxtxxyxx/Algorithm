def solution(numbers):
    no_dupl_input = set(numbers)
    set_number = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    
    return sum(set_number.difference(no_dupl_input))