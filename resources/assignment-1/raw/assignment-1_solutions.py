#Python1
#WRITE YOUR CODE INTO THIS CELL (~1 line of comments)
first_number = 5
second_number = "6"
first_number + int(second_number)
#as.integer

#Python2
#bash
##WRITE YOUR BASH COMMANDS INTO THIS CELL (~1-2 lines of code)
#pip install pandas numpy

#Python3
#WRITE YOUR CODE INTO THIS CELL (add ~1 line above code)
import numpy as np
another_array = np.zeros((2, 4, 6))

#Python4
#WRITE YOUR CODE INTO THIS CELL (edit ~1 line of code)
another_array = np.zeros((2, 4, 6))
new_array = another_array.copy()
new_array[1, 2, 2] = 1
print(another_array[1, 2, 2])

#Python5
#WRITE YOUR CODE INTO THIS CELL (edit SECOND line of code)
sample_scores = np.array([1, 6, 7, 8, 9, np.nan])
print(np.mean(sample_scores[~np.isnan(sample_scores)]))

#Python6
#WRITE YOUR CODE INTO THIS CELL (~1 line of code)
my_array = np.zeros((4,3,5))

#Python7
#WRITE YOUR CODE INTO THIS CELL (~2 lines of code)
import numpy as np 
# Create an array of the first 50 odd positive integers
odd_numbers = np.arange(1, 100, 2)  # Odd numbers from 1 to 99
# Compute the product of the array elements
product = np.prod(odd_numbers) 
print(product)

#Python8
#WRITE YOUR CODE INTO THIS CELL (~1-6 lines of code)
import pandas as pd

# Create the DataFrame in Python with shortcuts for all columns, including "Morality"
lotr_characters = pd.DataFrame({
  'Name': ["Gollum", "Smeagol", "Sauron", "Frodo", "Shelob", "Samwise"],
  'First_appearance': ["The Hobbit"]*3 + ["LOTR"]*3, 
  'Morality': ["Bad", "Good"]*3,  
  'Dating_appeal': list(range(0, 11, 2))
})

#Python9
#WRITE YOUR CODE INTO THIS CELL (~1-2 lines of code)
import os
" ".join(os.listdir())

#Python10
#WRITE YOUR CODE INTO THIS CELL (~2-5 lines of code)
my_measurements = {
  "my_mood_measurements": np.random.choice(["happy", "sad"], 365),
  "my_iq_values": np.random.normal(100, 3, 52)}
