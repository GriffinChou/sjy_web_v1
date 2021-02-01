from itertools import groupby
import os
import re

def main(path,path_file):
    try:
        files = os.listdir(path)   # 读入文件夹
        num_png = 0
        aaa = []
        for i in files:
            if i.split('.')[-1].lower() == 'jpg':
                num_png += 1      # 统计文件夹中的文件个数
                aaa.append(i)
        # print(num_png)
        # print(aaa)
        file = open(path_file, mode='r')
        file_data = file.readlines()
        # num_pos = len(file_data)-2
        # print(num_pos)
        num_pos = 0
        c = []
        for data in file_data:
            a = re.split(",|\t| ", data)
            b = []
            for k in range(len(a)):
                b.append(a[k])
            # print(b[0])
            ss_0 = [''.join(list(g)) for k, g in groupby(b[0], key=lambda x: x.isdigit())]
            b[0] = ss_0[-1]
            if len(b) > 4:
                for bbb in range(len(b[0])):
                    if b[0][bbb] != '0':
                        b[0] = b[0][bbb:]
                        break
                c.append(b[0])
        # print(c)
        kkk = []
        for mmm in c:
            if mmm.isdigit() == True:
                kkk.append(mmm)
                num_pos += 1
        # print(num_pos)
        # print(kkk)
        if num_png != num_pos:
            if 4*num_png < num_pos:
                if 5*num_png == num_pos:
                    for i in range(num_png - 1):
                        ss_0 = [''.join(list(g)) for k, g in groupby(files[i], key=lambda x: x.isdigit())]
                        ss_1 = [''.join(list(g)) for k, g in groupby(files[i + 1], key=lambda x: x.isdigit())]
                        if int(ss_1[-2]) - int(ss_0[-2]) == 1:
                            pass
                        else:
                            # print('在这个文件夹下面',path)
                            # print('这张照片存在断裂', files[i] + '之间' + file[i + 1])
                            return ('五倍数目对齐,在这个文件夹下面%s，照片存在断裂，是在%s之间%s' % (path, files[i], file[i + 1]))

                    for i in range(num_pos-1):
                        if int(kkk[i + 1]) - int(kkk[i]) == 1:
                            pass
                        else:
                            # print('在这个pos下面',path_file)
                            # print('pos在这里存在断裂', datas[i] + '之间' + datas[i + 1])
                            return ('五倍数目对齐,在这个pos文件下面%s,pos存在断裂，是在%s之间%s,pos的数目有%s' % (path_file, kkk[i], kkk[i + 1],num_pos))
                    return ('五倍数目已经对齐请点击下一步，下一步为文件的重新命名与新pos的更新')

                else:
                    for i in range(num_png - 1):
                        ss_0 = [''.join(list(g)) for k, g in groupby(files[i], key=lambda x: x.isdigit())]
                        ss_1 = [''.join(list(g)) for k, g in groupby(files[i + 1], key=lambda x: x.isdigit())]
                        if int(ss_1[-2]) - int(ss_0[-2]) == 1:
                            pass
                        else:
                            # print('在这个文件夹下面', path)
                            # print('这张照片存在断裂', files[i] + '之间' + file[i + 1])
                            return ('5倍数目对不齐,在这个文件夹下面%s，照片存在断裂，是在%s之间%s' % (path, files[i], file[i + 1]))

                    for i in range(num_pos-1):
                        if int(kkk[i + 1]) - int(kkk[i]) == 1:
                            pass
                        else:
                            # print('在这个pos下面', path_file)
                            # print('pos在这里存在断裂', datas[i] + '之间' + datas[i + 1])
                            return ('5倍数目对不齐,在这个pos文件下面%s,pos存在断裂，是在%s之间%s,pos的数目有%s' % (path_file, kkk[i], kkk[i + 1],num_pos))
                    return ('对不起5倍数目对不齐，都不存在断裂，这种情况我之后的数据处理不了了，请你检查是否有一些人为删除的数据，请你把那些删除的数据补充回来pos数目为%s'%num_pos)


            try:
                for i in range(num_png-1):
                    ss_0 = [''.join(list(g)) for k, g in groupby(files[i], key=lambda x: x.isdigit())]
                    ss_1 = [''.join(list(g)) for k, g in groupby(files[i+1], key=lambda x: x.isdigit())]
                    if int(ss_1[-2]) - int(ss_0[-2]) == 1:
                        pass
                    else:
                        # print('在这个文件夹下面', path)
                        # print('这张照片存在断裂', files[i]+'之间'+file[i+1])
                        return ('数目对不齐,在这个文件夹下面%s，照片存在断裂，是在%s之间%s'% (path,files[i],file[i+1]))

                for i in range(num_pos-1):
                    if int(kkk[i+1])-int(kkk[i]) == 1:
                        pass
                    else:
                        # print('在这个pos下面', path_file)
                        # print('pos在这里存在断裂', datas[i]+'之间'+datas[i+1])
                        return ('数目对不齐,在这个pos文件下面%s,pos存在断裂，是在%s之间%s,pos的数目有%s'%(path_file, kkk[i], kkk[i+1],num_pos))
                # print('数目对不齐')
                return ('数目对不齐,都不存在断裂，请你看看是否文件不对,文件数目%s张，pos的数目有%s'%(num_png,num_pos))

            except:
                # print('照片与pos都不存在断裂，但数目不匹配，请人工检查照片与pos的开头与结尾的错误')
                return ('照片与pos都不存在断裂，但数目不匹配，请人工检查照片与pos的错误,pos的数目有%s,文件数目%s张'%(num_pos,num_png))

        else:
            try:
                for i in range(num_png - 1):
                    ss_0 = [''.join(list(g)) for k, g in groupby(files[i], key=lambda x: x.isdigit())]
                    ss_1 = [''.join(list(g)) for k, g in groupby(files[i + 1], key=lambda x: x.isdigit())]
                    if int(ss_1[-2]) - int(ss_0[-2]) == 1:
                        pass
                    else:
                        # print('在这个文件夹下面', path)
                        # print('这张照片附近存在断裂', files[i]+'之间'+file[i+1])
                        return ('数目对齐,在这个文件夹下面%s，照片存在断裂，是在%s之间%s' % (path, files[i], file[i + 1]))

                for i in range(num_pos-1):
                    # print(datas[i+1])
                    if int(kkk[i + 1]) - int(kkk[i]) == 1:
                        pass
                    else:
                        # print('在这个pos下面', path_file)
                        # print('pos在这里附近存在断裂', datas[i]+'之间'+datas[i+1])
                        return ('数目对齐,在这个pos文件下面%s,pos存在断裂，是在%s之间%s,pos的数目有%s' % (path_file, kkk[i], kkk[i + 1],num_pos))
            except:
                print('这个之后不存在Id', kkk[i])

            # print('数目以对齐，都不存在断裂的情况，请你自己看情况进行下一步操作，下一步为文件的重新命名与新pos的更新')
            return ('数目以对齐，都不存在断裂的情况，请你自己看情况进行下一步操作，下一步为文件的重新命名与新pos的更新')
    except:
        print('没有路径')


if __name__ == '__main__':
    path = input('请输入文件夹路径：')
    path_file = input('请输入pos的路径：')
    main(path, path_file)