employee_dic = {}


def show_menu():
    """进入菜单栏"""
    print('*' * 10, '员工管理系统V1.0', '*' * 14)
    print("1、添加员工信息")
    print("2、删除员工信息")
    print("3、修改员工信息")
    print("4、查询员工信息")
    print("5、显示所有员工信息")
    print("6、退出系统")
    print("*" * 40)


def add_info():
    print("添加员工==>")
    employ_id = input("请输入要添加员工的工号：")
    all_id = list(employee_dic.keys())
    if employ_id in all_id:
        print("员工工号已存在，不能重复添加！")
        return
    employ_name = input("请输入要添加员工的姓名：")
    employ_sex = input("请输入要添加员工的性别：")
    employ_salary = input("请输入要添加员工的工资：")
    info_dic = {"name": employ_name, "sex": employ_sex, "salary": employ_salary}
    employee_dic[employ_id] = info_dic
    print(f"工号为{employ_id}的员工信息添加成功")


def delete_info():
    print("删除员工信息==>")
    employ_id = input("请输入要删除员工的工号：")
    all_id = list(employee_dic.keys())
    if employ_id not in all_id:
        print("员工工号不存在，无法进行删除！")
        return
    else:
        del employee_dic[employ_id]
    print(f"工号为{employ_id}的员工信息删除成功")


def update_info():
    print("修改员工信息==>")
    employ_id = input("请输入要修改员工的工号：")
    all_id = list(employee_dic.keys())
    if employ_id not in all_id:
        print("员工工号不存在，无法进行修改！")
        return
    new_name = input(f"姓名是{employee_dic[employ_id]['name']}修改后的姓名是：")
    new_sex = input(f"性别是{employee_dic[employ_id]['sex']}修改后的性别是：")
    new_salary = input(f"工资是{employee_dic[employ_id]['salary']}修改后的工资是：")
    if new_name != '':
        employee_dic[employ_id]['name'] = new_name
    if new_sex != '':
        employee_dic[employ_id]['sex'] = new_sex
    if new_salary != employee_dic[employ_id]['salary']:
        employee_dic[employ_id]['salary'] = new_salary
    print(f"工号为{employ_id}的员工信息修改成功！")


def select_info():
    print("查询员工信息==>")
    employ_id = input("请输入要查询员工的工号：")
    all_id = list(employee_dic.keys())
    if employ_id not in all_id:
        print("工号不存在，无法查到对应信息")
        return
    else:
        print(f"工号{employ_id}的信息：{employee_dic}")


def show_all_info():
    print("显示所有员工信息==>")
    if len(list(employee_dic.keys())) == 0:
        print("当前没任何员工信息，请选择操作 1 添加员工！")
        return
    print("-" * 40)
    for people in ['工号', '姓名', '性别', '工资']:
        print(people, end='\t\t')
    print('')
    print('-' * 40)
    for jboer in employee_dic.items():
        print(f"{jboer[0]}\t {jboer[1]['name']}\t {jboer[1]['sex']}\t {jboer[1]['salary']}")
    print('-' * 40)
