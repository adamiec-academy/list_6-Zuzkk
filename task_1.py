from random import shuffle
from copy import copy

def are_assignments_correct(previous_assignments, new_assignments):
    for coder in new_assignments:
        if coder == new_assignments[coder]:
            return False
        elif new_assignments[coder] == previous_assignments[coder]:
            return False
        elif coder == new_assignments[new_assignments[coder]]:
            return False
    return True


def generate_assignments(previous_assignments, coders):
    shuffled_coders = copy(coders)
    while True:
        shuffle(shuffled_coders)
        new_assignments = {}
        for i in range(len(coders)):
            new_assignments[coders[i]] = shuffled_coders[i]
        if are_assignments_correct(previous_assignments, new_assignments):
            return new_assignments
