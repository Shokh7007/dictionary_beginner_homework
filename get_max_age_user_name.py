def get_max_age_user_name(data:list) -> str:
    """
    Return the name of the user with the maximum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the maximum age in the dictionary
    """
    x=0
    k=0
    a=''
    for i,j in data:
        
        if data[k][j]>x:
            x=data[k][j]
            a=data[k][i]
        k+=1
    return a
print(get_max_age_user_name([
  {
    'name': 'John', 
    'age': 32
  }, 
  {
    'name': 'Mary', 
    'age': 48
  }, 
  {
    'name': 'Ann', 
    'age': 2878
  }, 
  {
    'name': 'Ban', 
    'age': 29
  }
])) 