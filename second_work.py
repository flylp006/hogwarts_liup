# -*- coding:utf-8 -*-
# @Author : 跳跃的闪电
# @Time : 2020/10/21 22:29
""" 定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，
如果传入“丁春秋”，打印“叛徒！我杀了你”
fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，
进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造"""


class TongLao:  # 定义TongLao类

    def __init__(self, name, hp, power):  # 构造函数
        self.name = name
        self.hp = hp
        self.power = power

    def see_people(self):  # 定义see_people函数
        if self.name == '无崖子':  # 判断实例化后的name
            print("师弟！！！！")
        elif self.name == '李秋水':
            print("呸，贱人!")
        elif self.name == '丁春秋':
            print("叛徒！我杀了你!")
        else:
            print("这是哪家道友啊?!")

    def fight_zms(self, enemy_hp, enemy_power):  # 定义fight_zms函数
        while True:
            self.hp = self.hp / 2 - enemy_power  # 调用此函数后实例的hp
            enemy_hp = enemy_hp - self.power * 10  # 调用此函数后敌人的hp
            if self.hp > enemy_hp:  # 判断双方hp的大小
                print(f"我的hp为{self.hp},敌人的hp为{enemy_hp}，我赢了!")
                break
            elif self.hp < enemy_hp:
                print(f"我的hp为{self.hp},敌人的hp为{enemy_hp}，我输了...")
                break
            else:
                print(f"我的hp为{self.hp},敌人的hp为{enemy_hp}，平手~")
                break


# WYZ = TongLao('无崖子', 1200, 50)
# WYZ.see_people()
# WYZ.fight_zms(800,250)
