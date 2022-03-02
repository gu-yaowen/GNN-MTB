from tkinter import *
from tkinter import *
import tkinter
import tkinter.messagebox
import easygui
import pandas as pd
import os


from predict import Predict


def run2():
    # txt_input.delete(1.0, END)
    file_dir = inpl2.get(1.0, END).strip('\n')
    if os.path.exists(file_dir.strip('\n')):
        try:
            file = pd.read_csv(file_dir)
        except:
            file = pd.read_csv(file_dir, encoding='gbk')
    else:
        easygui.msgbox('请输入正确的待分析物质文件路径!')
        return
    # n = file.head(5)['SMILES'].values.tolist()
    n = file.head(5).values.tolist()
    for item in n:
        List_input.insert(END, n)
    txt_output.delete(1.0, END)
    save_dir = inpl4.get(1.0, END).strip('\n')
    if os.path.exists(save_dir):
        tkinter.messagebox.showerror(title='错误', message='该文件已存在')
    else:
        try:
            output = Predict(file_dir, save_dir)
            txt_output.insert(END, output)
            inpl4.delete(1.0, END)
        except:
            tkinter.messagebox.showerror(title='错误', message=file_dir + save_dir)


####################################################################################
win = Tk()
win.title('GNN-TB:基于图神经网络的抗结核杆菌药物虚拟筛选模型')
win.geometry('800x600')

bg_color = "#2f6477"

frame = Frame(win, relief=RAISED, borderwidth=2, width=600, height=300, bg=bg_color)
frame.pack(side=TOP, fill=BOTH, ipadx=5, ipady=5, expand=1)

###############################################################################
lb2 = Label(win, text='待预测物质路径')
lb2.place(x=250, y=100, anchor=W, width=100, height=30)
inpl2 = Text(win)
inpl2.place(x=350, y=100, anchor=W, width=200, height=30)

lb4 = Label(win, text='结局保存路径', font=('宋体', 10))
lb4.place(x=250, y=150, anchor=W, width=100, height=30)
inpl4 = Text(win)
inpl4.place(x=350, y=150, anchor=W, width=200, height=30)
#############控件##############################################################
# y预测按钮
button2 = Button(win, text="执行", font=('宋体', 20), fg='red', command=run2)
button2.place(x=375, y=250, anchor=W, width=100, height=40)
# 输入分子框标签
L_input = Label(win, text="待预测分子列表", font=('宋体', 20), fg='red')
L_input.place(x=100, y=300, width=200, height=40)
# 输出分子框标签
L_output = Label(win, text="预测结局列表", font=('宋体', 20), fg='red')
L_output.place(x=550, y=300, width=200, height=40)
##############################################################################
# 输入分子
List_input = Listbox(win)
List_input.place(x=100, y=350, width=200, height=200)
# 输出概率
txt_output = Text(win)
txt_output.place(x=550, y=350, width=200, height=200)

######################## icon and bg #####################################
ico_path = 'fig\\favicon.ico'

if os.path.exists(ico_path):
    win.iconbitmap(ico_path)

bg_path = 'fig\\bg.png'
if os.path.exists(bg_path):
    bg_image = PhotoImage(file=bg_path)
    Label(frame, image=bg_image).place(x=0, y=0)

# ini()
win.mainloop()