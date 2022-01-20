#Adding strings
from operator import index


x="2"+"2"
print(x)
y="hello" + "charles"
print(y)

#Slicing strings
my_string="I am a boy"
print(my_string[3])#slicing specfic characters
print(my_string[2:6])#slicing within a range
print(my_string[2:])#slicing from [x:last value]
print(my_string[-5:])#slicing from the right
print(my_string[-9:-5:2])#slicing with increments

#classwork
my_string="this is 1000 naira"
string2="this 500 is lovely"
first_value=int(my_string[8:12])
second_value=int(string2[5:8])
print(first_value+second_value)

#String formatting
my_string="this is 1000 naira"
string2="this 500 is lovely"
first_value=int(my_string[8:12])
second_value=int(string2[5:8])
added=(first_value+second_value)
print(f"the sum of {first_value} and {second_value} is {added}")

#new line and tabbing sentences
print("Dear Buhari,\nPlease dont run for president again.\n\tYours in the country\n\t\tAstroverse team.")
#print("""Dear Buhari,


#                    Yours in the country,
#                    The Astroverse Team."""

#String methods
a="aaboy"
print(a.index("a"))
print(a.rindex("a"))#counts from right(last position of substring)
print(a.count("a"))#counting values
print(a.replace("a","w"))#replacing values
sentence="Ada is a girl and tunde loves icecream but, Ayo does not give him"#splitting into a list
print(sentence.split(" "))
num=["1","2","3","4"]
otp="".join(num)#joining list values
print(otp)

#classwork
s1="Welcome to USA. usa awesome, isnt it?"
print("the_usa_count_is:", s1.lower().count("usa"))#counting while ignoring case

str1="Emma is a data scientist who knows Python. Emma works at google"
print(str1.rindex("Emma"))

str1="Emma-is-a-data-scientist"
print(str1.replace("-"," "))

#list
my_list=["I","am","good"]
a_list=["she","is","a","queen"]

x=(my_list+a_list)
print(x[: :2])#slicing with increments

list1=[10,20,[300,400,[5000,6000],500],30,40]
print(list1[2][2][0] + list1[2][3])