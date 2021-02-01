import os

def getFileSize(filePath, size=0,number=0):
    try:
        for root, dirs, files in os.walk(filePath):
            for f in files:
                if f.split('.')[-1].lower() == 'jpg':
                    size += os.path.getsize(os.path.join(root, f))
                    number += 1
        return round(size/1024/1024/1024, 3), number
    except:
        print('请输入正确的文件路径')

if __name__ =="__main__":
    path = input('请输入文件夹的路径：')
    Size, number = getFileSize(path)
    print('字节大小为：', Size, number)