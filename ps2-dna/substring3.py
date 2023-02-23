def longest_substring(s, t):
    """Finds the longest substring that occurs in both s and t"""
    best = ''            
    # Find the lengths of s and t
    s_len, t_len = len(s), len(t)

    # Set the lower bound of the substring length to 0, and the upper bound to the minimum length of s and t
    low, high = 0, min(s_len, t_len)
    while low <= high:
        
        # Choose a substring length to test, halfway between the lower and upper bounds
        mid = (low + high) // 2
        # Check if there is a common substring of length mid using the k_substring function
        substr = k_substring(s, t, mid)

        # If there is a common substring of length mid, update the lower bound to mid + 1, and update the best substring
        if substr:
            best = substr
            low = mid + 1
        # Otherwise, update the upper bound to mid - 1
        else:
            high = mid - 1

    # Return the best substring found
    return best

def k_substring(s, t, k):
    """Finds a substring of length k in both s and t if there is one,
    and returns it. Otherwise, returns None."""
    s_substrings = set()
    # Put all substrings of s of length k into a set: s_substrings
    for s_start in range(len(s) - k + 1):
        current = s[s_start:s_start+k]
        s_substrings.add(current)
    # For every substring of t of length k, look for it in
    # s_substrings. If it's there, return it.
    for t_start in range(len(t)-k+1):
        current = t[t_start:t_start+k]
        if current in s_substrings:
            return current
    return None
