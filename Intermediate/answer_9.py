#Write a Python program to find the longest common prefix among a list of strings.

def longestCommonPrefix(strs):
    
    prefix = strs[0]

    for string in strs[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

input_strings = ["flower", "flow", "flight"]

print("Longest Common Prefix:", longestCommonPrefix(input_strings))