"""
def account_create(initial_amount=0):
    def atm(num, deposit=True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"存款, +{num}, 账号余额, {initial_amount}")
        else:
            initial_amount -= num
            print(f"取款, -{num}, 账户余额: {initial_amount}")

    return atm         

atm = account_create()

atm(100)
atm(100)
atm(100, deposit=False)          闭包
"""

"""
def outer(func):
    def inner():
        print("我睡觉了")
        func()
        print("我起床了")
    return inner

@outer
def sleep():
    import random
    import time
    print("睡眠中.......")
    time.sleep(random.randint(1, 5))    

sleep()  装饰器
"""


