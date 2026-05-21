def giai_cau_9(a, b, c):
    kq_tong = a + b + c
    print(f"Tong la: {kq_tong}")

    dem_chan = 0
    for ky_tu in str(kq_tong):
        if int(ky_tu) % 2 == 0:
            dem_chan += 1
            
    print(f"So luong chu so chan trong tong la: {dem_chan}")

# Goi module cau 9
# giai_cau_9()
