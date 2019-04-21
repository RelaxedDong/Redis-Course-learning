#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/20 9:53
import redis
"""哈希"""

"""
特点
Mapmap ?
Small redis
field不能相同

hget hset hdel   #api  O(1)


ghet key value  
sget key field value
def key field

hexists , hlen

hmget , hmset O(N)
hmset user:2:info age 30 name kaka shool myist
hmget uesr:2:info age name
"""

#hgetall , hvals , hkeys

#print(cache.hgetall('_userinfo:xxx'))
#print(cache.hvals('_userinfo:xxx'))
#print(cache.hkeys('_userinfo:xxx'))



"""案例
import redis
pool = redis.ConnectionPool(host='47.107.66.196', port=6379,password='donghao',encoding='utf-8',decode_responses=True)
cache = redis.Redis(connection_pool=pool)
redisKey = '_userinfo:xxx3x'
userinfo = cache.hgetall(redisKey)
print(userinfo)
if userinfo == {}:
    #viewcount = mysql.get('id+viewcount')
    print('redis 中不存在')
    cache.hset(redisKey,'viewcount',0)
else:
    viewcount = userinfo.get('viewcount')
    print(viewcount)
"""



#更多 hsetnx   hincrby hincrbyfloat