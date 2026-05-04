m = int (input ("Nhap so hang:"))
n = int (input ("Nhap so cot:"))
ma_tran = []
for i in range (m):
    hang = []
    for j in range (n):
        so = int ( input("Nhap phan tu thu [" + str (i) + "][" + str (j) + "]:"))
        hang.append(so)
    ma_tran.append(hang)

for i in range (m):
    for j in range (n):
        print (ma_tran[i][j],end= " ")
    print ()
