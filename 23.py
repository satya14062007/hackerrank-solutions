def merge_the_tools(string, k):
    # Loop through the string in steps of k
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        result = ""
        seen = set()

        # Build the subsequence with unique characters
        for ch in substring:
            if ch not in seen:
                seen.add(ch)
                result += ch

        print(result)
