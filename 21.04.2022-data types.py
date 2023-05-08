x="hello world" 
print(type(x)) #to print the data type of x.

y=9
print(type(y)) #to print the data type of y.

z=3.15
print(type(z)) #to print the data type of z.

x1=[1,2,3,4,5,6,7]
print(type(x1)) # to print the data type of x1

x2=3 + 6j
print(type(x2))       #to print the data type of X2

car=['bmw','benz','audi','lamborghini']     #list
print(type(car))        #print datatype of car
print(car[3])           #to print a certain item from the given list

car=['bmw','benz','audi','gtr','ferrari']       #list new
print(car)
car.append('lamborghini')           #to add a new item to list
car.insert(2,'rolls royce')         #to add a item to the specific position in the list
print(car)

car=['bmw','benz','audi','gtr','ferrari']       #list new
bike=['yamaha','ather','suzuki',]               #list
car.extend(bike)                                #to merge two(or more)lists together
print(car)

car=['bmw','benz','audi','gtr','ferrari']       #list new
bike=['yamaha','ather','suzuki']               #list
bike.extend(car)                                #to merge two(or more)lists together - check the output in both cases
print(bike)

#LIST IS MUTABLE

car=['bmw','benz','audi','gtr','ferrari']
print(car)
car[0]='porshe'                     #to change the value in index "0"
print(car)
car[3]='bmw'                        #to change the value in index "3"
print(car)                          #list is mutable see the output and learn the concept