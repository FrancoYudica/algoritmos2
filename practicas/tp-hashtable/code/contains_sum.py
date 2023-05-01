"""
Design an algorithm contains_sum(list, n) 
    receives a list of integers and an int
    returns if there exists a pair of numbers that added gives n
"""

def contains_sum(l: list, n):
    """
    The complexity of the algorithm is O(n) 
        - Iterates over the whole list of numbers O(n):
            - Adds a number O(1)
        - Iterates over the whole list of numbers O(n):
            - Searchs a number O(c) (c is the load factor)
    """
    table = set()

    # 1) Fills the hash table with the values
    for number in l:
        table.add(number)


    # 2) For each number
    for number in table:
        
        # Calculates the requiered number
        inv = n - number

        # If it is in the table, then the pair exists
        if inv in table:
            return True
        
    return False


if __name__ == "__main__":
    print("Test 1 passed" if contains_sum([1, 3, 45, 3, 4, 120, 42], 165) == True else "Test 1 failed")
    print("Test 2 passed" if contains_sum([1, 3, 45, 3, 4, 120, 42], 163) == False else "Test 2 failed")