#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/20 15:37

#hyperloglog



"""
pfadd  key value1 value 2
pfcount key
pfmerge  newname name1 name2

"""

import redis,time
pool = redis.ConnectionPool(host='47.107.66.196', port=6379,password='donghao',encoding='utf-8',decode_responses=True)
cache = redis.Redis(connection_pool=pool)

with cache.pipeline() as f:
    start = time.time()
    userlist = []
    for x in range(1000000):
        userlist.append('Uesr %s'%x)
        if x % 10000 == 0:
            f.pfadd('tody', *userlist )
            userlist = []
            print(x)
    f.execute()
    end = time.time()
    print('耗时%0.2fs' % (end - start)) #错误率1%左右  耗时21.83s







