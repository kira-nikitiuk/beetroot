# Task 1
# Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and the number of occurrences as values. 

str1 = 'the quick drown fox jumps over the lazy dog' 
list1 = str1.split(' ') 
dict1 = {}  
max = 0 
for i in list1: 
  if i in dict1.keys(): 
    dict1[i] += 1  
    if dict1[i] > max: 
      max = dict1[i]  
      max_i = i 
  else: 
     dict1[i] = 1 
     if dict1[i] > max: 
      max = dict1[i] 
      max_i = i 
print(dict1) 
print(max,max_i)