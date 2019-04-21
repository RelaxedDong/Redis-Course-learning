#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/21 11:14

# 重写AOF
"""
set a b
set a c
set a d

set a==>d  AOF

减少磁盘占用量
加速恢复速度


重写方式
1.  bgrewriteaof 类似bgsave
2.aof重写配置



bgrewriteaof：
bgrewriteaof->redis master (fork redis子进程) -> aof重写 ->AOF

配置：
auto-aof-rewrite-min-size:aof文件重写需要的尺寸
auto-aof-rewrite-percentage: aof 文件增长率

统计：
aof_currrent_size ：aof当前尺寸（单位：字节）
aof_base_size :  aof上次启动和重写的尺寸 （单位：字节)
"""


"""
appendonly  yes
appendfilename "appendonly-${port}.aof"
appendfsync everysec
dir /bigdiskpath
no-appendfsync-on-rewrite yes
auto-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb
"""






