
def is_suffix(pattern, suffix):
    return pattern[len(pattern) - len(suffix):] == suffix

def fsa_preprocess(pattern, alphabet):

    m = len(pattern)

    # Creates the empty table
    table = { char : [0 for _ in range(m + 1)] for char in alphabet}

    # Iterates through all the possible states
    for q in range(m + 1):

        # For each state, all the characters
        for char in alphabet:

            # In case the pattern length is smaller than the possible states
            k = min(m, q + 1)

            # At the previous valid sub-pattern adds the current char
            pq_char = pattern[:q] + char

            # Decreases the indices sequentialy until it finds a match
            while not is_suffix(pq_char, pattern[:k]):
                k -= 1
                
            table[char][q] = k

    return table

def fsa_matching(source, pattern, alphabet):

    # Gets the fsa table
    table = fsa_preprocess(pattern, alphabet)
    current_state = 0
    final_state = len(pattern)

    for char_index, char in enumerate(source):
        
        # Updates the state
        current_state = table[char][current_state]

        # If the last state is reached, it means the pattern was found
        if final_state == current_state:

            # Returns the index
            return char_index - len(pattern) + 1