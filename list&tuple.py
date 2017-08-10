#list 列表
#list 是一种有序集合
classmates = ['michael' , 'bob' , 'tracy']
print(classmates)
print(len(classmates))
print(classmates[0] , classmates[1] , classmates[2])
#索引不能越界
#print(classmates[3])
print(classmates[-1])
print(classmates[-2])
#正序0起头 负序-1起头

#list提示一个可变有序表
classmates.append('adam')
print(classmates)
classmates.append('bob')
print(classmates)
classmates.insert(1,'jack')
print(classmates)

#list 元素可以使不同的数据类型
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print(p)
print(s)
print(s[2][1])

#空list
L = []
print(len(L))

# tuple 元组 但是tuple初始化后不能修改
# tuple 类似java 中的数组
# 不变的是指向
# 如果可以尽量用元组 代替 列表
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])
