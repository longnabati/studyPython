import csv 
import json


# with open("1990sClassicHits.csv", mode="r", encoding = "utf8") as file:
#     for line in file: #Recomended dùng
#         print(line.strip())
        
with open("1990sClassicHits.csv", mode = "r", encoding = "utf8") as file:
    csv_file = csv.DictReader(file)
    lst = list(csv_file)
    print(json.dumps(lst, indent = 4)) 
    
    
import json

Student = [
    {
        "a" : 1,
        "b" : 2
    },
    {
        "a" : 3,
        "b" : 4
    }
]
# Đọc dữ liệu vào json
with open("info.json", mode = "r") as file:
    lst = json.load(file)
    print(json.dumps(lst, indent = 4))
    
#Ghi dữ liệu vào json
with open("data1.json", mode = "w") as file: 
    json.dump(Student, file, indent= 4)
    
    
#Ghi dữ liệu vào csv
import csv

header = ["Name", "age","id"]
students = ["Tai", "19","SV01"]
with open("test1.csv", mode = "w",newline= '') as file:
    csv_write = csv.writer(file)
    csv_write.writerow(header)
    csv_write.writerow(students)
    
# raw_string : r"path\to\file"

"""
- dump - ghi dữ liệu vào file json
- dumps - chuyển đổi từ list[dict] thành 1 chuỗi tương ứng
- load - đọc dữ liệu từ file json
- loads - chuyển đổi dữ liệu từ 1 chuỗi thành list[dict] hay dict tương ưng
"""


"""
csv

+ DictReader - list[dict]
+ writer(file) - Tạo ra 1 đối tượng để mình ghi
+ writerows()  - Ghi vào nhiều dòng

"""