def longest_sub_sequence(numbers):
    # Returns an array containing the length of the longest 
    # sub-sequence possible for every number in the list
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