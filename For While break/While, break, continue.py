s = input("S = ")
while s != 'q':
    print("Hello")
    s = input("S = ")
    
""" 
    + break
    + continue
    
"""
for i in range(1, 21):
    if i > 5:
        break
    print(i,  end = ' ' )

# In ra các số lẻ
for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i,  end = ' ' )