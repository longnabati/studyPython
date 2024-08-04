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