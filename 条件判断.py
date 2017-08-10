age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

'''
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
'''
'''
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
if 'x':
    print('True')

birth = input('birth: ')
if birth < '2000':
    print('00前')
else:
    print('00后')
'''

h = float(input('身高 ：'))
w = float(input('体重 ：'))

bmi = w / (h * h)

if bmi < 18.5:
    print('体重过轻：', 'bmi = ', bmi)
elif bmi < 25:
    print('体重正常：', 'bmi = ', bmi)
elif bmi < 28:
    print('体重过重：', 'bmi = ', bmi)
elif bmi < 32:
    print('体重肥胖：', 'bmi = ', bmi)
else:
    print('体重严重肥胖：', 'bmi = ', bmi)
