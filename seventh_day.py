# d={1:'one',2:'two',3:'three'}
# print(d)

d={1:'one',2:'two'}
# print(d.setdefault(1,"one"))
# print(d.update([(2,"dui")]))
# print(d.update({2:"two"}))
print( d.update([(3,"five"),(4,["six","choy","che"])]))
print(d.get(3))
print(d)