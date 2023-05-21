

def rabin_karp(string, pattern, q=13):

    base = 256
    m = len(pattern)
    n = len(string)
    h = pow(base, m - 1) % q

    # Preprocessing
    pattern_hash = 0
    rolling_hash = 0
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % q
        rolling_hash = (base * rolling_hash + ord(string[i])) % q

    # Matching
    for s in range(n - m + 1):

        if rolling_hash == pattern_hash:

            if pattern == string[s : s + m]:
                return s

        if s < n - m:
            rolling_hash = (base * (rolling_hash - h * ord(string[s])) + ord(string[s + m])) % q
