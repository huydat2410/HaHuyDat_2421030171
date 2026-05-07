import module1
x = int(input("Nhap chieu dai hinh chu nhat:"))
y = int(input("Nhap chieu rong hinh chu nhat:"))
r = int(input("Nhap ban kinh hinh tron:"))
z = int(input("Nhap canh hinh vuong:"))
print("Dien tich hinh chu nhat:", module1.s_hcn(x, y))
print("Dien tich hinh vuong:", module1.s_hv(z))
print("Chu vi hinh chu nhat:", module1.c_hcn(x, y))
print("Dien tich hinh tron:", module1.s_ht(r))