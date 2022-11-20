def cities_dict(cities:list):
    """
    Given a list of cities names, Return dictionary with keys ordered by city name.
    Args:
        cities(list): list of cities names
    Returns:
        dict: dictionary with keys ordered by city name
    """
    ans = {}
    for i in cities:
        ans[i] = i 
    return ans
print(cities_dict(['navoi','samarqand','toshkent']))
