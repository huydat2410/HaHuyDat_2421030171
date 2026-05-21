def giai_cau_8(x, y, z):
    tich = x * y * z
    print(f"Tich la: {tich}") 

    chuoi_tich = str(tich)
    print(f"So luong chu so: {len(chuoi_tich)}")

    max_chu_so = 0
    for ky_tu in chuoi_tich:
        so = int(ky_tu)
        if so > max_chu_so:
            max_chu_so = so
            
    print(f"Chu so lon nhat la: {max_chu_so}")

# Goi module cau 8
# giai_cau_8()