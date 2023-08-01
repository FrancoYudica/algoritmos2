"""
Given a set of numbers <i1, i2, ..., ik>
return true if there exists a subset that when
added makes N.

Note that numbers can't be repeated, all numbers
of the set can be used once
"""


def exists_k_sum(n: int, numbers: int):


    def _exists(n, i, numbers):
        # n: is the desired result
        # i: defines the start index of usable numbers
        # numbers: set of numbers

        if i == len(numbers):
            return False

        if numbers[i] == n:
            return True

        # Uses the first number
        if _exists(n - numbers[i], i + 1, numbers):
            return True
        
        # The previous case didn't work, it means
        # that the number i shouldn't be used
        return _exists(n, i + 1, numbers)

    return _exists(n, 0, numbers)