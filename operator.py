a=5
b=2
print(a**b) #a^b(power)

print(not(a>b))

#---------------------------LOGICAL OPERATOR(and ,or,not)
val1=True
val2=False
print("And operator :",val1 and val2)

#------------------------- TYPE CONVERSION(implicit , explicit)
va =2
va1=4.25
sum = va + va1
print(sum)
#---------------------------------Explicit
p = int("4") #string("4") to integer(4)
q = 4.25
sum2 = p+q 
print(sum2)
pq = 10
pq =str(pq)
print(type(pq))

#----------------------INPUT(all value automatic converted to string , so we need typecasting)
val4=input("Enter some value:")
print(type(val4),val4)

val5= int(input("Enter the value :"))
print(type(val5),val5)

val6= float(input("Enter the value :"))
print(type(val6),val6)