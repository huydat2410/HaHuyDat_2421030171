#viet chuong trinh nhap vao 1 so nguyen duong n, kiem tra xem tong cac chu so cua n co phai la so chia het cho 3 khong?
class bai2: 
    def __init__(self):
        self.n = int(input("Nhap so n: "))
    def tinh(self):
        kq_tong = 0
        for i in str(self.n):
            kq_tong += int(i)
        if kq_tong % 3 == 0:
            print("Tong cac chu so cua {} la {}, chia het cho 3".format(self.n, kq_tong))
        else:
            print("Tong cac chu so cua {} la {}, khong chia het cho 3".format(self.n, kq_tong))
b = bai2()
print(b.tinh())

#Don gian: 
n = int(input("Nhap n: "))
kq_tong = 0
while n>0:
    kq_tong += n%10
    n //= 10
if kq_tong % 3 ==0:
    print("Tong cac chu so chia het cho 3")
else:
    print("Tong cac chu so khong chia het cho 3")
