import numpy as np
from datetime import datetime
import time
import warnings

#Python1
# There are a few methods.

current_hour = datetime.now().hour

if current_hour >= 0 and current_hour < 5:
    print("Go to sleep!")
elif current_hour >= 7 and current_hour < 11:
    print("Eat your breakfast!")
else:
    print("Hang out on your phone!")


#Python2
def calculate_compatibility(user1, user2):
    total_score = 0
    total_importance = 0
    for hobby in user1:
        rating_diff = abs(user1[hobby][0] - user2[hobby][0])
        similarity = 1 - rating_diff / 10
        avg_importance = (user1[hobby][1] + user2[hobby][1]) / 2
        total_score += similarity * avg_importance
        total_importance += avg_importance
    return round(total_score / total_importance, 2)
  
#Python3
def special(vector):
    if not isinstance(vector, np.ndarray):
        raise Exception('Not a numpy ndarray!')
    special_vec = np.array(vector[0])
    for i in range(len(vector)):
        if vector[i] not in special_vec:
            special_vec = np.append(special_vec, vector[i])
    if np.array_equal(vector,special_vec):
        warnings.warn("All values are special!")
    print(special_vec)

#Python4
#A try block in Python is used to wrap code that may raise an exception
def do_something():
  try: 
      list_vec = [1, 2, 3, 3, 4, 5]
      print(this_is_not_implemented(list_vec))
  except Exception as e:
      print(e)

#Python5
def prime(n):
    result = np.zeros(n)
    count = 0
    number = 1
    while(count < n):
        check = True
        number += 1
        for i in range(count):
            if number % result[i] == 0.:
                check = False
                break
        if check:
            result[count] = number
            count += 1
    return result

#Python6
# The docstring of the function definition is shown as help
# Breaking up code into multiple files or modules makes it easier to read and work with 

#Python7
import string
def is_strong_password(password):
    """Check if the password is strong."""
    assert isinstance(password, str), "Input must be a string"
    
    # Define conditions
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    
    # Check if at least two conditions are met
    met_conditions = sum([has_upper, has_lower, has_digit, has_special])
    assert met_conditions >= 2, "Password must meet at least two of the strength requirements"
    
    return True
