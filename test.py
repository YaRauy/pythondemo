#coding=utf-8
print ("Hello, World!")

print ("编码")

import sys
if sys.version > '3':
   PY3 = True
else:
   PY3 = False

print(PY3) #区分大小写

#内置的 type() 函数可以用来查询变量所指的对象类型
a=111
b=111.0
c="runoob"

#还能这样赋值
e=f=5
h,j,k=1,2,"bang"

print(type(a),type(b),type(c))

#在python3中True和False被定义为关键字，但他们的值还是1和0，可以和数字相加

print(2+True);


#运算
s1=7/3; #除法，得到浮点数
s2=7//3;	#除法,得到一个整数
s3=7%3;	#取余
s4=3**3	#乘方
print(s1,s2,s3,s4)

#del可以删除一个或多个对象
del a,b,c


#字符串截取
str="Runoob go"
#变量[头下标:尾下标]
print(str)
print(str[0:-3]) 
print(str[0:3])
print(str[3:])
print(str+" lol")

#list列表
exlist=[1,"run",2.23,4.4,"abcd"]
tinylist=[123,'runoob']

#变量[头下标:尾下标]   -1为从末尾的开始位置   *表示重复操作
print(exlist[0])
print(exlist[1:])
print(exlist+tinylist)
#更改元素
exlist[0]=111
print(exlist)

#Tuple元祖
tuple1=("abc",111,23.3,44.456,"run")
#用法和列表一样，但是不可以更改其中的元素

#构造包含 0 个或 1 个元素的元组比较特殊
tup1=()
tup2=(20,)	#一个元素需要在后面加逗号

#元祖的元素虽然不可改，但是它可以包含可变的对象，比如list
tup=(exlist,tinylist)
print(tup)

exlist[3]="hahahha"

print(tup)



#Set 集合   一个无序不重复元素的序列
#基本功能是进行成员关系测试和删除重复元素

student={'Tom','Jim','Mary','Tome'} #创建集合{}
teacher=set('Mary')	#创建空集合必须用set(),{}是用来创建空字典

print(student) #重复的元素被自动去掉了

#成员测试
if('Rose' in student):
	print("Rose在集合中")
else:
	print("Rose不在集合中")

#可进行集合运算
a=set("abcdefg")
b=set("bcdk")
print("差集",a-b)	#a和b的差集,从a中减去b中重复的元素
print("并集",a|b)	#a和b的并集,不重复相加
print("交集",a&b)	#a和b的交集，重合的部分
print("不重复元素",a^b)	#a和b中不同时存在的元素，不重合的部分

#dictionary字典 无序的对象集合
dict1={}
dict1['name']="Tom"
dict1['age']=13
dict1['sex']="man"

print(dict1)
print(dict1['name'])

#dict()可以直接从键值对序列中构建字典
diction=dict([('runoob',1),('google',2),('taobal',3)])
print(diction)

#转换数据类型，dict(d)创建一个字典。d 必须是一个序列 (key,value)元组。 
li1=[1,"aaa"];li2=[2,'bbb'];li3=[3,'ccc']	#list列表
tupa=(li1,li2,li3)	#把列表放进元祖里
print("元祖",tupa)
dic2=dict(tupa)
print("字典",dic2)