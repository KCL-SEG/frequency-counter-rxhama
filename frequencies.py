"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        key = item
        if not isinstance(key, str):
            key = str(key)
        if (key in frequencies):
            dictionary[key] += 1
        else:
            dictionary[key] = 1

    return frequencies
