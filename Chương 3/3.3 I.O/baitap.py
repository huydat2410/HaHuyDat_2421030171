#viet chuong trinh Doc tep input.txt gom n dong, moi dong la 1 so tu nhien. ket qua chuong trinh la output gom n dong lan luot la cac uoc so nguyen to khac nhau
f = open("input.txt", "r")
fo = open("output.txt", "w")
s = f.readlines()
# for i in s:
#     num = int(i)
#     print("uoc so nguyen to cua", num, "la: ")
#     for j in range(2, num + 1):
#         if num % j == 0:
#             kt = True
#             for k in range(2, int(j**0.5) + 1):
#                 if j % k == 0: 
#                     kt = False
#                     break
#             if kt:
#                 print(j, " ")
for line in s:
    n = int(line)
    k = 2
    while n>1:
        while n%k !=0:
            k+=1
        if n%k == 0:
            print(k,file = fo, end = " ")
            n = n//k
    print(file = fo)
f.close()
fo.close()



