import os
from photo_Nopos_record import pos_write
import re
from itertools import groupby

def file_rename(floder_path,path_file):
    try:
        floder_path = [i for i in floder_path if i != '']
        path_file = [i for i in path_file if i != '']
        # print(floder_path)
        # print(path_file)
        nnn = 0
        lll = 0
        ggg = []
        # print('454545')
        for fff in floder_path:
            files_1 = os.listdir(fff)
            for m, file_mm in enumerate(files_1):
                if file_mm.split('.')[-1].lower() == 'jpg':
                    nnn += 1
        # print('26')
        file_2 = open(path_file[0], mode='r')
        file_data_2 = file_2.readlines()
        for data_ll in file_data_2:
            a = re.split(",|\t| ", data_ll)
            ddd = []
            for hhh in range(len(a)):
                ddd.append(a[hhh])
            # print(b[0])
            ss_0 = [''.join(list(g)) for k, g in groupby(ddd[0], key=lambda x: x.isdigit())]
            ddd[0] = ss_0[-1]
            if len(ddd) > 4:
                for ttt in range(len(ddd[0])):
                    if ddd[0][ttt] != '0':
                        ddd[0] = ddd[0][ttt:]
                        break
                ggg.append(ddd[0])
        # print(c)
        for mmm in ggg:
            if mmm.isdigit() == True:
                lll += 1
        try:
            if nnn == lll:
                mm = 0
                for path in floder_path:
                    files = os.listdir(path)
                    for i, file in enumerate(files):
                        if file.split('.')[-1].lower() == 'jpg':
                            NewName = os.path.join(path, floder_path[0].split('\\')[-1] + '_' + '%010d' % (mm + 1) + '.jpg')
                            OldName = os.path.join(path, file)
                            os.rename(OldName, NewName)
                            mm += 1
            else:
                for path in floder_path:
                    files = os.listdir(path)
                    for i, file in enumerate(files):
                        if file.split('.')[-1].lower() == 'jpg':
                            NewName = os.path.join(path, path.split('\\')[-1] + '_' + '%010d' % (i + 1) + '.jpg')
                            OldName = os.path.join(path, file)
                            os.rename(OldName, NewName)
            # print('44546546')
            New_file_path = pos_write.main(floder_path,path_file)
            # print(New_file_path)
            return (New_file_path)
        except:
            # print('没有找到有效的pos路径')
            return ('没有找到有效的pos路径')
    except:
        return ('请输入有效路径')

if __name__=='__main__':
    path = input('请输入文件夹路径：')
    path_file = input('请输入pos文件路径：')
    file_rename(path, path_file)

# 请输入文件夹路径：S:\仰德\3
# 请输入pos文件路径：S:\仰德\pos解算后\2020-11-24 15-09-42_cam4_pos.txt