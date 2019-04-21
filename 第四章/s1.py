#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/20 16:25


# RDB持久化
"""默认设置"""

"""
配置  seconds  changes
save    900        1
save    300        10
save    60         10000

dbfilename dump.rdb  rdb存储文件

dir ./  rdb或aof或日志存储文件地址

stop-writes-on-bgsave-error  yes    发生错误，是否会停止写入
rdbcompression yes                  是否采用压缩模式
rdbchecksum yes                     是否检验

"""

"""
取消默认模式
dbfilename dump-${port}.rdb
dir /bigdiskpath  #选择一个大的硬盘路径，可能也会分盘
stop-writes-on-bgsave-error  yes
rdbcompression yes
rdbchecksum yes
"""


# 触发机制
# 1.全量复制
# 2.debug reload
# 3.shutdown  有一个shutdown save









