"""
     if - elif - else

"""

n = int(input("n = "))
# if n > 0:
#     print("So duong")
# elif n < 0:
#     print("So am")
# else:
#     print("So 0")
    
print("n chia het cho 3" if n % 3 == 0 else "n khong chia het cho 3")   

# Nhập 2 số trên cùng 1 hàng
a , b = map(int, input().split()) #split là tách ra từng phần tử
# map là quy đổi các phần tử về dạng định sẵn

print(a if a > b else b)

#eval : đánh giá biểu thức nằm trong chuỗi
print(eval("1 + 2 ** 4"))

lst = list(map(eval, input().split())) #Có thể nhập vừa số nguyên vừa số thực
print(lst)

lst1 = [1 , 2, 3, 4]
print(*lst1, sep = " % ") #Phá vỡ list ra thành từng phần tử

#format : làm tròn số
x = 2.4567
print(format(x , ".2f"))

#round : làm tròn
print(round(x, 2))

#Sorted => List được sắp xếp
lst = [1, 2, 3, 4]
lst.sort()
new_lst = sorted(lst , reverse=True)
print(new_lst)

print(divmod(4 , 3))

print(bin(3)[2:])

print(format(3, 'b'))