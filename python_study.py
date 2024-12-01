print("=============================================")  #SEPARATOR

# print("x" * 50)                                       #EXPRESSION

print("=============================================")  #SEPARATOR

# price = 100
# print(price)

print("=============================================")  #SEPARATOR

# name = input('What is ur name?')
# print('Hi '+ name)

# name  = input('What is ur name? ')
# color = input('what is ur fav color? ')
# print('Hi '+name+' Your fav color is '+color)

print("=============================================")  #SEPARATOR

# dob = input("what is ur date of birth ")
# age = 2024 - int(dob)
# print (type(age))
# print("Your age is "+str(age))
# print (type(age))

print("=============================================")  #SEPARATOR

# x, y, z = "Orange", "Bannana", "Cherry"
# print(x)
# print(y)
# print(z)


# fruits = ["Apple", "Banana", "orange"]
# x,y,z  = fruits
# print(x)
# print(y)
# print(z)


# x = y = z = "Hello World"      # EQUAL VALUE FOR ALL VARIABLES
# print(x)
# print(y)
# print(z)

print("=============================================")  #SEPARATOR

# x = "awesome"                      # GLOBAL VARIABLE

# def my_func():
#     print("x = "+ x)

# my_func()

print("=============================================")  #SEPARATOR

# def my_func():
#     global x             #NORMALLY IT IS LOCAL BUT NOW IT IS GLOBAL
#     x = "Handsome"

# my_func()

# print(x)

print("=============================================")  #SEPARATOR

#DATA TYPES -> int/float/str/complex/list/tuple/range/dict/set/frozenset/bool/bytes/bytearray/memoryview/NoneType

# A = 10                                         #int
# print(A)


# B = 20.5                                       #float
# print(B)


# C = "Hello"                                    #str
# print(C)


# D = 5j                                         #complex
# print(D)


# E = ["Apple", "Orange", "cherry"]              #list
# print(E[0])
# print("Length of list is ",len(E))     

# F = ("Apple", "Orange", "cherry")              #tuple
# print(F[2])


# G = range(6)                                   #range
# print(G)


# H = {"name": "john", "age": 24}                #dictionary
# print(H)
# print(H["name"])


# I = {"Apple", "Orange", "cherry"}              #set
# print(I)                                       #CANT DECONSTRUCT IT


# J = frozenset({"Apple", "Orange", "cherry"})   #frozen set
# print(J)


# K = b"Hello"                                   #bytes
# print(K)            


# L = bytearray(5)                               #bytearray
# print(L) 


# M = memoryview(bytes(5))                       #memory view
# print(M)

# N = None                                       #None Type  
# print(N)


print("=============================================")  #SEPARATOR

# import random

# #print(random)                                  #THIS RANDOM NOT WORK
# print(random.randrange(1, 10))

print("=============== LIST ===============")     

# my_list = ["A", "B", "C"]
# print(my_list)
# my_list[1] = "F"
# print(my_list)
# my_list.append("L")
# print(my_list)
# my_list.insert(1, "H")
# print(my_list)
# my_list_2 = ["V", "K", "Z"]
# my_list.extend(my_list_2)
# print(my_list)
# my_list.remove("L")
# print(my_list)
# my_list.pop(1)
# print(my_list)
# my_list.pop()
# print(my_list)
# del my_list[0]
# #print(my_list)
# #del my_list
# #print(my_list)             # GIVES AN ERROR AS IT IS REMOVED EXPECTED OR my_list.clear()

# for x in my_list_2:
#   print(x)


# i = 0
# while i < len(my_list_2):
#     print(my_list_2[i])
#     i = i + 1


# new_list = [x for x in my_list_2 if "V" in x]     # X Comprehnsion
# print(new_list)

# new_list = [x for x in range(10)]
# print(new_list)


# new_list = [30, 80, 300, 40, 50]
# new_list.sort()
# print(new_list)

# copy_list = new_list.copy()
# print(copy_list)

# third_list = new_list + copy_list     #[1] FIRST  METHOD     
# print(third_list)
# #OR
# for y in copy_list:                   #[2] SECOND METHOD
#     third_list.append(y)
# print(third_list)

print("=============================================")  #SEPARATOR

print("=============== TUPLES ===============")     

# my_tuple = ("apple", "bananna", "potatoe", "cheese")
# print(my_tuple)
# print(my_tuple[:2])
# print(my_tuple[2:])
# print(my_tuple[-1])   #LAST ELEMENT
# print(my_tuple[-2])   #ELEMENT BEFORE LAST ELEMENT

# if "apple" in my_tuple:
#         print("Yes, Apple Exists")


# if "hassan" in my_tuple:
#         print("Yes, hassan Exists")
# else: 
#         print("No, hassan not Exists")


# # Once tuple is created u can not change its values BUT u can do that by converting it to a list
# my_tup_2_list = list(my_tuple)
# my_tup_2_list[1] = "Tuna"
# my_tup_2_list.append("protein")
# print(my_tup_2_list)

# y = ("creatine",)
# my_tuple += y          # ADD TUPLE TO TUPLE
# print(my_tuple)


