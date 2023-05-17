def find_max_value(data: dict):
    """
    Return the maximum int or float value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """ 
    x=0
    for i in data.values():
        if i>x:
            x=i
    return x
print(find_max_value({
    'a' : -4, 
    'b' : -10, 
    'c' : 0
  }))