import os
import datetime
import re
from itertools import groupby

def main(path_floder,path_file):
    # print(path_floder,path_file)
    if path_floder == [] or path_file == []:
        return ('请输入有效路径')
    nnn = 0
    lll = 0
    ggg = []
    # print('454545')
    for eee in range(1,len(path_floder)):
        path_file.append(path_file[0])
    # print(path_floder,path_file)
    for fff in path_floder:
        files_1 = os.listdir(fff)
        for m, file_mm in enumerate(files_1):
            if file_mm.split('.')[-1].lower() == 'jpg':
                nnn += 1
    # print('26')
    file_2 = open(path_file[0], mode='r')
    file_data_2 = file_2.readlines()
    for data_ll in file_data_2:
        a = re.split(",|\t| |\n", data_ll)
        ddd = []
        for hhh in range(len(a)):
            ddd.append(a[hhh])
        # print(b[0])
        ss_0 = [''.join(list(g)) for k, g in groupby(ddd[0], key=lambda x: x.isdigit())]
        ddd[0] = ss_0[-1]
        # print(ddd[0])
        if len(ddd) >4:
            for ttt in range(len(ddd[0])):
                if ddd[0][ttt] != '0':
                    ddd[0] = ddd[0][ttt:]
                    break
            ggg.append(ddd[0])
    # print(c)
    for mmm in ggg:
        if mmm.isdigit() == True:
            lll += 1
    # print(lll)
    if nnn == lll:
        now = datetime.datetime.now()
        file_name = get_desk_p() + '/' + now.strftime("%Y-%m-%d_%H_%M_%S") + 'pos_new' + '.txt'
        name = []
        for i in range(len(path_floder)):
            files = os.listdir(path_floder[i])

            for m, file in enumerate(files):
                if file.split('.')[-1].lower() == 'jpg':
                    ss_0 = [''.join(list(g)) for k, g in groupby(file, key=lambda x: x.isdigit())]
                    file = ss_0[-2]
                    for j in range(len(file)):
                        if file[j] != '0':
                            number = file[j:].split('.')[0]
                            name.append(number)
                            break
        file = open(path_file[0], mode='r')
        b = []
        uuu = 0
        file_data = file.readlines()
        for data in file_data:
            a = re.split(",|\t| |\n", data)
            # print(a)
            ss_0 = [''.join(list(g)) for k, g in groupby(a[0], key=lambda x: x.isdigit())]
            a[0] = ss_0[-1]
            if len(a) > 4:
                if a[0].isdigit() == True:
                    b.append(a)
        for name_i in name:
            try:
                b[uuu][0] = path_floder[0].split('\\')[-1]+'_' + '%010d' % int(name_i)
                try:
                    for data_j in b[uuu][0:7]:
                        data_j.replace('\n','')
                        open(file_name, 'a+').write(data_j + '\t')
                    open(file_name, 'a+').write('\n')
                except:
                    for data_j in b[uuu][0:3]:
                        data_j.replace('\n', '')
                        open(file_name, 'a+').write(data_j + '\t')
                    open(file_name, 'a+').write('\n')
            except:
                pass
            uuu += 1
        # print(file_name)
        return file_name



    else:
        try:
            now = datetime.datetime.now()
            # print(now)
            file_name = get_desk_p() + '/' + now.strftime("%Y-%m-%d_%H_%M_%S") + 'pos_new' + '.txt'
            for i in range(len(path_floder)):
                files = os.listdir(path_floder[i])
                name = []

                for m, file in enumerate(files):
                    if file.split('.')[-1].lower() == 'jpg':
                        # print(file)
                        ss_0 = [''.join(list(g)) for k, g in groupby(file, key=lambda x: x.isdigit())]
                        file = ss_0[-2]
                        for j in range(len(file)):
                            if file[j] != '0':
                                number = file[j:].split('.')[0]
                                name.append(number)
                                break
                # print(name)

                file = open(path_file[i], mode='r')
                # print(path_file[i])
                file_data = file.readlines()

                Num_kk = 0
                for data in file_data:
                    a = re.split(",|\t| |\n", data)
                    b = []
                    for mm in range(len(a)):
                        b.append(a[mm])
                    # print(a[0])
                    ss_0 = [''.join(list(g)) for k, g in groupby(b[0], key=lambda x: x.isdigit())]
                    b[0] = ss_0[-1]
                    yyy = []
                    if len(b) >4:
                        if b[0].isdigit() == True:
                            for bbb in range(len(b[0])):
                                if b[0][bbb] != '0':
                                    b[0] = b[0][bbb:]
                                    yyy = b
                                    break
                    # print(b)
                    # print(yyy)
                    # print(data.split()[0:7])
                    # print(b[0])
                    # print(b)
                    Num_ll = 0
                    try:
                        for name_i in name:
                            # print(name_i)
                            if name_i == yyy[0]:
                                try:
                                    data_7 = yyy[0:7]
                                    # print(data_7[0])
                                    data_7[0] = path_floder[i].split('\\')[-1]+'_' + '%010d' % int(name_i)
                                    # print(data_7)
                                    for data_j in data_7:
                                        data_j.replace('\n', '')
                                        open(file_name, 'a+').write(data_j+'\t')
                                    open(file_name, 'a+').write('\n')
                                    break
                                except:
                                    data_3 = yyy[0:3]
                                    data_3[0] = path_floder[i].split('\\')[-1] + '_' + '%010d' % int(name_i)
                                    for data_j in data_3:
                                        data_j.replace('\n', '')
                                        open(file_name, 'a+').write(data_j + '\t')
                                    open(file_name, 'a+').write('\n')
                                    break
                            elif Num_ll == len(name) - 1:
                                try:
                                    data_7 = yyy[0:7]
                                    # print(data_7[0])
                                    data_7[0] = path_floder[i].split('\\')[-1]+'_' + '%010d' % int(name[Num_kk])
                                    # print(data_7)
                                    for data_j in data_7:
                                        data_j.replace('\n', '')
                                        open(file_name, 'a+').write(data_j+'\t')
                                    open(file_name, 'a+').write('\n')
                                    break
                                except:
                                    data_3 = yyy[0:3]
                                    data_3[0] = path_floder[i].split('\\')[-1] + '_' + '%010d' % int(name[Num_kk])
                                    for data_j in data_3:
                                        data_j.replace('\n', '')
                                        open(file_name, 'a+').write(data_j + '\t')
                                    open(file_name, 'a+').write('\n')
                                    break
                            else:
                                pass
                            Num_ll += 1
                    except:
                        pass
                    Num_kk += 1
            # print('写入完成,请更换文件夹与pos')
            # print('输出路径为：', file_name)
            # print(file_name)
            return file_name
        except:
            # print('手动输入该路径，复制路径是默认添加了什么未知的前缀')
            return ('存储失败')

def get_desk_p():
    return os.path.join(os.path.expanduser('~'),"Desktop")

if __name__ == '__main__':
    path_floder = input('请输入文件夹路径：')
    path_file = input('请输入pos文件路径：')
    main(path_floder,path_file)