#viet chuong trinh nhap vao 1 so nguyen duong n, kiem tra xem tich cac chu so cua n co phai la so chan va lon hon 20 khong?
class bai3:
    def __init__(self):
        self.n = int(input("Nhap so n: "))
    def tinh(self):
        tich = 1
        for i in str(self.n):
            tich *= int(i)
        if tich % 2 == 0 and tich > 20:
            return "Tich cac chu so cua {} la {}, la so chan va lon hon 20".format(self.n, tich)
        else:
            return "Tich cac chu so cua {} la {}, khong thoa man Dieu kien".format(self.n, tich)
b = bai3()
print(b.tinh())

#
n = int(input("Nhap n: "))
tich = 1
while n > 0:
    tich *= n % 10
    n //= 10

if tich % 2 == 0 and tich > 20:
    print("Tich cac chu so la",tich, "so chan va lon hon 20")
else:
    print("Tich cac chu so la",tich, "khong thoa man Dieu kien")