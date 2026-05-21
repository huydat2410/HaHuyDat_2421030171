# Cau 7 Viet chuong trinh nhap vao mot day so nguyen x1, x2, ..., xn (0 < n < 100), tinh tong cac phan tu la so nguyen to trong day, va kiem tra xem tong nay co phai la so le va lon hon 50 hay khong.
# Ham kiem tra mot so co phai so nguyen to hay khong
def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Ham giai quyet chinh cho Cau 7
def giai_cau_7(n):
    arr = []
    for i in range(n):
        so = int(input(f"Nhap phan tu thu {i+1}: "))
        arr.append(so)

    tong_nt = 0
    for x in arr:
        if kiem_tra_nguyen_to(x):
            tong_nt += x
    
    print(f"Tong cac so nguyen to la: {tong_nt}")
    
    # Kiem tra Dieu kien: so le va > 50
    if tong_nt % 2 != 0 and tong_nt > 50:
        print("=> Thoa man: La so le va lon hon 50.")
    else:
        print("=> Khong thoa man Dieu kien.")

# Goi module cau 7
# giai_cau_7()

# Cau 8 Viet chuong trinh nhap vao ba so nguyen duong x, y, z, sau Do tim xem tich (x * y * z) co may chu so va chu so lon nhat bang bao nhieu.


# Cau 9 Viet chuong trinh nhap vao ba so nguyen duong a, b, c, sau Do tinh tong (a + b + c) va kiem tra xem trong tong Do co bao nhieu chu so chan
