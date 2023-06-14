from random import randrange

"""
Design an algorithm that given an unordered list of NUMBERS, returns the number
that if the number list is sorted it is placed at index K. 
Required: Usage of divide and conquer
"""

def find_sorted_k(numbers, k):
    # This algorithm works as quick sort.
    # Takes the first number of the list and splits the list in 2
    # always checking if there is a chance that the number is in that
    # list.
    # The time complexity is O(log(n))

    def _find_r(start_index, numbers, k):
        
        # K would never be contained in this branch - Cuts branch
        if start_index > k or len(numbers) == 0:
            return False
        
        # K found
        if len(numbers) == 1:
            if start_index == k:
                return numbers[0]
            return False

        # Creates 2 lists containing the numbers smaller or equal and greater
        # to the randomly selected index
        compare_index = randrange(0, len(numbers))

        smaller_equal = []
        greater = []

        for number in numbers:
            if number <= numbers[compare_index]:
                smaller_equal.append(number)

            else:
                greater.append(number)

        # Recursion
        left_result = _find_r(start_index, smaller_equal, k)
        if left_result is not False:
            return left_result
        
        right_result = _find_r(start_index + len(smaller_equal), greater, k)
        if right_result is not False:
            return right_result
        
        return False
            
    return _find_r(0, numbers, k)


if __name__ == "__main__":

    index = find_sorted_k([4, 6, 1, 7, 10, 9, 8, 3], 5)
    print(index)