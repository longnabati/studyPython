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

last_value = numbers.pop()
#Xoa di giá trị cuối trong list và nó sẽ trả về giá trị đó, mình cần gán nó cho 1 biến

numbers.extend([7,8,9]) # Thêm 1 list khác vào list đã có

numbers[0]=75# Chỉnh sửa giá trị trong list

amount=numbers.count(75) #Đếm số giá trị cần tìm trong list

print(numbers)
print(amount)

numbers.clear()#Xoa toàn bộ list
print(numbers)