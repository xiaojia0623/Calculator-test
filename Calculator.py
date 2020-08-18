while True:
	user_input = input('請輸入你的數值用法(+,-,*,/): ')
	if user_input == 'exit':
		break
	elif user_input == '+':
		num_1 = float(input('請輸入數字: '))
		num_2 = float(input('請輸入第二個數字: '))
		result = str(num_1 + num_2)
		print('答案是 : ' + result)
	elif user_input == '-':
		num_1 = float(input('請輸入數字: '))
		num_2 = float(input('請輸入第二個數字: '))
		result = str(num_1 - num_2)
		print('答案是 : ' + result)
	elif user_input == '*':
		num_1 = float(input('請輸入數字: '))
		num_2 = float(input('請輸入第二個數字: '))
		result = str(num_1 * num_2)
		print('答案是 : ' + result)
	elif user_input == '/':
		num_1 = float(input('請輸入數字: '))
		num_2 = float(input('請輸入第二個數字: '))
		result = str(num_1 / num_2)
		print('答案是 : ' + result)