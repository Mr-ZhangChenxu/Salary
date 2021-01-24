'''
原有存款 1000元， 发工资之后存款变为2000元
定义模块
1、money.py saved_money = 1000
2、定义发工资模块 send_money，用来增加收入计算
3、定义工资查询模块 select_money，用来展示工资数额
4、定义一个start.py ，启动文件展示最终存款金额
'''
import money
import select_money
import send_money

if __name__ == '__main__':
    before_salary = money.saved_money
    print(f'原有存款为：{before_salary}')
    add_money = 1000
    print(f'本月工资为：{add_money}')
    now_salary = select_money.select_money(send_money.send_money(now_money=1000))
    print(f'现有存款为：{now_salary}')
