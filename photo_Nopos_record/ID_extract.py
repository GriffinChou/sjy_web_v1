from itertools import groupby
import os
from photo_Nopos_record import file_than_pos
import re

def main(path,pos_file_path):
    files = os.listdir(path)   # 读入文件夹
    ID_png = []
    for i in files:
        if i.split('.')[-1].lower() == 'jpg':
            ss_0 = [''.join(list(g)) for k, g in groupby(i, key=lambda x: x.isdigit())]
            a = ss_0[-2]
            for j in range(10):
                if a[j] != '0':
                    number = a[j:]
                    ID_png.append(number)
                    break
    # print(ID_png)
    ID_png = set(ID_png)
    # print(ID_png)
    c = []
    file = open(pos_file_path, mode='r')
    file_data = file.readlines()
    # print(file_data)
    for data in file_data:
        a = re.split(",|\t| ", data)
        b = []
        for k in range(len(a)):
            b.append(a[k])
        # print(b[0])
        ss_0 = [''.join(list(g)) for k, g in groupby(b[0], key=lambda x: x.isdigit())]
        b[0] = ss_0[-1]
        # print(b[0])
        if len(b) > 4:
            for bbb in range(len(b[0])):
                if b[0][bbb] != '0':
                    b[0] = b[0][bbb:]
                    break
            c.append(b[0])

    ID_pos = c
    # print(ID_pos)

    ID_pos = set(ID_pos)
    # print(ID_pos)
    # print(ID_png-ID_pos)
    if ID_png-ID_pos == set() and ID_pos - ID_png == set():
        # print('已完全匹配,可进行下一步操作,下一步为照片的重命名与pos修改')
        return ('已完全匹配,可进行下一步操作,下一步为照片的重命名与pos修改')

    else:
        # print('ID完全匹配不成功，进入下一步文件数目的比较')
        data_map = file_than_pos.main(path,pos_file_path)
        # print(data_file_pos, number_1,number_2)
        # print(data_map)
        return data_map

if __name__ == '__main__':
    path = 'S:/托德/2'
    pos_file_path = 'S:/托德/pos解算后/2020-11-24 14-46-12_cam2_pos.txt'
    main(path,pos_file_path)