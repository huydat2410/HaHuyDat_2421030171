#Nhap vao 1 ma tran co m hang va n cot. Ghi ma tran vua nhap vao file "ma_tran.txt" o o Dia C
m = int(input('Nhap so hang:'))
n = int(input('Nhap so cot:'))
obj = open("ma_tran.txt", "w")
for i in range(m):
    for j in range(n):
        x = int(input("Nhap phan tu thu [" + str(i) + "][" + str(j) + "]: "))
        obj.write(str(x) + " ")
    obj.write("\n")
obj.close()
