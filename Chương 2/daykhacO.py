kq_tong = 0
so = int (input ("Nhap so:"))
while so != 0 :
    if so % 2 == 0 :
        kq_tong += so
    so = int (input ("Nhap so:"))
print ("Tong cac so chan la:", kq_tong)
