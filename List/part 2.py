"""
    + list in list
    + copy list 
    + list slicing
"""
#List in list
friends = [["Bob",23], ["Jen",34], ["Kenny", 56]] 

print(friends[0][0])

#copy list
lst1= [1, 3, 4,7]
lst2= lst1.copy() #copy sẽ khác địa chỉ bộ nhứo

#is : Check thử có cùng địa chỉ bộ nhớ không
print(lst2 is lst1) # địa chỉ bộ nhớ
print(lst2 == lst1) #  giá trị

#id : in ra địa chỉ bộ nhớ
print(id(lst1), id(lst2))

#list slicing => new list
#         0  1  2  3  4
#         -5 -4 -3 -2 -1
a= [3, 5, 7, 9, 10]
# a[start : stop : step]
new_list = a[:]
print(new_list)