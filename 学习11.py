# 好好学习
# 加油！加油！加油！
  #比较运算符   比较运算符的结果为bool类型

a,b=10,20

print('a>b吗？',a>b)  #错误的，a应该是小于b，False
print('a<b吗？',a<b)  #正确的，a应该是大于b，True
print('a>=b吗？',a>=b)
print('a<=b吗？',a<=b)
print('a!=b吗?',a!=b)


"""一个=等于赋值运算符；两个==等于比较值运算符
    比较对象的标识是：is
"""

a=20
b=20
print(a==b)   #a与b的value相等，值相等
print(a is b) #a与b的id相等，标识相等



lst1=[11,22,33,44]
lst2=[11,22,33,44]

print(lst1==lst2)
print(lst1 is lst2)
print(id(lst1))
print(id(lst2))

print(a is not b )   #a和b的结果是不相等的？错误。False
print(lst1 is not lst2)  #lst1和lst2的结果是不相等的？正确。True
