import mailbox
# from curses.ascii import ctrl
# from http.cookiejar import user_domain_match
from operator import truediv
from os import name
from shutil import make_archive
from time import perf_counter


print(" dad"   " 我是第一行"
      '\n 我是第二行 '
      ' she said\'victory' + ' indeed')
print(" hi\' world"+" his' bad intention"'\n weird')
# ''' my_lover=4564554
#  my_lover_now=my_lover
#  my_lover_now='456684'
#   这是注释可以不执行 快捷键：control + /
#  print(my_lover)
#  print(my_lover_now)
#  print(" labour lack ladder laser")
#  v=my_lover_now
#  print(v)
#  对字符串求长度  len（）
#  print(len('on the way'))'''
#  通过索引获取单个字符
#  print(v[4])
#  print(v[len(v)-3])

import math
result=1+2-3/4*5
print(result)
a=-1
b=-2
c=11
delta=b**2-4*a*c
result_1=(-b + math.sqrt(delta))/(2*a)
result_2=(-b - math.sqrt(b**2-4*a*c))/(2*a)

print(result_1)
print(result_2)
# bool类型
b2=True
b1=False
# 空值类型
None
print(type(result_1))
print(type(a))
print(type(b))

#python有两种执行模式   命令模式    交互模式 ——F12
# ctrl+y ；  删除整行
# ctrl+D ；  自动copy整行
# ctrl+z :   返回上一步
# ctrl+x ：  剪切
# shift+F6 :   批量改变量名



# BMI计算器
'''User_height = float(input('身高m: '))
User_weight = float(input('体重kg: '))
BMI=round(User_weight/User_height**2 ,4)
print("你的BMI值为:" + str(BMI))

if  BMI <18.5:
    print("True" + "\nHow great you are ")
    print("Good")

    user_gender = input("请输入你的性别：")
    if user_gender=='男':
        print("ok")
        user_nation=input("请输入你的国家：")
        if user_nation=="中国":
            print("ok")

        else:
            print("not ok")


    else:
        print("not ok")


elif BMI >18.5 and BMI <25:
    print("偏瘦")
elif BMI >25 and BMI <30:
    print("重")
else:
      print("False Oh bad news ")'''


# mood_index=int(input("请输入心情指数："))
# is_at_home=input("请输入是不是在家：")
# if mood_index>60:
#     if is_at_home=="是":
#           print("very good" )
#     else:
#           print("very bad")
#
#
# else:
#     print("Not very good")

shopping_list=[]
shopping_list.append(' 鼠标')
shopping_list.append(' 键帽')
shopping_list.append(' 键盘')
shopping_list.append(' 音响')


print(shopping_list)
shopping_list.remove(shopping_list[0])
print(shopping_list)
print(len(shopping_list))
shopping_list.remove(' 音响')
print(shopping_list[len(shopping_list)-1])

price=[799,1024,200,800]
max_price=max(price)
min_price=min(price)
sorted_price=sorted(price)
print(max_price)
print(min_price)
print(sorted_price)

# example_tuple=("joke"," lamp"," emphasize")
# example_tuple.append=("fruitful") 元组固定不变

contacts={"小红":"125535356266",
          "小白":"219874358738",
          "小仲":"389545768498"}
contacts["小天"]="128371327398"
contacts["小苗"]="948756576945"
print("小天"in contacts)
del contacts["小天"]
print(contacts)
print(len(contacts))
query =input("请输入你要查询的联系人名字:")
for name in contacts:
    if query in name :
        print("你好 你查询的" + query, "电话号码如下")
        print(contacts[name])
    else:
        print("你好你要查询的电话号码不在这里")














