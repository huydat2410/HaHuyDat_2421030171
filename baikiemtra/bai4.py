#Viet chg trinh nhap 2 so nguyen duong a ,b.Tinh tong a+b va in ra chu so lon nhat trong tong Do
class bai4:
    def __init__(self):
        self.a = int(input("Nhap so nguyen duong a: "))
        self.b = int(input("Nhap so nguyen duong b: "))
    def tinh(self):
        kq_tong = self.a + self.b
        max_digit = max(str(kq_tong))
        return "Tong cua {} va {} la {}, chu so lon nhat trong tong la {}".format(self.a, self.b, kq_tong, max_digit)
b = bai4()
print(b.tinh())

#
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
s = a + b
max = 0
while s > 0:
    temp = s % 10
    if temp > max:
        max = temp
    s //= 10
print("Chu so lon nhat la ", max)
