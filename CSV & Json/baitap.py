# Tạo một meny có các chức năng của app quản lí sách
# Thêm 1 cuốn sách
# Hiển thị tất cả các cuốn sách
# Xóa các cuốn sách theo id
# Tìm kiếm cuốn sách theo id
# Lưu ý: Các dữ liệu lưu trữ các cuốn sách trong file json

import json
USER_MENU = '''
    Các chức năng:
    'a' : Thêm một cuốn sách
    'd' : Hiện thị tất cả cuốn sách
    'r' : Xóa một cuốn sách
    'f' : Tìm kiếm một cuốn sách
    'q' : Thoát
'''
bookFile = "info_book.json"
prevs = set()
try:
    with open(bookFile,mode = "x") as book_file:
        json.dump([],book_file)
except FileExistsError:
    pass


def add_book():
    id = input("Nhap vao id sach: ")
    while id in prevs:
        print("ID sach da trung lap")
        id = input("Nhap lai id sach: ")
    name = input("nhap vao ten cuon sach: ")
    author = input("Nhap vao ten tac gia: ")
    year = input("Nhap vao nam san xuat: ")
    new_book = {
        "ID" : id,
        "name" : name,
        "author" : author,
        "year" : year
    }
    with open(bookFile,mode = "r+") as file:
        lst_book = json.load(file)
        lst_book.append(new_book)
        json.dump(lst_book, file, indent = 4)
    print("Them thanh cong")
    prevs.add(id)         

def show_book(book):
    print(f"ID: {book['ID']}")
    print(f"Name : {book['name']}")      

add_book()
