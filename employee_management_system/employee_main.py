from employee_management_system import employee_tools
import time

while True:
    employee_tools.show_menu()
    action_str = input("请输入您的操作：")
    if action_str == '1':
        employee_tools.add_info()
    elif action_str == '2':
        employee_tools.delete_info()
    elif action_str == '3':
        employee_tools.update_info()
    elif action_str == '4':
        employee_tools.select_info()
    elif action_str == '5':
        employee_tools.show_all_info()
    elif action_str == '6':
        print("欢迎您再次使用系统")
        break
    else:
        print("您的输入有误，请重新选择：")
