#在Python中没有do..while循环
n=100
sum=0
con=1
while con<n:
	sum+=con
	con+=1

print("1到%d的和为：%d" % (n,sum))

#while … else 在条件语句为 false 时执行 else 的语句块
count=0
while count<5:
	print(count)
	count+=1
else:
	print(count,"大于或等于5")	

# for循环可以遍历任何序列的项目，如一个列表或者一个字符串
list1=["tim","tom","Perl","Python"]
for x in list1:
	print (x)

#break跳出当前循环体
for i in list1:
	if i =="Perl":
		print("执行到"+i)
		break;
	print("输出："+i)

#range()函数
for i in range(5):
	print(i)

print("***********range(2,10)**************")

for i in range(2,10):
	print(i)

print("***********range(2,10,2)**************")

for i in range(2,10,2):
	print(i)

print("***********遍历一个序列的索引**************")
#可以结合range()和len()函数以遍历一个序列的索引
for i in range(len(list1)):
	print ("第%d个元素为：%s"%(i,list1[i]))

#利用range()创建列表
list2=list(range(2,10,2))
print(list2)