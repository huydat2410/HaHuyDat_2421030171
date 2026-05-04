n = int (input ("Nhap so pt day:"))
a = []
i = 0
while i < n :
    x = int (input ("Nhap so thu " + str (i + 1) + ":"))
    a.append (x)
    i += 1
i = 0 
kq_tong = 0
while i < n :
    if a [i] % 2 == 0 :
        kq_tong += a [i]
    i += 1
print ("Tong cac so chan la:", kq_tong)
