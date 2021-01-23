# 好好学习
# 加油！加油！加油！


#布尔运算符
a,b=10,20
print('------------and 或者--------')
print(a==10 and b==20)  #True and True，结果便是True
print(a==10 and b<20)  #True and False,结果便是False
print(a!=10 and b==20) #False and True，结果便是False
print(a!=10 and b!=20) #False and False，结果便是False

print('------------or 并且--------')

print(a==10 or b==20)   #True or True，结果便是True
print(a==10 or b<20)    #True or False,结果便是True
print(a!=10 or b==20)   #False or True，结果便是rue
print(a!=10 or b!=20)   ##False or False，结果便是False

print('------------not,对bool布尔类型的操作数进行取反--------')

f=True
f1=False

print(not f)
print(not f1)

print('------------in 和 not in  在 和 不存在--------')
s='helloword'
print('w' in s )
print('k' in s )
print('w' not in s )
print('k' not in s)
s1='我爱你'
print('我' in s1)
print('孙' in s1)
print('我' not in s1)
print('孙' not in s1)
