#-------------SYNTAX--------------
str1 ="This is a string "
str2='Aman'
str3="""This is another string """
str4="This is string\nin next line"
print(str4)

#------------CONCATENATION & LENGTH-----------
str5="Aman"
str6="Mishra"
print(str5+str6)
print(len(str5))

#------------------INDEXING(access character)-----------------
print(str5[0])

#---------------------SLICING(doesn't inclue ending)------------------------
str7="Herbivore Animal"
print(str7[0:]) #automatically till end
print(str7[0:9])
print(str7[9:])
print(str7[:9])
print(str7[-3:-1])

#---------------------STRING FUNCTION-----------------------------
str="I am studying python"
print(str.endswith("on"))

str8="aman"
print(str8.capitalize())

str9="i am studying python from appna college"
print(str9.replace("o","a"))
print(str9.replace("python","java"))

str10="Finding Characters in string"
print(str10.find("a"))
print(str10.find("string"))

str11="i am from ghaziabad and i from up"
print(str11.count("from"))
print(str11.count("i"))
