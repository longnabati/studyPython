


"""
    + Python functions
"""

def func(lst = []):
    lst.append(2)
    print(lst)
    
func()
func()

def greet(msg):
    print("Hello "+ msg) # Mọi hàm đều trả về None
    
hello = greet
print(hello("Jone"))

# *args
def add(*arg):
    return sum(arg)

print(add(1,2,3,4,5,6))

lst = [10 , 4 , 8, 9, 21]
first, *mid ,last = lst
print(first)
print(mid)
print(last)


def addd(*lst, operation):
    return operation(lst)

print(addd(1,2,3,4, operation = sum))

"""Mặc định tất cả các giá trị của hàm đều trả về None"""

lst = [[] for _ in range (5)]

lst[1].append(2)
print(lst) 

""" Những tham số mặc định phải được đặt ở cuối cùng

EX:
def func(a= 2, b):
    pass
    
=> Bị lỗi


"""

