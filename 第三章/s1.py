#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/20 11:19

#redis生命周期

# 1.发送命令
# 2.排队
# 3.执行
# 4.返回
# 慢查询：发生第三阶段

# 两个配置  slowlog-max-len

# 1.先进先出 队列
# 2.固定长度
# 3.保存在内存中 重启后不会持久化

"""
slow-log-slower-than = 10000

slowlog list  #先进先出队列

slowlog-max-len = 100
"""

"""
slow-log-slower-than 慢查询阈值（单位：微秒）

slow-log-slower-than = 0 所有记录记录为慢查询
slow-log-slower-than < 0  不记录


配置方法：
1.默认值
config get slowlog-max-len = 128
config get slow-log-slower-than = 10000  10毫秒

2.修改配置文件重启

3.动态配置
config set slowlog-max-len = 128
config set slow-log-slower-than = 10000
"""

"""
慢查询命令：
slowlog get [n] :获取慢查询队列
slowlog len :获取长度

slowlog reset #清空慢查询
"""







