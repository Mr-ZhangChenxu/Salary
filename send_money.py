'''
原有存款 1000元， 发工资之后存款变为2000元
定义模块
1、money.py saved_money = 1000
2、定义发工资模块 send_money，用来增加收入计算
3、定义工资查询模块 select_money，用来展示工资数额
4、定义一个start.py ，启动文件展示最终存款金额
'''
from money import saved_money


def send_money(now_money=0):
    now_money += saved_money
    return now_money

if __name__ == '__main__':
    print(f'原有工资为：{saved_money}')
    now_money = send_money(now_money=1000)
    print(f'现有工资为：{now_money}')