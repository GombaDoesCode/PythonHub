from reprlib import aRepr


print("welcome to python")

#checking types
print (type("5"))
print (type(5))
print (type(5.0))

#changing types
print(type(int("5")))#changed a string to int

#Assigning variables
x = 5
print(x)

#using operators
x= (-10 + (4*5*3)**0.5)/(2*5)
print(x)

#classwork
#1) find the volume of a sphere of radius 5
x=(4/3)*(3.14)*(5**3)
print(x)
#2) time arrived
departed=6 + 52/60
running=(8.15+(7.12*3)+8.15)/60
arrived= (departed + running)
print(arrived)
#3) order
book=24.95
discount=0.6
shipping_cost=3
additional_copy=0.75
wholesale_cost=(book*60*discount)+shipping_cost+(59*additional_copy)
print(wholesale_cost)
#carpet costs...
L=12/3
B=15/3
area=L*B
carpeting_costs=24.99
cushioning_cost=2.99
labor_charge=35
per_square_yard=18
total_cost=(area*carpeting_costs)+(area*cushioning_cost)+35+(18*area)
print(total_cost)

