print('hello world!')
print("hello python")
print('''hello hellew''')
'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""

'''
python   保留字
and	
exec	
not
assert	
finally	
or
break	
for	
pass
class	
from	
print
continue	
global	
raise
def	
if	
return
del	
import	
try
elif	
in	
while
else	
is	
with
except	
lambda	
yield
'''
#以缩进控制代码块
if True:
    print ('true')
else:
    print('false')
if False:
    print('true')
else:
    print('false')

#多行语句以（\）为分割
item_one = '标题一'
item_two = '标题二'
item_three = '标题三'
total = item_one + \
        item_two + \
        item_three
print(total)
#多行语句在同域可以自由分割
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print('数组：');print(days)

#python的字符串可以用单双三引号来表示 ，同类型即可
#另外python三引号也表示注释 即纯字符串无输出出入赋值

x="a"
y="b"
# 换行输出
print(x)
print(y)

print ('---------')
# 不换行输出
print (x,)
print (y,)

#缩进相同的一组语句构成一个代码块，称为代码组
#类似if 试了def class 复合语句，首行以关键字开始，以冒号’：‘结束
#该行之后的一行或多行代码构成代码组
#首行以及后面的代码组称为一个子句（clause）

'''
if expression :
    suite
elif expression:
    suite
else :
    suite   #如果缩进不同会导致无法识别else下语句是否属于else
'''

# _？_ python shell 是否需要频繁交互？

#python 的变量类型
#python 变量赋值不需要类型声明
#每个变量在内存中创建 都包括变量的标识 名称 数据
#变量使用前都需要赋值 赋值之后的变量才会被创建
#用=赋值
counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = 'John' # 字符串
print(counter)
print(miles)
print(name)
#多变量赋值
tmp_a = tmp_b = tmp_c = 1 # 三个变量指向同一个内存空间
#多个对象指定多个变量
a,b,c = 1,2,'john'
print(a)
print(b)
print(c)

#python 的标准数据类型
#Number 数字 String 字符串 List 列表 Tuple 元组 Dictionary 字典

#Number 数字
#指定一个值时 Number对象会被创建
var1 = 1
var2 = 2
var3 = 3
#也可以使用del 删除对象引用
del var1
del var2 ,var3
#python的数据类型四种
#int  long   float  complex
#整型 长整型 浮点型 复数
#居然特么的支持虚数 QAQ

#python字符串
#有两种取值顺序
#1）从左向右  0至n-1
#2）从右向左  -1至-n
#包左不包右 包上不包下
s = 'ilovepython'
print(s[1:5])
print(s[-10:-6])
print(s[1:])
print(s * 2)
print(s + 'test')
print(s[1:] + 'test')
print(s[1:] * 2)
print(s[:5])

#python 列表  集合了集合和数组
#支持了字符，数字，字符串，列表
#列表用[]标识 用 , 分割元素
#列表切割 List[头索引：尾索引]
#截取正向正数 负向负数 空头取头 空尾取尾 包左不包右 包上不包下
#可重复赋值
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print (list)               # 输出完整列表
print (list[0])            # 输出列表的第一个元素
print (list[1:3])          # 输出第二个至第三个的元素
print (list[2:])           # 输出从第三个开始至列表末尾的所有元素
print (tinylist * 2 )      # 输出列表两次
print (list + tinylist )   # 打印组合的列表

#python元组
#元组是另外一种数据类型 类似与列表
#元组用 ()标识 内部用 , 分割元素
# 元组不能二次赋值  相当于只读列表
#元组也可以截取
zoo = ('wolf', 'elephant', 'penguin')
print( 'Number of animals in the zoo is', len(zoo))
new_zoo = ('monkey', 'dolphin', zoo)
print( 'Number of animals in the new zoo is', len(new_zoo))
print ('All animals in new zoo are', new_zoo)
print( 'Animals brought from old zoo are', new_zoo[2])
print ('Last animal brought from old zoo is', new_zoo[2][2])

#python 字典
#字典是无序的集合 类似map
#用{}字典由引索（key）和它对应的 value组成的
#通过键值对取值
dict = {}
#添加键值对
dict['one'] = 'this is one'
dict[2] = 'this is two'

tinydict = {'name':'john','code':456,'dept':'sales'}

print(dict['one'])
print(dict[2])
print(dict)
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

# _?_ 数据类型转换
