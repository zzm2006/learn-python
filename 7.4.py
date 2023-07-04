import random

angel = random.randint(1, 10)
you_angel = int(input("请猜一猜数字是多少: "))
if you_angel == angel:
    print("恭喜你第一次就猜对了")
else:
    if you_angel > angel:
        print("你猜测的数字大了")
    else:
        print("你猜测的数字小了")
    you_angel = int(input("请再猜一猜数字是多少: "))
    if you_angel == angel:
            print("恭喜你第二次猜对了")
    else:
        if you_angel > angel:
            print("你猜测的数字大了")
        else:
            print("你猜测的数字小了")    
        you_angel = int(input("请第三次猜一猜数字是多少: "))
        if you_angel == angel:
            print("恭喜你第三次再对了")
        else:
            print("三次都猜不对, 你个垃圾")    
                     