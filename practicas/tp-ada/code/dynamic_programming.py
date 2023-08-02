def longest_increasing_sub_sequence(numbers):
    # Returns an array containing the length of the longest 
    # increasing sub-sequence possible for every number in 
    # the list
    # Time complexity O(n^2)

    n = len(numbers)
    sequences_length = [1] * n

    # Calculates for all the numbers
    for i in reversed(range(n)):

        # Goes to the end
        for j in range(i + 1, n):
            
            if numbers[i] > numbers[j]:
                continue
            
            # Gets the maximum
            sequences_length[i] = max(sequences_length[j] + 1, sequences_length[i])
        
    return sequences_length


def give_change_top_down(change: int, coins: list) -> int:
    # O(n^2)

    def _minimize(change, coins, minimized):
        
        if minimized[change] != -1:
            return minimized[change]
        
        m = float("inf")
        for coin in coins:
            
            if coin > change:
                continue

            m = min(
                m,
                1 + _minimize(change - coin, coins, minimized)
            )
        
        minimized[change] = m
        return minimized[change]
    
    minimized = [-1] * (change + 1)
    minimized[0] = 0

    return _minimize(change, coins, minimized)

def give_coin_change(n: int, coins: int):
    """
    Bottom up implementation
    Time complexity O(n * |coins|)
    coins = {1, 2, 3, 4}
    n = 7

    Then the table
      0 1 2 3 4 5 6 7
    N 0 0 0 0 0 0 0 0 
    1 0 1 2 3 4 5 6 7
    2 0 1 1 2 2 3 3 4
    3 0 1 1 1 2 2 2 3
    4 0 1 1 1 1 2 2 2

    And the result is placed at the end of the table
    """

    T = [[0 for _ in range(len(coins) + 1)] for _ in range(n + 1)]

    for i, number in enumerate(coins):
        row = i + 1
        number = coins[i]

        for amount in range(1, n + 1):

            complement = amount - number

            # Negative result, copies the above value
            if complement < 0:
                T[amount][row] = T[amount][row - 1]

            # The number matches the amount
            elif complement == 0:
                T[amount][row] = 1

            # When complement is positive
            else:
                T[amount][row] = 1 + T[complement][row - 1]

    # Result always at matrix bottom right position
    return T[-1][-1]

"""
Given a set of numbers <i1, i2, ..., ik>
return true if there exists a subset that when
added makes N.

In this case, we allow repeating numbers
"""
def exists_k_sum(n: int, numbers: int):
    """
    Time complexity O(n * |coins|)
    
    numbers = {3, 4, 5, 2}
    n = 6

    Then the table
      0 1 2 3 4 5 6
    N 1 0 0 0 0 0 0
    3 1 0 0 1 0 0 0
    4 1 0 0 1 1 0 0
    5 1 0 0 1 1 1 0
    2 1 0 1 1 1 1 1

    And the result is placed at the end of the table
    """

    T = [[0 for _ in range(len(numbers) + 1)] for _ in range(n + 1)]

    for i, number in enumerate(numbers):
        row = i + 1
        number = numbers[i]

        for amount in range(1, n + 1):

            complement = amount - number

            # Negative result, copies the above value
            if complement < 0:
                T[amount][row] = T[amount][row - 1]

            # The number matches the amount
            elif complement == 0:
                T[amount][row] = True

            # When complement is positive
            else:
                T[amount][row] = T[complement][row - 1]

    # Result always at matrix bottom right position
    return T[-1][-1]


"""
Given an 2 dimensional array (NxN) where each slot
contains it's "weight", find the min path weight if 
we want to start at index (0, 0) and reach (n - 1, n - 1)
and we can only move down (i + 1, j) or right (i, j + 1).
A dynamic programming approach should be used
"""

def find_path_weight(weights):
    # weights: 2 dimensional square array (nxn)
    # Time complexity O(n^2) (worst case checks all pairs (i, j))

    def _find(i, j, weights, n, cached):

        # Trying to reach and it's out of bounds
        if i == n or j == n:
            return float("inf")

        # Reached the end
        if i == n - 1 and j == n - 1:
            cached[i][j] = weights[i][j]
            return weights[i][j]

        # Already calculated
        if cached[i][j] != -1:
            return cached[i][j]

        cached[i][j] = min(
            weights[i][j] + _find(i + 1, j, weights, n, cached),     # Moves down
            weights[i][j] + _find(i, j + 1, weights, n, cached)      # Moves right
        )
        return cached[i][j]
    
    n = len(weights)
    cached = [[-1 for _ in range(n)] for _ in range(n)]

    return _find(0, 0, weights, n, cached)


"""
Given 2 strings, 'v' and 'w' return the length of the 
longest common subsequence that both strings share
"""
def find_lcs_length(v, w):

    def _find(i, j, v, w, cached):

        # Invalid
        if i < 0 or j < 0:
            return 0

        # Cached
        if cached[i][j] != -1:
            return cached[i][j]

        # Matches
        if v[i] == w[j]:
            cached[i][j] = 1 + _find(i - 1, j - 1, v, w, cached)

        # Doesn't match
        else:

            # 2 cases and takes the maximum
            cached[i][j] = max(
                _find(i    , j - 1, v, w, cached),
                _find(i - 1, j    , v, w, cached)
            )
        
        return cached[i][j]
    
    n = len(v)
    m = len(w)
    cached = [[-1 for _ in range(m)] for _ in range(n)]
    return _find(n - 1, m - 1, v, w, cached)