"""
+ Advanced set
+ Dictionary => key : value
+ sum, len, min, max, join
"""


set1 = {1, 4, 3, 2}
set2 = {2,5,4,10}

set3 = set1.intersection(set2) # Set 1 còn cái thứ 2 có thể là list hoặc tupple
print(set3)

print(set1 & set2) # Cả 2 đều phải là set 

#diffenrence
set3 = set1.difference(set2) # Set 1 còn cái thứ 2 có thể là list hoặc tupple
print(set3)

print(set1 - set2) # Cả 2 đều phải là set 


#gộp nhưng ko trùng lặp
set3 = set1.union(set2)
print(set3)

print(set1 | set2)

# Lấy ra tất cả phần tử trừ đi phần chung
set3 = set1.symmetric_difference(set2)
print(set3)

print(set1 ^ set2)

# Dictionary 
import json

students = {
    "name" : "Bob",
    "age" : 23,
    "grades" : [45, 67, 90, 98, 99]
}

print(json.dumps(students, indent = 4))

value = students.get("id", 23718491)
print(value)

students["id"] = 237
print(students["id"])


info = [
    ("cid", 20),
    ("gender", "Nam")
]
students.update(info)
print(json.dumps(students, indent = 4))

#remove
value = students.pop("name")
del students["age"]
print(students)
print(value)


tup = students.popitem()
print(tup)
print(students)

#key

key = list(students.keys())
print(key)

#value 
value = list(students.values())
print(value)

#items
items = list(students.items())
print(items)


#sum
list1 = [[1, 2, 3, 4]]
sum2 = sum(list1, [0])

print(sum2)

#join : Ngăn cách nhau bởi
lst = [1, 2, 3, 4]
s = " - ".join(map(str,lst)) # Hàm map dùng để chuyển list về dạng tương ứng
print(s)