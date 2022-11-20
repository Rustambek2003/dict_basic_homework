def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    n = 0
    m = 0
    for i in txt:
        if i.isdigit():
            n += 1
        else:
            m += 1
    ans = {}
    ans['LETTERS'] = m
    ans["DIGITS"] = n
    return ans