# 1. Join the items of this list to a string sentence. Print the result on the terminal. 
#     my_list = [ "The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]

# 2. Change the value of True in this list to False. Print the result on the terminal
#     new_list = ['this', "brown", 55, "oxen", True, 0.85]

# 3. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Sample List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output = ['Green', 'White', 'Black']

# 4. Write a program that takes in the user input of his favourite colour and adds it to an existing list of colours.
# color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

#solution
from ntpath import join
from os import remove


my_list = [ "The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]
sentence=" ".join(my_list)
print(sentence)

new_list = ['this', "brown", 55, "oxen", True, 0.85]
new_list[4]= False
print(new_list)

sample_List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
del sample_List[0]
del sample_List[4]
del sample_List[3]
print(sample_List)

color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color=input("Type your favourite colour: ")
color_list.append(color)
print(color_list)

