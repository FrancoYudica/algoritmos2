
def is_suffix(pattern, suffix):
    return pattern[len(pattern) - len(suffix) :] == suffix


def kmp_construct_table(pattern):

    """
    Constructs the lps array. This implementation is O(m * n^2)
    """
    m = len(pattern)
    table = [0] * m 
    
    # q ranges in [1, ..., m - 1] because table[0] = 0
    for q in range(1, m):
        
        # Takes the current prefix
        pattern_prefix = pattern[:q + 1]

        # Finds the largest prefix of P that is also suffix of "pattern_prefix"
        for i in reversed(range(0, q)):
            
            smaller_prefix = pattern[:i + 1]
            
            if is_suffix(pattern_prefix, smaller_prefix):
                table[q] = i + 1
                break

    return table


def kmp_matcher(source, pattern):
    n = len(source)
    m = len(pattern)
    table = kmp_construct_table(pattern)

    i = 0 # Index for source
    j = 0 # Index for pattern

    while n - i >= m - j:

        # If match increases the indices
        if source[i] == pattern[j]:
            i += 1
            j += 1

        # When the end of the pattern is reached
        if j == m:
            return i - j
        
        # If any of the ends is reached and the chars doesn't match
        elif i < n and source[i] != pattern[j]:

            # Takes the previous value of the talble
            if j != 0:
                j = table[j - 1]

            # Increases the index, this is requiered, otherwise infinite loop
            else:
                i += 1

if __name__ == "__main__":
    print(kmp_construct_table("ababaca"))

    print(kmp_matcher("abbbbbbbbababacanaa", "ababaca"))