name = {}


def  begin():
    print('填写所需选项的序号:')
    print('1: 列出所有成绩')
    print('2：增加或更改学生和成绩')
    print('3：删除学生')
    print('4：查找学生成绩')
    print('5：按成绩排名')
    print('6：导出数据')
    print('7：读取数据')
    #print('8：联网检查更新（未开发）')
    print('0：退出系统')


def allg():
    for i in name:
        allgrade = 0
        if len(name[i]) == 3:
            for q in name[i]:
                allgrade += int(q)
            name[i].append(allgrade)


def a1():
    print('(注：输出的顺序为:\n姓名 语文成绩 数学成绩 英语成绩 总分)')
    if name == {}:
        f = input('当前没有学生，输入‘T’前往添加,输入‘Enter’进行下一步:')
        if f == 'T':
            a2()
        if f == '':
            print()
    for stu in name:
        print(stu+':'+str(name[stu]))
    f = input('输入‘F’回到主菜单:')
    if f == 'F':
        print()


def a2():
    newname = str(input('请输入新学生或需要修改的学生名字：'))
    newgrade_Chinese = input('请输入Ta的语文成绩：')
    newgrade_Mach = input('请输入Ta的数学成绩：')
    newgrade_English = input('请输入Ta的英语成绩：')
    allnewgrade = [newgrade_Chinese, newgrade_Mach, newgrade_English]
    name.update({newname: allnewgrade})
    f = input('回到主菜单输入‘F’\n请输入：')
    if (f == 'F'):
        print()


def a3():
    while True:
        if name == {}:
            f = input('当前没有学生，输入‘T’前往添加,输入‘F’回到主菜单:')
        if f == 'T':
            a2()
            break
        if f == 'F':
            break

        delname = input('请输入需要删除的学生名字:\n')
        if (delname in name):
            name.pop(delname)
            f = input('已删除,继续删除输入‘T’，返回主菜单输入‘F’\n请输入：')
            if f == 'F':
                break
            else:
                continue
        else:
            f = input('输入有误,继续删除输入‘T’，输入‘F’返回主菜单\n请输入：')
            if f == 'F':
                break
            else:
                continue


def a4():
    while True:
        if name == {}:
            f = input('当前没有学生，输入‘T’前往添加,输入‘F’回到主菜单:')
        if f == 'T':
            a2()
            break
        if f == 'F':
            break

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


def a5():
    if name == {}:
        f = input('当前没有学生，输入‘T’前往添加,输入‘F’回到主菜单:')
        if f == 'T':
            a2()
        if f == 'F':
            print()

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


def a6():
    f = open('学生名录.txt','w')
    f.write(str(name))
    f.close()
    print('导出完成')


def a7():
    f = open('学生名录.txt','r')
    data2 = f.read()
    name = eval(data2)
    print('读取成功，读取的数据为:')
    for stu in name:
        print(stu+':'+str(name[stu]))

print('欢迎使用学生管理系统v0.2.1\n©Copyright2021杨一朔.AllRightsReserved\n按回车键开始使用')
p = input()

while True:
    allg()
    begin()
    a = int(input('输入您的选项:'))


    if (a == 1):
        a1()

    if (a == 2):
        a2()

    if (a == 3):
        a3()

    if (a == 4):
        a4()

    if (a == 5):
        a5()
    
    if (a == 6):
        a6()

    if (a == 7):
        a7()

    if (a == 0):
        print('期待您的下次使用')
        break

    if (a != 1 and a != 2 and a != 3 and a != 4 and a != 5 and a != 6 and a != 7 and a != 0 ):
        print('输入有误，请重新输入')
        continue