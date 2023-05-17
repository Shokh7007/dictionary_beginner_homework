def get_min_age_user_name(data:list) -> str:
    """
    Return the name of the user with the minimum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the minimum age in the dictionary
    """
    x=data[0]["age"]
    k=0
    a=''
    for i,j in data:      
        if data[k][j]<=x:
            x=data[k][j]
            a=data[k][i]
        k+=1
    return a
print(get_min_age_user_name([
  {
    'name': 'John', 
    'age': 2
  }, 
  {
    'name': 'Mary', 
    'age': 18
  }, 
  {
    'name': 'Ann', 
    'age': 20
  },
  {
    'name': 'Ban', 
    'age': 29
  }
]))