#Doc file abcd.txt va in ra nd
obj = open("abcd.txt", "r")
nd1 = obj.read()
print('nd1: ' + nd1)
obj.close()
#co gia tri
obj = open("abcd.txt", "r")
nd2 = obj.read(6)
print('nd2: ' + nd2)
obj.close()

f =open("dulieu.txt", "r")
s = f.read()
s = s.strip()#xoa khoang trang o Dau va cuoi chuoi s
a = s.split(" ") #tach chuoi s thanh 1 list a, moi phan tu cua a la 1 so nguyen duoi dang chuoi
t=0
print("day:",a)
for i in a:
    t += int(i)
print("tong:",t)
f.close()

#Doc file abcd.txt theo readline
obj = open("abcd.txt", "r")
nd4 = obj.readline()
print('nd4: ' + nd4)
obj.close()

obj = open("abcd.txt", "r")
nd5 = obj.readline(3)
print('nd5: ' + nd5)
obj.close()
#cach1  
obj = open("abcd.txt", "r")
for i in range(3):
    nd6 = obj.readline()
    print('nd6: ' + nd6)
obj.close()
#cach 2
obj = open("abcd.txt", "r")
nd7 = obj.readline()
while nd7: 
    print('nd7: ' + nd7)
    nd7 = obj.readline()
obj.close()
#cach 3
obj = open("abcd.txt", "r")
for i in obj:
    print(i)
obj.close()

#Doc vao 1 ma tran tu file ma_tran.txt, tinh va in ra tong ma tran Do
f = open("ma_tran.txt", "r")
s = f.readlines()
t = 0
for i in s:
    a = i.split() #tach chuoi i thanh 1 list a, moi phan tu cua a la 1 so nguyen duoi dang chuoi
    for j in a:
        t += int(j)
print("tong ma tran:", t)
f.close()  

