user_name="Long Nabati"
#vi tri:
#        0  1  2   3  4
#        -5 -4 -3  -2 -1
numbers=[1, 2, 3 , 5, 1] # tao List
print(type(numbers))
print(numbers[-1])

numbers.append(100)#Them 1 gia tri vao cuoi list
#Neu a= numbers.append("100") 
# print(a) -> tra ve gia tri None: no value

numbers.remove(1) # Xoa 1 gia tri trong list
#Neu gia tri khong nam trong danh sach thi se phat sinh loi
del numbers[3]

last_value = numbers.pop()
#Xoa di giá trị cuối trong list và nó sẽ trả về giá trị đó, mình cần gán nó cho 1 biến

numbers.extend([7,8,9]) # Thêm 1 list khác vào list đã có

numbers[0]=75# Chỉnh sửa giá trị trong list

amount=numbers.count(75) #Đếm số giá trị cần tìm trong list

print(amount)

lengh=len(numbers)
print(lengh)

numbers.insert(4,200) #chèn vào list
print(numbers)

find=numbers.index(200)#Tìm giá trị trong list
print(find)

numbers.reverse()#đảo ngược toàn list
print(numbers)

print("Thứ tự tăng dần: ")
numbers.sort() # Sắp xếp list theo thứ tự từ nhỏ đến lớn
print(numbers)

print("Thứ tự giảm dần: ")
numbers.sort(reverse=True) # Sắp xếp theo thứ tự giảm dần
print(numbers)

max_value=max(numbers)
print(max_value)
# numbers.clear()#Xoa toàn bộ list
# print(numbers)
from pprint import pprint #Giúp dễ nhìn

list_films=["Anh 7 sấbdainsaá lkasdsamlasm",
            "Anh 2 asinasasdoln oaold",
            "Anh 5 ashnoaisnas no"]
pprint(list_films)