# new_tuple = ("green", "red", "yelllow")   # UN_PACKING TUPLE
# (color1, color2, color3) = new_tuple
# print(color1)
# print(color2)
# print(color3)


# new_tuple = ("green", "red", "yelllow", "violet", "pink")   # UN_PACKING TUPLE
# (color1, color2, *other_colors) = new_tuple           # Astrix means save all others as a list if num of values > num of variables 
# print(color1)
# print(color2)
# print(other_colors)


# print("loop1=========")
# for x in new_tuple:
#      print(x)

# # OR
# print("loop2=========")
# for x in range (len(new_tuple)):   # in range make x represents index not value
#     print(new_tuple[x])

# # OR
# print("loop3=========")
# i = 0
# while i < len(new_tuple):
#     print(new_tuple[i])
#     i = i + 1


# # JOIN TUPLES
# third_tuple = my_tuple + new_tuple
# print(third_tuple)

# third_tuple = my_tuple * 2
# print(third_tuple)


print("=============================================")  #SEPARATOR

print("=============== SETS ===============")  

# # SETS ARE UNORDERED SO WE CANT PREDICT IN WHICH ORDER THEY WILL APPEAR
# # NO DUPLICATES IN ONE SET SO TRUE AND 1 DOR EXAMPLE CONSIDERED DUPLICATE

# my_set = {"hassan", "hassan", "sara", "ahmed", "salem"}
# print(my_set)

# if "hassan" in my_set:
#     print("EXISTS")

# if "ALI" not in my_set:
#     print("NOT EXISTS")

# my_set.add("ali")
# print(my_set) 

# new_list = ["hello" , "hi"] 
# new_set  = {"hello" , "hi"}
# my_set.update(new_set)   # UPDATE CAN BE ANY ITERABLE LIST/TUPLE/SET/DICT
# print(my_set)
# my_set.update(new_list)
# print(my_set)

# my_set.remove("hassan")
# my_set.discard("salem")
# print(my_set)


# my_set.pop()   # REMOVE RANDOM ITEM
# print(my_set)


# # my_set.clear() # EMPTIES THE SET
# # del my_set
# # print(my_set)


# # FOR SET JOIN -> set1.update/union/intersection/difference/symmetric_difference(set2)
# # symmetric_difference -> keeps all values except duplicates
# # union equiv to set1 | set2 
# # set1.union(set2,set3,set4) <===> sest5 = set1 | set2 | set3 | set4
# # intersection equiv to set1 & set2 
# # difference equiv to set1 - set2
# # set1.difference_update(set2) will update the original one no LHS
# # set3 = set1.symmetric_difference(set2) keeps the items not present in both sets
# # symmetric_diff equiv to ^
# # update is equiv to |=


print("=============================================")  #SEPARATOR

print("=============== DICTIONARY ===============")  

# KEEPS VALUES IN KEY-VALUE PAIR

# my_dict = {
#     "brand" : "FORD",
#     "model" : "MUSTANG",
#     "year"  : "1964",
#     "color" : "red"
# }

# print(my_dict)
# print(my_dict["color"])
# print(len(my_dict))

# # DATA INSIDE DICT CAN BE OF ANY DATA TYPE
# my_dict2 = {
#     "brand" : "FORD",
#     "model" : "MUSTANG",
#     "year"  : "1964",
#     "electric": True,
#     "colors" : ["red", "green", "blue"]
# }
# print(my_dict2)


# # USING dict constructor to create a dict
# new_dict = dict(name = "hassan", age = 24, country = "Egypt")
# print(new_dict)


# x = new_dict.keys()
# print(x)
# new_dict["color"] = "Black"  # ADDING A NEW KEY-VALUE Pair 
# print(new_dict)
# x = new_dict.values()
# print(x)
# x = new_dict.items()   # GET THE CONTENT AS A LIST OF TUPLES "GOOD"
# print(x)



# print("loop1=========")
# for x in my_dict.keys():
#     print(x)

# print("loop2=========")
# for x in my_dict.values():
#     print(x)

# print("loop3=========")
# for x,y in my_dict.items():
#     print(x, y)



# cpy_dict = dict(my_dict)
# print(cpy_dict)


# nested_dict = {
    
#     "child1":{
#         "name": "hassan",
#         "age" : 24
#     },

#     "child2":{
#         "name": "ahmed",
#         "age" : 22
#     },

#     "child3":{
#         "name": "salem",
#         "age" : 21
#     }    
# }

# print(nested_dict)

# # OR

# child1 = {
#     "name": "hassan",
#     "age" : 24    
# } 

# child2 = {
#     "name": "ahmed",
#     "age" : 22    
# } 

# child3 = {
#     "name": "Salem",
#     "age" : 20    
# } 

# nested_dict = {
#     "child1" : child1,
#     "child2" : child2,
#     "child3" : child3
# }
# print(nested_dict)


print("=============================================")  #SEPARATOR

print("=============== IF/ELIF/ELSE ===============")  

a = 100
b = 800
c = 5000

if a > b:
    print("a is bigger than b")
elif b > c:
    print("b is the greatest")
else:
    print("c is the biggest")    


print("=============================================")  #SEPARATOR


