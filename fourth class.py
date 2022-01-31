# #Dictionaries
# # my_dict= {}#empty dictionary

# my_dict= {"key":"value","key2":"value2"}
# my_dict["new_key"]="new_value"#adding to the dictionary//.update() adds multiple elements to the dict like extend does to sets
# print(my_dict.keys())#shows a list of all the keys//use .values() to see all values and .items to create a list of tuples[(key,values)]
# dict_1=[("key","value"),("key2","value2")]
# print(dict(dict_1))#converts list of tuples into a dictionary

# my_dict= {"key":"value","key1":"value2"}
# # popped=my_dict.pop("key")
# # print(popped)
# print(my_dict.get("xyz", "Not Found"))#.get() return the value of the specified key else it displays an error value

#Classwork
# data={"name":"chuks","location":"aba","job":"senior frontend","salary":"$50,000"}
# #change location to city
# popped=data.pop("location")
# data["city"]="aba"
# print(data)

#Conditionals
# if "ada" == "Ada":
#     print("correct")
# else:
#     print("incorrect")

# Classwork
#Write a progam that creates a user account,
#if they do not have an account(only if they want to).
#in the case where they already have an account,tell them they already do.

my_dict= dict()
account=input("Enter account mail:")
password=input("Enter account password:")
if account == my_dict:
    print("This account already exists")
else:
    my_dict[account]=password
    print(my_dict)
