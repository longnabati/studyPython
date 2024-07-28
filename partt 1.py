"""
    + set {} => Không thể lặp lại, không thể truy cập các giá trị trong set 
    + tupple () => Không thể thêm
"""
#tuple()

tup1= 1, 2, 3
tup1 += (4,5,6)
print(tup1)

#set{}
set1= set()
set1.add(1) #add chỉ dùng để thêm giá trị không thể thay đổi
set1.update([4,5,6,"abc"]) #update có thể thêm cả 1 list vào set (vì list 6)
set2=set1.copy()
print(set1)
print(type(set1))
print(set2 is set1)
print(set2 == set1)

any_value=set1.pop()#xóa 1 giá trị bất kỳ

#Để copy sâu vào trong lst ban đầu dùng
from copy import deepcopy

lst = [[1,[2,3]],(4,5)]
lst1 = lst[:]   #lst1 = lst.copy() => nó vẫn copy giá trị trong lst thay đổi

lst2 = deepcopy(lst) #copy giá trị ban đầu của lst


lst[0][1].append(100)
print(lst1)
print(lst2)

#kiểm tra kiểu của giá trị
print(isinstance("abc",str))

#trả về thứ tự của ký tự 
print(ord('b'))

print(repr('a')) #in ra cả dấu nháy
s = 'a'
print(f"{s !r}")