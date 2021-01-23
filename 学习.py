# 好好学习
# 加油！加油！
print(520)
print(330)


print(68+9)


#将数据输出到文件.注意点：1，所指定的盘符存中；2、使用file=fp

fp=open('D:/text.txt','a+')    #a+=文件不在，便创建；文件在，便继续添加
a=10
print(a,file=fp)
print('hello word',file=fp)

fp.close()


#不进行换行输出
print('hello','word','python')


#python小技巧  修改字符串的大小写

name='xia ming yue'
print(name.title())     #title(),将字符串小写输出为：首字母大写

nam='Xia Ming Yue'
print(nam.upper())      #upper(),将字符串全部变为：大写
print(nam.lower())      #lower()，将字符串全部变为：小写

