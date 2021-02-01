from tkinter import *
import ID_extract
import file_rename_1
import read_Size
import os
import re
from itertools import groupby

LOG_LINE_NUM = 0

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name


    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("无pos更名的小工具")           #窗口名
        #self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('1068x938+10+10')
        self.init_window_name["bg"] = "Indigo"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高


        #标签
        self.folder_input_1 = Label(self.init_window_name, text="请输入文件夹路径信息")
        self.folder_input_1.grid(row=0, column=0)
        self.pos_input_1 = Label(self.init_window_name, text="请输入pos文件路径")
        self.pos_input_1 .grid(row=0, column=12)
        self.mapping_input_1 = Label(self.init_window_name, text="匹配结果")
        self.mapping_input_1.grid(row=0, column=22)
        self.folder_input_2 = Label(self.init_window_name, text="请输入文件夹路径信息")
        self.folder_input_2.grid(row=4, column=0)
        self.pos_input_2 = Label(self.init_window_name, text="请输入pos文件路径")
        self.pos_input_2.grid(row=4, column=12)
        self.mapping_input_2 = Label(self.init_window_name, text="匹配结果")
        self.mapping_input_2.grid(row=4, column=22)
        self.folder_input_3 = Label(self.init_window_name, text="请输入文件夹路径信息")
        self.folder_input_3.grid(row=8, column=0)
        self.pos_input_3 = Label(self.init_window_name, text="请输入pos文件路径")
        self.pos_input_3.grid(row=8, column=12)
        self.mapping_input_3 = Label(self.init_window_name, text="匹配结果")
        self.mapping_input_3.grid(row=8, column=22)
        self.folder_input_4 = Label(self.init_window_name, text="请输入文件夹路径信息")
        self.folder_input_4.grid(row=12, column=0)
        self.pos_input_4 = Label(self.init_window_name, text="请输入pos文件路径")
        self.pos_input_4.grid(row=12, column=12)
        self.mapping_input_4 = Label(self.init_window_name, text="匹配结果")
        self.mapping_input_4.grid(row=12, column=22)
        self.folder_input_5 = Label(self.init_window_name, text="请输入文件夹路径信息")
        self.folder_input_5.grid(row=16, column=0)
        self.pos_input_5 = Label(self.init_window_name, text="请输入pos文件路径")
        self.pos_input_5.grid(row=16, column=12)
        self.mapping_input_5 = Label(self.init_window_name, text="匹配结果")
        self.mapping_input_5.grid(row=16, column=22)



        self.number_result_label = Label(self.init_window_name, text="各个文件夹的大小与照片数目")
        self.number_result_label.grid(row=21, column=0)
        self.New_result_label = Label(self.init_window_name, text="文件重命名pos导出结果，命名规则为文件名加下划线加计数")
        self.New_result_label.grid(row=21, column=12)
        self.file_path_result_label = Label(self.init_window_name, text="文件输出路径")
        self.file_path_result_label.grid(row=21, column=22)

        #文本框
        self.folder_input_1_Text = Text(self.init_window_name, width=40, height=9)  #原始数据录入框
        self.folder_input_1_Text.grid(row=1, column=0, rowspan=2, columnspan=8)
        self.pos_input_1_Text = Text(self.init_window_name, width=40, height=9)  # 日志框
        self.pos_input_1_Text.grid(row=1, column=12, rowspan=2, columnspan=8)
        self.mapping_input_1_Text = Text(self.init_window_name, width=40, height=9)  # 原始数据录入框
        self.mapping_input_1_Text.grid(row=1, column=20, rowspan=2, columnspan=8)
        self.folder_input_2_Text = Text(self.init_window_name, width=40, height=9)  # 原始数据录入框
        self.folder_input_2_Text.grid(row=5, column=0, rowspan=2, columnspan=8)
        self.pos_input_2_Text = Text(self.init_window_name, width=40, height=9)  # 日志框
        self.pos_input_2_Text.grid(row=5, column=12, rowspan=2, columnspan=8)
        self.mapping_input_2_Text = Text(self.init_window_name, width=40, height=9)  # 原始数据录入框
        self.mapping_input_2_Text.grid(row=5, column=20, rowspan=2, columnspan=8)
        self.folder_input_3_Text = Text(self.init_window_name, width=40, height=9)  # 原始数据录入框
        self.folder_input_3_Text.grid(row=9, column=0, rowspan=2, columnspan=8)
        self.pos_input_3_Text = Text(self.init_window_name, width=40, height=9)  # 日志框
        self.pos_input_3_Text.grid(row=9, column=12, rowspan=2, columnspan=8)
        self.mapping_input_3_Text = Text(self.init_window_name, width=40, height=9)  # 原始数据录入框
        self.mapping_input_3_Text.grid(row=9, column=20, rowspan=2, columnspan=8)
        self.folder_input_4_Text = Text(self.init_window_name, width=40, height=9)  # 原始数据录入框
        self.folder_input_4_Text.grid(row=13, column=0, rowspan=2, columnspan=8)
        self.pos_input_4_Text = Text(self.init_window_name, width=40, height=9)  # 日志框
        self.pos_input_4_Text.grid(row=13, column=12, rowspan=2, columnspan=8)
        self.mapping_input_4_Text = Text(self.init_window_name, width=40, height=9)  # 原始数据录入框
        self.mapping_input_4_Text.grid(row=13, column=20, rowspan=2, columnspan=8)
        self.folder_input_5_Text = Text(self.init_window_name, width=40, height=9)  # 原始数据录入框
        self.folder_input_5_Text.grid(row=17, column=0, rowspan=2, columnspan=8)
        self.pos_input_5_Text = Text(self.init_window_name, width=40, height=9)  # 日志框
        self.pos_input_5_Text.grid(row=17, column=12, rowspan=2, columnspan=8)
        self.mapping_input_5_Text = Text(self.init_window_name, width=40, height=9)  # 原始数据录入框
        self.mapping_input_5_Text.grid(row=17, column=20, rowspan=2, columnspan=8)

        self.number_result_Text = Text(self.init_window_name, width=40, height=9)  # 处理结果展示
        self.number_result_Text.grid(row=22, column=0, rowspan=2, columnspan=8)
        self.New_result_Text = Text(self.init_window_name, width=40, height=9)  # 处理结果展示
        self.New_result_Text.grid(row=22, column=12, rowspan=2, columnspan=8)
        self.file_path_result_Text = Text(self.init_window_name, width=40, height=9)  # 处理结果展示
        self.file_path_result_Text.grid(row=22, column=22, rowspan=2, columnspan=8)


        #按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="pos整理", bg="lightblue", width=10,
                                              command=self.than_pos)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=1, column=11)

        self.pos_trans_to_md5_button = Button(self.init_window_name, text="文件重命名pos导出", bg="lightblue", width=15,
                                              command=self.Rname)  # 调用内部方法  加()为直接调用
        self.pos_trans_to_md5_button.grid(row=20, column=11)


    def than_pos(self):
        try:
            floder_src_1 = self.folder_input_1_Text.get(1.0,END).strip().replace("  " or "\n","")
            pos_src_1 = self.pos_input_1_Text.get(1.0,END).strip().replace("  " or "\n","")
            # print(floder_src_1)
            floder_src_2 = self.folder_input_2_Text.get(1.0, END).strip().replace("  " or "\n", "")
            pos_src_2 = self.pos_input_2_Text.get(1.0, END).strip().replace("  " or "\n", "")
            # print(floder_src_2)
            floder_src_3 = self.folder_input_3_Text.get(1.0, END).strip().replace("  " or "\n", "")
            pos_src_3 = self.pos_input_3_Text.get(1.0, END).strip().replace("  " or "\n", "")
            # print(floder_src_3)
            floder_src_4 = self.folder_input_4_Text.get(1.0, END).strip().replace("  " or "\n", "")
            pos_src_4 = self.pos_input_4_Text.get(1.0, END).strip().replace("  " or "\n", "")
            # print(floder_src_4)
            floder_src_5 = self.folder_input_5_Text.get(1.0, END).strip().replace("  " or "\n", "")
            pos_src_5 = self.pos_input_5_Text.get(1.0, END).strip().replace("  " or "\n", "")
            # print(floder_src_5)

            aa_1 = [floder_src_1, floder_src_2, floder_src_3, floder_src_4, floder_src_5]
            bb_1 = [pos_src_1, pos_src_2, pos_src_3, pos_src_4, pos_src_5]
            aa_2 = []
            bb_2 = []
            for i in range(len(aa_1)):
                # print('aa')
                if aa_1[i] != '':
                    aa_2.append(aa_1[i])
                if bb_1[i] != '':
                    bb_2.append(bb_1[i])
            # print(len(aa_2))
            # print(len(bb_2))
            if len(aa_2) != len(bb_2):
                if len(bb_2) == 1:
                    # print('aa')
                    for i in range(1, len(aa_2)):
                        bb_2.append(bb_2[0])
                else:
                    self.mapping_input_1_Text.delete(1.0, END)
                    self.mapping_input_1_Text.insert(1.0, 'pos只支持一个或者与文件相同的pos输入')
                    # return self.mapping_input_1_Text
            # print(len(bb_2))
            # print(aa_2)
            # print(bb_2)
            if len(aa_2) == len(bb_2):
                self.aa = []
                self.bb = []
                self.number_result_Text.delete(1.0, END)

                for i in range(len(aa_2)):
                    self.aa.append(aa_2[i])
                    self.bb.append(bb_2[i])
                    # self.New_result_Text.delete(1.0, END)
                    size, number = read_Size.getFileSize(aa_2[i])
                    self.number_result_Text.insert(1.0, '这个文件夹的大小%sGB与照片数为%s张'%(size, number))
                    self.number_result_Text.insert(1.0, '\n')
                # print(self.aa,self.bb)
                nnn = 0
                lll = 0
                ggg = []
                # print('454545')
                for fff in self.aa:
                    files_1 = os.listdir(fff)
                    for m, file_mm in enumerate(files_1):
                        if file_mm.split('.')[-1].lower() == 'jpg':
                            nnn += 1
                # print('26')
                file_2 = open(self.bb[0], mode='r')
                file_data_2 = file_2.readlines()
                for data_ll in file_data_2:
                    a = re.split(",|\t| ", data_ll)
                    ddd = []
                    for hhh in range(len(a)):
                        ddd.append(a[hhh])
                    # print(b[0])
                    # ss_0 = [''.join(list(g)) for k, g in groupby(ddd[0], key=lambda x: x.isdigit())]
                    # ddd[0] = ss_0[-1]
                    # print(ddd[0])
                    for ttt in range(len(ddd[0])):
                        if ddd[0][ttt] != '0':
                            ddd[0] = ddd[0][ttt:]
                            break
                    ggg.append(ddd[0])
                # print(c)
                for mmm in ggg:
                    if mmm.isdigit() == True:
                        lll += 1
                if nnn == lll:
                    self.mapping_input_1_Text.delete(1.0, END)
                    self.mapping_input_1_Text.insert(1.0, '匹配结果：数目对齐' )
                else:
                    for i in range(len(self.bb)):
                        mipping_result = ID_extract.main(self.aa[i], self.bb[i])
                        if i == 0:
                            self.mapping_input_1_Text.delete(1.0, END)
                            self.mapping_input_1_Text.insert(1.0, '匹配结果：%s'%mipping_result)
                        if i == 1:
                            self.mapping_input_2_Text.delete(1.0, END)
                            self.mapping_input_2_Text.insert(1.0, '匹配结果：%s'%mipping_result)
                        if i == 2:
                            self.mapping_input_3_Text.delete(1.0, END)
                            self.mapping_input_3_Text.insert(1.0, '匹配结果：%s'%mipping_result)
                        if i == 3:
                            self.mapping_input_4_Text.delete(1.0, END)
                            self.mapping_input_4_Text.insert(1.0, '匹配结果：%s'%mipping_result)
                        if i == 4:
                            self.mapping_input_5_Text.delete(1.0, END)
                            self.mapping_input_5_Text.insert(1.0, '匹配结果：%s'%mipping_result)
                # return self.mapping_input_1_Text
            else:
                self.mapping_input_1_Text.delete(1.0, END)
                self.mapping_input_1_Text.insert(1.0, '输入的文件夹数目与pos数目不一致')
                # return self.mapping_input_1_Text
        except:
            self.mapping_input_1_Text.delete(1.0, END)
            self.mapping_input_1_Text.insert(1.0, '你在复制文件路径时前面出现了一点点问题，请你重新复制并粘贴' )
            # return self.mapping_input_1_Text


    def Rname(self):
        # print(self.aa, self.bb)
        self.file_path_result_Text.delete(1.0, END)
        self.pos_save_path = file_rename_1.file_rename(self.aa, self.bb)
        self.file_path_result_Text.insert(1.0, '\n文件保存路径为：%s'%self.pos_save_path)
        self.New_result_Text.delete(1.0, END)
        self.New_result_Text.insert(1.0, 'pos与更名完成')
        # return ('wangcheng')


def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()
    # init_window.withdraw()  # ****实现主窗口隐藏
    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


if __name__ == '__main__':
    gui_start()