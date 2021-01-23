# 好好学习
# 加油！加油！加油！
#转义字符

print('\thello\n\tword')#\n换行
print('hello\tword')#\t
print('hellooo\tword')#\t空格
print('hello\rword')#\r回车，覆盖
print('hellp\b\twode')#\b是退格
print('http:\\\\www.baidu.com')
print('老师说:\"大家好\"')


#原字符，让字符串中的转义字符不起作用，在字符串之前加上r或者R

print(r'hello\nword\\\\')