#cho file input.txt gom cac kieu du lieu chu va so. Lap trinh output.txt gom outso.txt va outchu.txt
f = open("input.txt", "r")
f1 = open("outso.txt", "w")
f2 = open("outchu.txt", "w")
s = f.readlines()
for i in s:
    i = i.strip().split()
    for j in i:
        if j.isdigit():
            print(j, file = f1, end = " ")
        else:
            print(j, file = f2, end = " ")
f.close()
f1.close()
f2.close()
