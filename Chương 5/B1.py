#iet chuong trinh nhap vao mot day so thuc x1, x2, …, xn (0 < n < 100), sau Do tim trung binh cong cac phan tu am trong day ma gia tri nam trong khoang (-1000, -10)
class tbc: 
    def __init__(self):
        self.n = int(input("Nhap so luong phan tu: "))
        self.a = []
        for i in range(self.n):
            self.a.append(float(input("Nhap phan tu thu {}: ".format(i + 1))))

    def tbc_am(self):
        kq_tong = 0
        dem = 0
        for i in self.a:
            if i < 0 and -1000 < i < -10:
                kq_tong += i
                dem += 1
        if dem == 0:
            return "Khong co phan tu am nao trong khoang (-1000, -10)"
        else:
            return kq_tong / dem
c = tbc()
print("Trung binh cong cac phan tu am trong khoang (-1000, -10) la: ", c.tbc_am())
