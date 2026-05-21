#viet chg trinh nhap 2 so nguyen duong m,n kiem tra xem m co chia het tong chu so cua n khong?
class bai5:
    def __init__(self):
        self.m = int(input("Nhap so nguyen duong m: "))
        self.n = int(input("Nhap so nguyen duong n: "))
    def tinh(self):
        kq_tong = 0
        for i in str(self.n):
            kq_tong += int(i)
        if self.m % kq_tong == 0:
            return "{} chia het tong chu so cua {} la {}".format(self.m, self.n, kq_tong)
        else:
            return "{} khong chia het tong chu so cua {} la {}".format(self.m, self.n, kq_tong)
b = bai5()
print(b.tinh())

#
m = int(input("Nhap m: "))
n = int(input("Nhap n: "))
kq_tong = 0
temp = n
while temp > 0:
    kq_tong = kq_tong + temp % 10
    temp //= 10
if m % kq_tong == 0:
    print(f"{m} chia het cho tong cua chu so {n} la {kq_tong}")
else:
    print(f"{m} khong chia het cho tong cua chu so {n} la {kq_tong}")
