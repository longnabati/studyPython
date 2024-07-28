"""
    + set {}
    + tupple ()
"""
#tuple()

tup1= 1, 2, 3
tup1 += (4,5,6)
print(tup1)

#set{}
set1= set()
set1.add(1)
set1.update([4,5,6])
set2=set1.copy()
print(set1)
print(set2 is set1)
print(set2 == set1)
