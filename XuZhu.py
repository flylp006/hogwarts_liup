# -*- coding:utf-8 -*-
# @Author : 跳跃的闪电
# @Time : 2020/10/21 22:58
from second_work import TongLao  # 导入TongLao类


class XuZhu(TongLao):  # XuZhu类继承TongLao类

    def read(self, enemy_hp, ennemy_power):  # 定义read函数
        print("罪过罪过")
        super().see_people()  # 继承see_people函数
        super().fight_zms(enemy_hp, ennemy_power)  # 继承fight_zms函数


DCQ = XuZhu('丁春秋', 1000, 120)  # 实例化
DCQ.read(1200, 500)  # 调用read函数
