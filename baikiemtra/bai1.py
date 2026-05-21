#iet chuong trinh nhap vao mot day so thuc x1, x2, …, xn (0 < n < 100), sau Do tim trung binh cong cac phan tu duong trong day ma gia tri nam trong khoang (0, 1000)
class tbc: 
    def __init__(self):
        self.n = int(input("Nhap so luong phan tu: "))
        self.a = []
        for i in range(self.n):
            self.a.append(float(input("Nhap phan tu thu {}: ".format(i + 1))))

    def tbcd(self):
        kq_tong = 0
        dem = 0
        for i in self.a:
            if 0 < i < 1000:
                kq_tong += i
                dem += 1
        if dem == 0:
            return "Khong co phan tu duong nao trong khoang (0,1000)"
        else:
            return kq_tong / dem
c = tbc()
print("Trung binh cong cac phan tu duong trong khoang (0,1000) la: ", c.tbcd())

#thuat toan:
n = int(input("Nhap so luong day: "))

kq_tong = 0
dem = 0

for i in range(n):
    x = int(input("Nhap so: "))

    if 0 < x < 1000:
        kq_tong += x
        dem += 1

if dem > 0:
    print("Trung binh cong cua day: ", kq_tong/dem)
else:
    print("TBC la:",kq_tong/dem, "Khong TM Dieu kien")
