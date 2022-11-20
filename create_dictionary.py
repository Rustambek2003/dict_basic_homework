def create_dictionary(key, value):
    """
    Convert two lists into a dictionary
    Args:
        key(list): list of keys
        value(list): list of values
    Returns:
        dict: dictionary with keys and values
    """
    a = zip(key,value)
    ans = {}
    for i, j in a:
        ans[i] = j

    
    return ans
