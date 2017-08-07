#迭代器		基本方法：iter()和next()
list1=list(range(1,5))
it=iter(list1)
#print(next(it))
#print(next(it))

#迭代器对象可以使用常规for语句进行遍历
'''for x in it:
	print(x,end="")
'''

'''import sys

while True:
	try:
		print (next(it))
	except StopIteration:
		sys.exit()
'''
i=0
while i<len(list1):
		print (next(it))
		i+=1
	
