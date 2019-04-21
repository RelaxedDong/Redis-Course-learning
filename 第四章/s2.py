#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/21 10:47


# O(n)数据：耗时
# fork():消耗内存,copy-on-write策略
# Disk I/O:性能


# AOF: 根据日志的原理


"""
（1）AOF文件因为没有压缩，因此体积比RDB大。
（2）AOF是在每秒或者每次写操作都进行备份，因此如果并发量比较大，效率可能有点慢。
（3）AOF文件因为存储的是命令，因此在灾难恢复的时候Redis会重新运行AOF中的命令，速度不及RDB
"""


"""三种策略"""
"""
1. always

写命令时，先写入缓冲区，always 每条命令执行fsync到硬盘


2. everysec(默认值)
写命令时，先写入缓冲区，always 每秒命令执行fsync到硬盘

3.no
写命令时，先写入缓冲区，always 操作系统决定fsync -> 硬盘



命令    always          eversec                no

优点  不丢失数据   每一秒fsync丢一秒数据       不用管
缺点    io开销大        丢一秒数据             不可控
"""












