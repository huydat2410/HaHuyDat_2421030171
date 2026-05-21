#Viet chuong trinh nhap vao 2 so nguyen duong m va n, sau Do tinh tong (a+b) va tim ra chu so lon nhat trong tong Do.
class tinh:
    def __init__(self):
        self.a = int(input("Nhap so nguyen duong a: "))
        self.b = int(input("Nhap so nguyen duong b: "))

    def kq_tong(self):
        return self.a + self.b

    def chu_so_lon_nhat(self):
        kq_tong = self.kq_tong()
        max_digit = 0
        while kq_tong > 0:
            digit = kq_tong % 10
            if digit > max_digit:
                max_digit = digit
            kq_tong //= 10
        return max_digit
c = tinh()
print("Tong cua a va b la: ", c.kq_tong())
print("Chu so lon nhat trong tong la: ", c.chu_so_lon_nhat())
