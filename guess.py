import random
r_num = random.randint(1, 100)
#print(r_num)
c = 0
while True:
	c = c + 1
	k_num = input('请输入数字：')
	k_num = int(k_num)
	if k_num == r_num:
		print('你猜对了！')
		print('你猜了', c, "次")
		break
	elif k_num > r_num:
		print('数字猜大了')
	elif k_num < r_num:
		print('数字猜小了')
	print('你猜了', c, "次")
	print('     .')
		


