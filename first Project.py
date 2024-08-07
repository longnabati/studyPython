#Tạo list movie
movies = []

# Tạo ra 1 set để kiểm tra xem tên phim có bị trùng lặp ko
test = set()

def add_movie():
    name = input("Nhap vao ten bo phim: ")
    while name in test:
        print("Vui long nhap lai ten phim !")
        name = input("Nhap vao ten bo phim: ")
    director = input("Nhap vao ten dao dien: ")
    year = input("Nhap vao nam phát hành: ")
    movie = {
        'name' : name,
        'director' : director,
        'year' : year
    }
    movies.append(movie)
    test.add(name)
    
def show_moive(movie):
    movie_name = movie['name']
    movie_director = movie['director']
    movie_year = movie['year']
    
    print(f"Tên:\t {movie_name}")
    print(f"Tên đạo diễn:\t {movie_director}")
    print(f"Năm sản xuất:\t {movie_year}")
    
def show_movies():
    if movies:
        for idx, movie in enumerate(movies,start = 1):
            print("THÔNG TIN BỘ PHIM ",idx)
            show_moive(movie)
    else:
        print("Danh sách trống !")
