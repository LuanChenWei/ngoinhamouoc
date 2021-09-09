# list = ['Nguyen','Tra','Quoc','Chung']
#
# for i in list:
#     print('Happy new year, ', i, '!', sep='')
#
list = [
    ['hoten1','gioitinh1','tp1','30','55'],
    ['hoten2','gioitinh2','tp2','70','80'],
    ['hoten3','gioitinh3','tp3','99','1']
]
# print(list[1][1])
def luachon():
    print('''Lua chon
    1) Them thong tin hoc vien vao list
    2) Hien thi danh sach tat ca hoc vien
    3) Xoa thong tin hoc vien'''
    )
    global chonso
    chonso = int(input('lua chon cua ban la: '))
    print('ban da chon: ', chonso)

def them():
    print('khong the them vi lap trinh vien khong biet lam!')

def hienthi(danhsach):
    for a in range(len(danhsach)):
        print(danhsach[a])

def xoa(danhsach,tencanxoa):
    for j in range(2):
        if tencanxoa == danhsach[j][0]:
            danhsach.pop(j)

    print('danh sach hoc sinh con lai: ', danhsach)


while 1:
    luachon()
    if chonso == 1:
        them()
    if chonso == 2:
        hienthi(list)
    if chonso == 3:
        chonten = (input('chon ten hs can xoa: '))
        xoa(list,chonten)