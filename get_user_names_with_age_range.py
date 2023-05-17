def get_user_names_with_age_range(data:list, min_age:int, max_age:int) -> list:
    """
    Return a list of users with a given age range

    Args:
        data (dict): A dictionary of values
        min_age (int): The minimum age to search for
        max_age (int): The maximum age to search for
    Returns:
        list: A list of users with the given age range
    """
    x=max_age
    y=min_age
    k=0
    a=[]
    for i,j in data:
        if y<=data[k][j] and data[k][j]<=x: 
            a.append(data[k][i])
        k+=1
    return a
print(get_user_names_with_age_range([
  {
    'name': 'Joh7n', 
    'age': 20
  }, 
  {
    'name': 'Mary', 
    'age': 17
  },
  {
    'name': 'Ban', 
    'age': 23
  },
  {
    'name': 'John', 
    'age': 27
  }
],18,25)) 