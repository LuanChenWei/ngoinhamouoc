can=['Canh','Tân','Nhâm','Quý','Giáp','Ất','Bính','Đinh','Mậu','Kỷ']

chi = ['Thân', 'Dậu', 'Tuất', 'Hợi','Tí','Sửu','Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', 'Mùi']

a=int(input('Nhập số năm: '))


index_can=a % 10

index_chi=a % 12

print(index_can,index_chi)

print(can[index_can]+ " " + chi[index_chi])
