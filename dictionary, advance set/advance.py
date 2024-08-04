# lst = [4, 100, 27, 53]

# for value in lst:
#     print(value)

d = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}
for key in d.keys():
    print(key)
for value in d.values():
    print(value)
for item in d.items():
    key, value = item
    print(key)
    print(value)
    print(' ------------------ ')
    
"""
    +Interable : list, tuple, set, dictionary
    
"""

#List comprehensions
lst = [1, 2, 3, 4]

# #new list = [2 , 4, 6, 8]
# new_lst = []

# for x in lst:
#     val = x *2
#     new_lst.append(val)
    
# print(new_lst)

new_lst = [val * 2 for val in lst]
print(new_lst)


#Set comprehensions
set_a = {'a', 'b', 'c'}

#in hoa
new_set = {s.upper() for s in set_a}
print(new_set)

#Dict comprehensions
d = {
    'a' : 1,
    'b' : 2,
    "c" : 3
}

new_dict = {
    k : v * 2
    for k, v in d.items() 
}

print(new_dict)


"""
    +zip : Ghép các phần tử để tạo thành 1 list
    +enumberate
"""

# Dựa vào số phần tử ít nhất 
#Zip
lst1 = ['a', 'b', 'c']
lst2 = [1, 2, 3]
lst3 = ['a1', 'b1']

print(list(zip(lst1,lst2,lst3)))

# Enumerate

#       0    1    2   
lst = ['a', 'b', 'c']
print(list(enumerate(lst)))
print(dict(enumerate(lst, start = 1)))
 
lst = [1, 2, 3, 4]
print(list(val ** 3 for val in lst))

numbers = [1 , 2, 3 ,4 ,5 , 6]
new_lst = [val for val in numbers if val % 2 != 0]
print(new_lst)

new_lst1 = [val * 2 if val % 2 == 0 else val * 3 for val in numbers]
print(new_lst1)

#      1  2  3  4
lst = [1, 2, 3, 4]
for item in enumerate(lst,start = 1):
    key, val = item
    print(f"{key}  -  {val}")
for key, val in enumerate(lst, start = 1):
    if key % 2 == 0:
        print(f"{key} - {val}")
    

print(list(zip(enumerate(lst, start = 1))))