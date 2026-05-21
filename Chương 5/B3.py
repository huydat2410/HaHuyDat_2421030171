#Viet chuong trinh nhap vao 2 so nguyen duong a va b, sau Do kiem tra xem a co chia het cho chu so nho nhat cua b hay khong.
#Vi du: a = 24, b = 582, chu so nho nhat cua b la 2, va 24 chia het cho 2
class bai4:
    def __init__(self):
        self.a = int(input("Nhap so nguyen duong a: "))
        self.b = int(input("Nhap so nguyen duong b: "))

    def chu_so_nho_nhat(self):
        min_digit = 9
        while self.b > 0:
            digit = self.b % 10
            if digit < min_digit:
                min_digit = digit
            self.b //= 10
        return min_digit

    def kiem_tra_chia_het(self):
        min_digit = self.chu_so_nho_nhat()
        if min_digit == 0:
            return "Chu so nho nhat cua b la 0, khong the chia cho 0"
        elif self.a % min_digit == 0:
            return "a chia het cho chu so nho nhat cua b la {}".format(min_digit)
        else:
            return "a khong chia het cho chu so nho nhat cua b la {}".format(min_digit)
c = bai4()
print(c.kiem_tra_chia_het())
