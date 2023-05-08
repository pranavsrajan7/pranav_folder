animals=['dog','cat','goat','cow','pig','cow','crow']
fruits=['orange','apple','mango']

print(animals)
animals.append('hen')           #append
print(animals)
count=animals.count('cat')      #count
print(count)
animals.insert(3,'sheep')       #insert
print(animals)
animals.pop(2)                  #pop
print(animals)
animals.remove('crow')          #remove
print(animals)
animals.reverse()               #reverse
print(animals)
animals.extend(fruits)          #extend
print(animals)  
animals.sort()                  #sort
print(animals)

animals.sort(reverse=True) # sort in descending order
print(animals)             # print the sorted list

animals.clear()                 #clear
print(animals)