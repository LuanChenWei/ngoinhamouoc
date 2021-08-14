import math
usd = float(input("nhap so tien can chuyen sang vnd: "))
tygia = float(input("nhap ty gia hom nay: "))

vnd = usd*tygia

msg = "so tien chuyen doi tu {} usd la: {}"

print(msg.format(usd, vnd))
