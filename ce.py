#test1
#这是一个注释
print ("你好")

'''
长注释在此哟
啦啦啦啦啦啦
'''

#缩进必须一样

#test2
#True 必须大写，不然报错
if True:
	print ("true")
else:
	print ("false")

#test3
# 反斜杠可以实现多行语句
total='item_one' + \
'item_two' + \
'item_three'

print (total)

#test4
#字符串前加r或R，所有字符会原样输出
word1="this is a line with \n"
print (word1)
word2=r"this is a line with \n"
print (word2)

#test5
#执行代码后在按回车键后就会等待用户输入：
#input("\n\n按下enter键后退出")

#test6
#Python可以在同一行中使用多条语句，语句之间使用分号(;)分割
import sys;x="runoob";sys.stdout.write(x+"\n")

#test7
#不换行输出
print(total,end="")
print(x)