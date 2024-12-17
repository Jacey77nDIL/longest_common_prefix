def longest_common_prefix(strs):
    min_len = min(len(s) for s in strs)  # More concise way to find min length

    for i in range(min_len):
        char = strs[0][i]  # Get the character at the current index from the first string
        for s in strs[1:]:  # Iterate through the rest of the strings
            if i >= len(s) or s[i] != char:  # Check for index out of bounds or mismatch
               return strs[0][:i]  # Return the prefix up to the mismatch
    return strs[0][:min_len] # If all prefixes match, return the shortest string or the common prefix