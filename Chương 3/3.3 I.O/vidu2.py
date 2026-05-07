#nhap 1 day so nguyen gom n phan tu. Ghi dy so vua nhap vao file "dulieu.txt" o o Dia C
n = int(input("nhap n: "))
obj = open("dulieu.txt", "w")
for i in range(n):
    x = int(input("nhap phan tu thu " + str(i+1) + ": "))
    obj.write(str(x) + " ")
obj.close()
