#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/19 17:46

#单线程为什么快

# 1.  纯内存 （响应时间大约100ns）
# 2.  非阻塞IO
# 3.  避免了线程切换和静态消耗


# 1.一次只运行 一条命令
# 2.拒绝长（慢）命令 keys *,flushall,flushdb.....等
# 3.其实不是单线程
    #fysnc file descriptor
    #close file descriptor
