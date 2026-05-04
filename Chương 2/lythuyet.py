#2.1. if:
#Nhap  3 so nguyen, tim so max,min trong 3 so Do:
a = int(input("nhap a: "))
b = int(input("nhap b: "))  
c = int(input("nhap c: "))
max = a
if b > max:
    max = b
if c > max:
    max = c
print("so lon nhat la: ", max)
#cmtt voi min.
# 2.1.2. if-else:
#Nhap 1 so nguyen, kiem tra xem so Do la chan hay le:
n = int(input("nhap n: "))
if n % 2 == 0:
    print("%d la so chan" %n)
else:
    print("%d la so le" %n)
#GPT bac nhat ax + b = 0
a = int(input("nhap a: "))
b = int(input("nhap b: "))
if a == 0:
    if b == 0:
        print("phuong trinh vo so nghiem")
    else:
        print("phuong trinh vo nghiem")
else:
    x = -b/a
    print("phuong trinh co nghiem x = %.2f" %x)
#Nhap 2 so va ktra ><=:
a = int(input("nhap a: "))
b = int(input("nhap b: "))
if a > b:
    print("%d > %d" %(a,b))
elif a < b:
    print("%d < %d" %(a,b))
else:
    print("%d = %d" %(a,b))
#2.1.3 if elif else:
#Nhap ma dan toc va hien thi:
ma = input("nhap ma dan toc: ")
if ma == 1:
    print("dan toc Kinh")
elif ma == 2:
    print("dan toc Tay")
elif ma == 3:
    print("dan toc Nung")
elif ma == 4:
    print("dan toc Thai")
elif ma == 5:
    print("dan toc Khmer")
else:
    print("kco ma tuong ung")
#2.2 while:
#Tinh tong cac so 1,2,...,n:
n = int(input("nhap n: "))
s = 0
i = 1
while i <= n:
    s += i
    i += 1
print("tong la: ", s)
#break, continue, pass:
var = 10
while var > 0:
    print("gia tri hien tai: ", var)
    var -= 1
    if var == 5:
        break

var  = 5
while var > 0:
    var -= 1
    if var == 3:
        continue
    print("gia tri hien tai: ", var)

i = 1
while i <= 10:
    if i % 2 == 0:
        pass
    else:
        print("gia tri hien tai: ", i)
    i += 1

#BT: Nhap 3 Diem toan, ly, hoa. Tinh Diem trung binh va xep loai: voi <5: yeu, 5-6.5: trung binh, 6.5-8: kha, >8: gioi.
toan = float(input("nhap Diem toan: "))
ly = float(input("nhap Diem ly: "))
hoa = float(input("nhap Diem hoa: "))
dtb = (toan + ly + hoa)/3
if dtb < 5:
    print("xep loai yeu")
elif dtb < 6.5:
    print("xep loai trung binh")
elif dtb < 8:
    print("xep loai kha")
else:
    print("xep loai gioi")

#2BTVN: file rieng

#2.3 For:
#Tinh tong cac so 1,2,...,n:
n = int(input("nhap n: "))
s = 0
for i in range(1, n+1):
    s += i
print("tong la: ", s)
#tinh tong day so bat ky:
n = int(input("nhap day: "))
s = 0
a=[]
for i in range(n):
    x = int(input("nhap so thu " + str(i+1) + ": "))
    a.append(x)
for i in a:
    s += i
print("tong la: ", s)
#nhap va in ma tran:
m = int(input("nhap so dong: "))
n = int(input("nhap so cot: "))
for i in range(m):
    for j in range(n):
        x = int(input("nhap phan tu thu [" + str(i) + "][" + str(j) + "]: "))
        print(x, end = " ")
    print()
#nhap vao 1 xau ky tu voi moi ky tu tren 1 dong
s = input("nhap xau: ")
for i in range(len(s)):
    print(s[i])
    i += 1

#cach 2:
s = "CNTT"
i=0
while i < len(s):
    print(s[i])
    i += 1
#nhap 1 so va ktra so Do co phai so hoan hao khong
n = int(input("nhap n: "))
s = 0
for i in range(1, n/2 + 1):
    if n % i == 0:
        s += i
    if s == n:
        print("%d la so hoan hao" %n)
    else:
        print("%d khong phai la so hoan hao" %n)
#ktra 1 xau ky tu xem co bnh ktu la so va bnh ktu la chu, neu ktdb thi thoat:
s = input("nhap xau: ")
dem_so = 0
dem_chu = 0
for i in s:
    if i.isdigit():
        dem_so += 1
    elif i.isalpha():
        dem_chu += 1
    else:
        print("xau co ky tu Dac biet, thoat chuong trinh")
        exit()
print("so ky tu la so: ", dem_so)
print("so ky tu la chu: ", dem_chu)
#cho A[1,2,3], B[4,5,6]. Tao C la hop cua A&B:
A = [1,2,3]
B = [4,5,6]
C=[]
for i in A:
    C.append(i)
for i in B:
    C.append(i)
print("hop cua A va B la: ", C)

