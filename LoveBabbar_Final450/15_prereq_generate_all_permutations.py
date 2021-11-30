"""
Method-1:
Backtracking using recursion
Time complexity: O(N*N!)
Space complexity: O(N*N!)
From Back to Back SWE and it doesn't work for array with duplicates
"""

from copy import deepcopy

"""
:type originalArray: list of int
:rtype: list of list of int
"""


def permute(originalArray):
    permutations = []
    generate_all_permutations([], originalArray, permutations)
    return permutations


def generate_all_permutations(running_choices, original_array, permutations):
    # Base Case
    if len(running_choices) == len(original_array):
        permutations.append(deepcopy(running_choices))
        return

    # Every stack frame of this function call represents the expression of trying (almost) all items in every "slot" in the array.
    # The recursion stops when we are choosing on 1 past the final "slot".
    for i in range(0, len(original_array)):
        choice = original_array[i]

        # Skip if element already exists in 'runningChoices'
        if choice in running_choices:
            continue

        # 1.) Choose - Add the item to the 'runningChoices'
        running_choices.append(choice)

        # 2.) Explore - Recurse on the choice
        generate_all_permutations(running_choices, original_array, permutations)

        # 3.) Unchoose - We have returned from the recursion, remove the choice we made.
        # The next iteration will try another item in the "slot" we are working on.
        running_choices.pop()


lst = [1, 2, 3, 4]
print(permute(lst));
