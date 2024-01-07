#!/usr/bin/python3
"""text-indentation function."""

def text_indentation(text):
    """Print text with two new lines
    Args:
    text (string)
    Raises:
    TypeError
    """
    if not isinstance(text, str):
    raise TypeError("text must be a string")

    ch = 0
    while ch < len(text) and text[ch] == ' ':
    ch += 1

    while ch < len(text):
    print(text[ch], end="")
    if text[ch] == "\n" or text[ch] in ".?:":
    if text[ch] in ".?:":
    print("\n")
    ch += 1
    while ch < len(text) and text[ch] == ' ':
    ch += 1
    continue
    ch += 1
