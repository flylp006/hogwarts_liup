"""题目：
一个多回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了"""


def fight(enemy_hp, enemy_power):  # 定义fight方法，传入enemy的hp和power。疑问：当调用方法时传入的不是int怎么做限制
    my_hp = 1000  # 定义我的hp
    my_power = 200  # 定义我的power
    try:
        while True:  # 多回合制用while循环实现
            my_hp = my_hp - enemy_power  # 我的战损
            enemy_hp = enemy_hp - my_power  # enemy的战损
            if my_hp <= 0:  # 判断我的hp是否先为0
                print(f"我的hp为{my_hp},我输了")
                break
            elif enemy_hp <= 0:  # 判断enemy的hp是否先为0
                print(f"enemy的hp为{enemy_hp}，enemy输了")
                break
    except:
        print("enemy_hp和enemy_power都必须为数字")  # 调用方法的参数必须为数字


fight(1100, 250)  # 调用fight方法
