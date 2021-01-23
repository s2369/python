# 好好学习
# 加油！加油！加油！
str1='我只爱夏明月'
str2="我只爱夏明月"
str3='''我只爱\n\t
夏明月'''

str4="""我只爱夏明月"""


print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
print(str4,str(str4))

i=24

he='祝你'+str(i)+'岁生日快乐'

print(he,type(i))


name='张三,'
age=20
print(name,type(name), age,type(age))   #name与age的数值类型不相同

print('我叫'+name+'今年'+str(age)+'岁')      #当str类型，和int类型连接时。出现失败后，应进行转换方案


print('-----------------------str()将其它类型的数值，转换成str')

a=98
b=9.8
c=False
d='我爱你'

print(type(a),type(b),type(c),type(d))

print(str(a)+str(b)+str(c)+str(d))
print(a,b,c)



print('-----------------------int()将其它类型的数值，转换成int')

s1='777'
s2=22.2
s3='28.8'
s4=True
s5=28
s6='hello'
s7=False
print(type(s1),type(s2),type(s3),type(s4),type(s5),type(s6))

print(int(s1),type(int(s1)))     #将str类型转换成int类型，前提是，字符串内为整数、数字串
print(int(s2),type(int(s2)))     #float类型转换成int类型，只会截取整数，舍掉小数部分
#print(int(s3),type(s3))    #将str类型转换成int类型，报错。原因是，字符串为小数串
print(int(s4),type(int(s4)))
#print(int(s6),type(s6))     #非整数的字符串，无法转换成int类型
print(int(s7),type(int(s7)))


print('-----------------------float()将其它类型的数值，转换成int')
s1='777'
s2=22.2
s3='28.8'
s4=True
s5=28
s6='hello'
s7=False

print(float(s1),type(float(s1)))
print(float(s7),type(float(s7)))




i=8
s='数字'
j=9
y='也是'
print(str(i)+'是我最喜欢的'+s+str(j)+y)
