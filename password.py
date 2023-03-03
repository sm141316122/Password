password = "123456"
num = 3

while num > 0:
	answer = input("請輸入密碼: ")
	if answer == password:
		print("登入成功!")
		break
	else:
		num -= 1
		if num == 0:
			print("密碼錯誤")
		else:
			print(f"密碼錯誤 還有{num}次機會")
