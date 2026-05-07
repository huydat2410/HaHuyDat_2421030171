fo = open ("foo.txt", "w")
fo.write("Python la ngon ngu lap trinh. \nMinh cung nghi nhu the!! \n")
fo.close()
# Cac thuoc tinh cua file:
#1 kiem tra xem file Da Dong chua
print(fo.closed)
#2 che Do truy cap
print(fo.mode)
#3 ten file
print(fo.name)
