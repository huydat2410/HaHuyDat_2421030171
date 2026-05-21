#Viet chuong trinh nhap vao mot day so nguyen x1, x2, …, xn (0 < n < 200), tinh tong cac phan tu chan trong day, va kiem tra xem tong nay co chia het cho 7 va nho hon 200 hay khong
class tinhsochan:
    def __init__(self):
        self.n = int(input("Nhap so luong phan tu: "))
        self.a = []
        for i in range(self.n):
            self.a.append(int(input("Nhap phan tu thu {}: ".format(i + 1))))

    def tong_so_chan(self):
        kq_tong = 0
        for i in self.a:
            if i % 2 == 0:
                kq_tong += i
        return kq_tong

    def kiem_tra(self):
        tong_chan = self.tong_so_chan()
        if tong_chan % 7 == 0 and tong_chan < 200:
            return "Tong cac phan tu chan la {} va no chia het cho 7 va nho hon 200".format(tong_chan)
        elif tong_chan % 7 == 0 and tong_chan > 200:
            return "Tong cac phan tu chan la {} va no chia het cho 7 nhung khong nho hon 200".format(tong_chan)
        elif tong_chan % 7 != 0 and tong_chan < 200:
            return "Tong cac phan tu chan la {} va no khong chia het cho 7 va nho hon 200".format(tong_chan)
        else:
            return "Tong cac phan tu chan la {} va no khong chia het cho 7 va khong nho hon 200".format(tong_chan)
c = tinhsochan()
print(c.kiem_tra())
