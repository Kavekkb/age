driving = input('你有沒有開過車?')

if driving != '有' and driving !='沒有':
	print('只能輸入有/沒有')
	raise SystemExit

age = input("how old are u?")

age=int(age)

if driving == '有':
	if age >= 18:
		print('通過測驗')
	else:
		print('??????')
elif driving=='沒有':
	if age >=18:
		print('可以考駕照了')
	else:
		print('還不行')