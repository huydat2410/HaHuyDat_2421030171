# class Circle:
#     def Dientich(self):
#         return self.bk * self.bk * 3.141592
#     def Nhap(self):
#         self.bk = float(input("Nhap ban kinh: "))
# c = Circle()
# c.Nhap()
# print("Dien tich hinh tron la: ", c.Dientich())

class Circle:
    p = 3.141592
    def __init__(self, radius = 1):
        self.bk = radius
        def Dientich(self):
            return self.bk * self.bk * Circle.pi
c = Circle(5)
print("Dien tich hinh tron la: ", c.Dientich())
