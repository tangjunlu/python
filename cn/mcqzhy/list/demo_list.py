# li = [100,'列表',True,[1,2,3]]

# 列表的创建
# 方式一
# li = [1,2,3]

# # 方式二
# li = list()

# 方式三: 列表推导式

# 索引
# a = li[0]

# 增删改查
li = ['孙悟空','猪八戒','沙悟净','金婵子']

# 增
# append
# 追加
# li.append('如来')
# print(li)

# insert
# 按位置增加
# li.insert(2,'白骨精')
# print(li)

# extend 迭代增加

# 删
# pop
# 按照索引删  返回删除的元素
# li.pop(-2)

# # 默认删除最后一个
# li.pop()
# print(li)

# remove
# 指定元素删除
# li.remove('金婵子')
# print(li)

# del
# 按照索引删除
# del li[-1]
# print(li)
# 按照切片删除
# del li [::2]
# print(li)

# 改
# 按照索引改值
# li[0] = '太白'
# print(li)
# 按照切片改
# li[2:] = 'aaaaaa'
# print(li)
# 按照切片 （步长）
# li[::2] = 'ab'
# print(li)

# 查
# 索引 切片
# for i in li:
#     print(i)