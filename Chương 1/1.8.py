

#1.7. Nhap/Xuat
#format()
name = "Ha Huy Dat"
msv = "2421030171"
lop = "DCCTCT68B"
print("Xin chao, toi la {}, msv: {}, lop: {}".format(name, msv, lop))

#1.8 Cac kdl chuan
#1.8.1 Cac ham xu ly xau
#Nhap vao 1 xau "cnTt dia tin hoc, dia chat".Hthi xau Do tu vtri 3, 4-7, all:
s = "cnTt dia tin hoc, dia chat, dia hoc"
print(s[3]) 
print(s[4:8])
print(s[:])
print(s[0:])
print(s[4:2:-1])
print(s[-1:-3:-1])
print(s[-3:-1])
#in:
print('a' in 'abc')
print('ac' in 'abc')
#Cac ham: len()
a = "dia"
print(len(a))
#lower(), upper()
print(a.lower())
print(a.upper())
#find()
print(s.find(a))
print(s.find(a, 10))
print(s.find(a, 20))
#count()
print(s.count(a))
print(s.count(a,10))
print(s.count(a,10, -1))
#replace()
print(s.replace("dia", "Dia"))
print(s.replace("dia", "Dia", 2))
#split()
print(s.split())
print(s.split(" ", 1))
#lstrip(), rstrip(), strip()
chuoi1 = "   dia hoc   "
print(chuoi1.lstrip())
print(chuoi1.rstrip())
print(chuoi1.strip()) 
#isalpha(), isdigit(), isspace()
print("abc".isalpha())
print("ab c".isalpha())
print("123".isdigit())
print("12 3".isdigit())
print("   ".isspace())
print(" .  ".isspace())

#1.8.3 List
#Cac ham tuong tu nhu xau: len(), count(), index(), find(), in, replace(), split(),append(), insert(), pop(), remove(), sort(), reverse(),... 
#ham list(): chuyen 1 tuple thanh list:
t = (1, "a1", "abc")
l = list(t)
print(t)
print(l)
#toan tu +,*:
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l1 + l2)
print(l1 * 3)
l3 = [1, "ab", [1, 2]]
l4 = [1, "cd", [3,4]]
print(l3 + l4)
#print(l3 * l4) #ko dc
print(["ab"] * 2)
#thay Doi phan tu trong list:
l5 = [1, 2, 3, 4]
l5[0] = 10
print(l5)
#thay Doi phan tu trong list con:
l6 = [1, 2, [3, 4]]
l6[2][0] = 30
print(l6)
#ham len():
l7 = [1, 2, 3, 4]
print(len(l7))
l8 = [1, 2, [3, 4]]
print(len(l8))
#max, min:
l9 = [1, 2, 3, 4]
print(max(l9))
print(min(l9))
#append():
l10 = [1, 2, 3]
l10.append(4)
print(l10)
#count():
l11 = [1, 2, 3, 2, 4]
print(l11.count(2))
#extend():
l12 = [1, 2, 3]
l13 = [4, 5, 6]
l12.extend(l13)
print(l12)
#index():
l14 = [1, 2, 3, 2, 4]
print(l14.index(2))
print(l14.index(2, 2))#tim tu vi tri 2 tro Di
#insert():
l15 = [1, 2, 3]
l15.insert(1, 10)
print(l15)
#pop():
l16 = [1, 2, 3, 4]
print(l16.pop()) #mac Dinh xoa phan tu cuoi
print(l16)
#remove():
l17 = [1, 2, 3, 2, 4]
l17.remove(2) #xoa phan tu Dau tien co gia tri 2
print(l17)
#del():
l18 = [1, 2, 3, 4]
del l18[1] #xoa phan tu co vi tri 1
print(l18)
#reverse():
l19 = [1, 2, 3, 4]
l19.reverse()
print(l19)
#clear():
l20 = [1, 2, 3, 4]
l20.clear()
print(l20)
#sort():
l21 = [3, 1, 4, 2]  
l21.sort()
print(l21)
#list chua list:
l22 = [[1, 2,3], [4, 5, 6]]
print(l22)
print(l22[0])
print(l22[0][1])
print(l22[0][:2])
print(l22[0][:])
#Bai tap:
#Nhap vao 1 chuoi so cach nhau boi " ", chuyen chung thanh list so nguyen va tinh tong.in ra ma tran 1 chieu cua chuoi so Do
chuoi1 = input("Nhap vao mot chuoi so cach nhau boi khoang trang: ")
danh_sach = eval("[" + chuoi1.replace(" ",",") + "]") #chuyen chuoi thanh list
print(danh_sach)
chuoi2 = input("Nhap vao mot chuoi so cach nhau boi dau phay va cac hang cua ma tran cach nhau boi dau cham phay: ")
ma_tran = eval("[" + chuoi2.replace(";","],[").replace(" ",",") + "]") 
#chuoi2 = "1 2 3;4 5 6;7 8 9" sao khong nhap vao chuoi so cach nhau boi dau phay va cac hang cua ma tran cach nhau boi dau cham phay, do 
print(ma_tran)
kq_tong = sum(danh_sach) 
print(kq_tong)

#1.8.4 Tuple
#BT: Nhap ma_tran 4x3 duoi dang tuple:
chuoi3 = input("Nhap vao mot chuoi so cach nhau boi dau phay va cac hang cua ma tran cach nhau boi dau cham phay: ")
matran_tuple = eval("(" + chuoi3.replace(";","),(").replace(" ",",") + ")")
print(matran_tuple)
#in phan tu cua tuple, cach nhau boi " ", su dung *matrix[]:
print(*matran_tuple)
#1.8.5. Dictionary
tu_dien = {"name": "Ha Huy Dat", "msv": "2421030171", "lop": "DCCTCT68B"}
print(tu_dien)
print(tu_dien["name"])
tu_dien["cannang"] = 60
print(tu_dien)

#1.8.6 Date and Time
import datetime
#lay ngay gio hien tai:
hien_tai = datetime.datetime.hien_tai()
print(hien_tai)
#tao mot Doi tuong datetime:
dt = datetime.datetime(2024, 6, 1, 12, 0, 0)
print(dt)   
#pthuc strftime(): Dinh dang ngay gio thanh chuoi:
import datetime
hien_tai = datetime.datetime.hien_tai()
print(hien_tai)
s = hien_tai.strftime("%Y-%m-%d %H:%M:%S")
print(s)
#pthuc strptime(): chuyen chuoi thanh datetime:
from datetime import datetime
chuoi1 = "2024-06-01 12:00:00"
ngay_gio = datetime.strptime(chuoi1, "%Y-%m-%d %H:%M:%S")
print(ngay_gio)
chuoi2 = ngay_gio.strftime("%d/%m/%Y %H:%M:%S")
print(chuoi2)





