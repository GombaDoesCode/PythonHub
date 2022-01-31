#list methods
color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(color_list.index("Red"))#returns the position/index

# print("Welcome to the astroverse!!!")
# color=input("Enter your favourite colour: ")
# color_list.append(color)#adds new element to list
# print(color_list)

# print("Welcome to the astroverse!!!")
# color=input("Enter your favourite colour: ")
# position=int(input("Enter the position: "))
# color_list.insert(position,color)#adds new element to list in a specific position
# print(color_list)

# print("Welcome to the astroverse!!!")
# color=input("Enter your favourite colours seperated by space: ")
# cleaned_data=color.split()#removes spaces
# color_list.extend(cleaned_data)#adds multiple elements to list
# print(color_list)

# li=[0,2,9,8]
# b=li.pop(2)#extracts an element from a list but it can still be used//removes by index
# print(b)
# li.append(b)
# print(li)

# li=[0,2,9,8]
# li.remove(9)#removes element by value
# print(li)

a=[0,2,9,8]
b=a
c=a.copy()
a.remove(2)
print(b)
print(c)