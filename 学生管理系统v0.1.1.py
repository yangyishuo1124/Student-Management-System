from typing import Match

import ptvsd
ptvsd.enable_attach(address = ('192.168.101.86', 3000))
ptvsd.wait_for_attach()

name = {'liming': [100, 65, 84]}
jishu1 = 0



print('欢迎使用学生管理系统v0.1.1\n©Copyright2021杨一朔.AllRightsReserved\n按回车键开始使用')
input()

while True:

    for i in name:
        allgrade = 0
    if len(name[i]) == 3:
        for q in name[i]:
            allgrade += int(q)
        name[i].append(allgrade)

    
    print('填写所需选项的序号:')
    print('1: 列出所有成绩')
    print('2：增加或更改学生和成绩')
    print('3：删除学生')
    print('4：查找学生成绩')
    print('5：按成绩排名（尚未开发）')
    print('0：退出系统')
    a = int(input('输入您的选项:'))


    if a == 1:
        print('(注：输出的顺序为:\n姓名 语文成绩 数学成绩 英语成绩 总分)')
        print(name)
        f = input('输入‘F’回到主菜单')
        if f == 'F':
            f =''
            continue

    if (a == 2):
        while True:
            newname = str(input('请输入新学生或需要修改的学生名字：'))
            newgrade_Chinese = input('请输入Ta的语文成绩：')
            newgrade_Mach = input('请输入Ta的数学成绩：')
            newgrade_English = input('请输入Ta的英语成绩：')
            allnewgrade = [newgrade_Chinese, newgrade_Mach, newgrade_English]
            name.update({newname: allnewgrade})
            for i in name:
                allgrade = 0
                if len(name[i]) == 3:
                    for q in name[i]:
                        allgrade += int(q)
                    name[i].append(allgrade)
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
                f=input('输入有误,继续查询输入‘T’，输入‘F’返回主菜单\n请输入：')
                if f == 'F':
                    break
                else:
                    continue

    if (a == 4):
        while True:
            for i in name:
                allgrade = 0
                if len(name[i]) == 3:
                    for q in name[i]:
                        allgrade += int(q)
                    name[i].append(allgrade)
            findname = input('请输入需要查找成绩的学生名字:\n')
            if (findname in name):
                
                print(name[findname])
                f=input('已完成，继续查询输入‘T’，回到主菜单输入‘F’\n请输入：')
                if f=='F':
                    break
                else:
                    continue
                
            else:
                f=input('输入有误，继续查询输入‘T’，输入‘F’返回主菜单\n请输入：')
                if f == 'F':
                    break
                else:
                    continue

    if (a==5):
        #预留
        jishu1 += 1 
        if jishu1 <=3:
            print('===================================')
            print('此功能尚未开发，期待后续新版本更新')
            print('===================================')
            continue
        if jishu1 >= 3 <=4:
            print('===================================')
            print('都说了没开发呢，就别按了')
            print('===================================')
            continue
        if jishu1 >= 5 <=6:
            print('===================================')
            print('你再按也™没有，憋按了')
            print('===================================')
            continue
        if jishu1 >= 7:
            print('===================================')
            print('再见吧')
            print('===================================')
            break

    if (a == 0):
        print('期待您的下次使用')
        break


