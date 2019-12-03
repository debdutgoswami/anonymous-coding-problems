def first_recurring_char(s: str) -> str:
    """python program to find the first repeated character in a string.

    Arguments:
        s {str} -- the string on which the search is to be performed.

    Returns:
        str -- first occuring character else None
    """
    h = {} # using dictionary as hash
    for ch in s:
        if ch in h:
            return ch

        h[ch] = 0
    return None

print(first_recurring_char('qwertty'))

print(first_recurring_char('qwerty'))