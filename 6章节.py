"""
mylist = [21, 25, 21, 23, 22, 20]
mylist.append(31)
mylist.extend([29, 33, 30])
num1 = mylist[0]
print(f"取出第一个元素, 应该是2")
num2 = mylist[-1]
print(f"取出最后一个元素, 应该是30")
index = mylist.index(31)
print(f"元素31在列表的小下标位置是: {index}")
print(f"最后列表的内容是: {mylist}")
"""
"""
my_str = "itheima itcast boxuegu"
num = my_str.count("it")
print(f"字符串{my_str}中有{num}个it字符")
new_my_str = my_str.replace(" ", "|")
print(f"字符串{my_str}被替换空格后，结果是: {new_my_str}")
my_str_list = new_my_str.split("|")
print(f"字符串{new_my_str}按照|分割后结果是: {my_str_list}")
"""
"""
my_str = "爱情, 也不过是转瞬即逝的现实, 唯有孤独永恒"
result1 = my_str[::-1][8:10]
print(f"输出: {result1}")
"""
"""
my_list = ['程序员', '挪威的森林', '程序员', '挪威的森林', 'exam', 'angel', 'exam', 'angel', 'best']
my_set = set()

for element in my_list:
    my_set.add(element)
print(f"列表的内容是: {my_list}")
print(f"通过for循环后, 得到的集合对象是: {my_set}")    
"""
"""
info_dict = {
    "小明": {
        "部门": "科技部",
        "工资": 3000,
        "级别": 1
    },
    "小绿": {
        "部门": "市场部",
        "工资": 5000,
        "级别": 2
    },
    "小紫": {
        "部门": "市场部",
        "工资": 7000,
        "级别": 3
    },
    "小蓝": {
        "部门": "科技部",
        "工资": 4000,
        "级别": 1
    },
    "小红": {
        "部门": "市场部",
        "工资": 6000,
        "级别": 2
    }
}

print(f"升职加薪之前: {info_dict}")

for name in info_dict:
    if info_dict[name]["级别"] == 1:
        employee_info_dict = info_dict[name]
        employee_info_dict["级别"] = 2
        employee_info_dict["工资"] += 1000
        info_dict[name] = employee_info_dict
print(f"升职加薪后: {info_dict}")        

"""

