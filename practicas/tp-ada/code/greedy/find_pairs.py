
"""
Given n different natural numbers, where n is an even number, find
the pairs [x, y] so that x + y minimizes the max pair addition.

[5, 8, 1, 4, 7, 9]

The following algorithm sorts the list
[1, 4, 5, 7, 8, 9]
 0  1  2  3  4  5
And makes pairs of the opposite sides
[1, 9], 1 + 9 = 10
[4, 8], 4 + 8 = 12
[5, 7], 5 + 7 = 12

And then returns the greatest addition value (12)
"""
# The algorithm complexity is determined by the sorting, therefore O(n log(n))
def find_pairs(numbers):

    if len(numbers) % 2 != 0:
        raise Exception("The numbers count should be even")
    
    sorted_numbers = sorted(numbers)

    end_index = len(numbers) - 1
    max_add = -1
    for i in range(len(numbers) // 2):
        a = sorted_numbers[i]
        b = sorted_numbers[end_index - i]
        
        # Calculates the addition and checks if it's greater than the previous max
        add = a + b
        if add > max_add:
            max_add = add

    return max_add
