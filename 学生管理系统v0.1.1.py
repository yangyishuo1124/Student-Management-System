name = {'liming': [100, 65, 84]}
jishu1 = 0

import tkinter.messagebox
import requests
VERSION_NOW='v0.1.1'#0.1.1
UPDATE_DOWNLOAD_URL='https://myguthub.coding.net/api/user/myguthub/project/student-management-system/depot/Student-Management-System/git/releases/attachments/download/86079' #新版本文件
VERSION_URL='https://myguthub.coding.net/p/student-management-system/d/Student-Management-System/git/releases/3'#最新版本号

try:
    ver=request.get(VERSION_URL)#获取最新版本号
   #然后自己根据版本号对版本进行对比处理
    #这里省略
    #直接跳到更新代码
    tkinter.messagebox.showwarning(title='提示', message='发现新版本，点击确定开始更新。更新时间跟网速有关，请耐心等待！')
    newFile=requests.get(UPDATE_DOWNLOAD_URL)
    with open("newFile_update.zip","wb") as fp:
        fp.write(newFile.content)
except:
    tkinter.messagebox.showwarning(title='警告', message='更新失败，请检查网络！')
tkinter.messagebox.showwarning(title='提示', message='新版本软件下载完成！请在当前软件目录查看(文件名：newFile_update.zip)并使用新版本。') 
 

def  begin():
    print('填写所需选项的序号:')
    print('1: 列出所有成绩')
    print('2：增加或更改学生和成绩')
    print('3：删除学生')
    print('4：查找学生成绩')
    print('5：按成绩排名')
    #print('6：联网检查更新（未开发）')
    print('0：退出系统')


def allg():
    for i in name:
        allgrade = 0
        if len(name[i]) == 3:
            for q in name[i]:
                allgrade += int(q)
            name[i].append(allgrade)
        
print('欢迎使用学生管理系统v0.2.1\n©Copyright2021杨一朔.AllRightsReserved\n按回车键开始使用')
p = input()

while True:
    allg()
    begin()
    a = int(input('输入您的选项:'))


    if a == 1:
        print('(注：输出的顺序为:\n姓名 语文成绩 数学成绩 英语成绩 总分)')
        for stu in name:
            print(stu+':'+str(name[stu]))
        f = input('输入‘F’回到主菜单')
        if f == 'F':
            f = ''
            continue

    if (a == 2):
        while True:
            newname = str(input('请输入新学生或需要修改的学生名字：'))
            newgrade_Chinese = input('请输入Ta的语文成绩：')
            newgrade_Mach = input('请输入Ta的数学成绩：')
            newgrade_English = input('请输入Ta的英语成绩：')
            allnewgrade = [newgrade_Chinese, newgrade_Mach, newgrade_English]
            name.update({newname: allnewgrade})
            f = input('继续添加输入‘T’，回到主菜单输入‘F’\n请输入：')
            if (f == 'F'):
                break
            #bug标注
            if (f == 'T'):
                continue

    if (a == 3):
        while True:
            delname = input('请输入需要删除的学生名字:\n')
            if (delname in name):
                name.pop(delname)
                f = input('已删除,继续查询输入‘T’，返回主菜单输入‘F’\n请输入：')
                if f == 'F':
                    break
                else:
                    continue
            else:
                f = input('输入有误,继续查询输入‘T’，输入‘F’返回主菜单\n请输入：')
                if f == 'F':
                    break
                else:
                    continue

    if (a == 4):
        while True:
            findname = input('请输入需要查找成绩的学生名字:\n')
            if (findname in name):
                
                print(name[findname])
                f = input('已完成，继续查询输入‘T’，回到主菜单输入‘F’\n请输入：')
                if f == 'F':
                    break
                else:
                    continue
                
            else:
                f = input('输入有误，继续查询输入‘T’，输入‘F’返回主菜单\n请输入：')
                if f == 'F':
                    break
                else:
                    continue

    if (a == 5):
        paixu = {}
        name5 = name.copy()
        while len(name5) > 0:
            mix = 0
            mixname = ''
            for name1 in name5:
                allgrad = name5[name1][3]
                if allgrad > mix:
                    mix = allgrad
                    mixname = name1
            paixu.update({mixname: name5[mixname]})
            name5.pop(mixname)
        for stu in paixu:
            print(stu+':'+str(paixu[stu]))

    if (a == 0):
        print('期待您的下次使用')
        break
