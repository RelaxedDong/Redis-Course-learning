#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/19 17:12

# keys partern

#Mset 命令用于同时设置一个或多个 key-value 对。
# mset hello world hehe haha bb php
#例如： keys [a-z]*

# keys *怎么用
#1. 热备从节点
#2. scan

# dbsize
# 计算key的总数

# exists 检查key是否存在
# 存在返回1

#del key
# 删除key-value

#expire key second
#key 在  seconds秒后过期


#ttl key
# 查看还有多久过期

# persist key
#去掉key的过期时间   ttl表示无过期时间


#type key 查看类型


