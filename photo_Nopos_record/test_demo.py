from photo_Nopos_record import ID_extract
from photo_Nopos_record import read_Size
import os
import re
from itertools import groupby

class ksa():
    def __init__(self,floder_path,pos_path):
        self.floder_path = [i for i in floder_path if i !='']
        self.pos_path = [i for i in pos_path if i !='']
        # print(len(self.floder_path))
        # print(len(self.pos_path))

    def than(self):
        if self.pos_path ==[] or self.floder_path == []:
            result = []
            for i in range(10):
                if len(result) != 6:
                    result.append([0, 0])
                else:
                    break
            result.append(['文件路径出错，请重新复制粘贴'])
            return result
        try:
            if len(self.floder_path) != len(self.pos_path):
                # print('aaaa')
                if len(self.pos_path) == 1 and len(self.floder_path) != 1:
                    for i in range(1,len(self.floder_path)):
                        self.pos_path.append(self.pos_path[0])
                else:
                    result = []
                    for i in range(10):
                        if len(result) != 6:
                            result.append([0, 0])
                        else:
                            break
                    result.append(['文件路径出错，请重新复制粘贴'])
                    return result
            # print(self.floder_path)
            # print(self.pos_path)
            nnn = 0
            lll = 0
            ggg = []
            result = []
            # fileSize = 0
            # file_Number = 0
            # print('454545')
            for fff in self.floder_path:
                size,number = read_Size.getFileSize(fff)
                result.append([size,number])
                # print(size,number)
                files_1 = os.listdir(fff)
                for m, file_mm in enumerate(files_1):
                    if file_mm.split('.')[-1].lower() == 'jpg':
                        nnn += 1
            # print(nnn)
            # result.append([fileSize,file_Number])
            for i in range(10):
                if len(result) != 6:
                    result.append([0,0])
                else:
                    break
            file_2 = open(self.pos_path[0], mode='r')
            file_data_2 = file_2.readlines()
            # print(file_data_2)
            for data_ll in file_data_2:
                a = re.split(",|\t| |\n", data_ll)
                ddd = []
                for hhh in range(len(a)):
                    ddd.append(a[hhh])
                ss_0 = [''.join(list(g)) for k, g in groupby(ddd[0], key=lambda x: x.isdigit())]
                ddd[0] = ss_0[-1]
                # print(ddd)
                if len(ddd) >4:
                    for ttt in range(len(ddd[0])):
                        if ddd[0][ttt] != '0':
                            ddd[0] = ddd[0][ttt:]
                            break
                    ggg.append(ddd[0])
                    # print(ggg)
            for mmm in ggg:
                if mmm.isdigit() == True:
                    lll += 1
            # print(lll)
            if nnn == lll:
                result.append(['数目对齐'])
            else:
                for i in range(len(self.floder_path)):
                    result_1 = ID_extract.main(self.floder_path[i],self.pos_path[i])
                    result.append([result_1])
            return result
        except:
            result = []
            for i in range(10):
                if len(result) != 6:
                    result.append([0, 0])
                else:
                    break
            result.append(['文件路径出错，请重新复制粘贴'])
            return result

if __name__ == '__main__':
    floder_path = ['S:\仰德\\1','S:\仰德\\2','S:\仰德\\3']
    pos_path = ['S:\仰德\pos解算后\\2020-11-24 15-09-42_cam1_pos.txt']
    print(floder_path,pos_path)
    a =ksa(floder_path,pos_path)
    a.than()

