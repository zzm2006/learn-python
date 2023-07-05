"""
angel = 0
i = 1
while i <= 100:
    angel = angel+i
    i += 1
    print(f"1到100的和是:{angel}")
"""
"""
import random
angel = random.randint(1, 100)
exam = 0

you = True
while you: 
    on_angel = int(input("请输入你猜测的数字:"))
    exam += 1
    if on_angel == angel:
        print("猜中了")
        you = False
    else:
        if on_angel > angel:
            print("你猜测的数字大了")
        else:
            print("你猜的数字小了")

print(f"你总干猜测了{exam}次")                
"""
"""
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j} * {i} = {j * i}\t", end='')
        j += 1
    i += 1
    print()    
"""
"""
angel = "intheima is a brand of itcast"
i = 0
for x in angel:
    if x == "a":
        i += 1
        print(f"{angel}里面有{i}个a")
"""
"""
exam = 0
for x in range(1, 100):
    print(x)
    if x%2 == 0:
        exam += 1
        print(f"有多少个偶数{exam}")

"""
"""
for x in range(1, 10):
    for a in range(1, x+1):
        print(f"{a} * {x} = {a * x}\t", end= '')
    print()        
"""
"""
exam = 10000
for i in range(1, 21):
    import random
    angel = random.randint(1, 10)

    if angel < 5:
        print(f"员工{i}你的积分{angel}不足, 不发工资, 下一位")
        continue
    if exam >= 1000:
        exam -= 1000
        print(f"{i}员工, 积分足够发放工资1000, 公司账户余额:{exam}")
    else:
        print(f"没有了,当前余额:{exam}元, 下次再来")
        break       
"""






