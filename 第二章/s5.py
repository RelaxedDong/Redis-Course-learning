#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/20 10:47

#列表结构
import redis
pool = redis.ConnectionPool(host='47.107.66.196', port=6379,password='donghao',encoding='utf-8',decode_responses=True)
cache = redis.Redis(connection_pool=pool)


#cache.rpush('user:1:message','message1')
#cache.rpush('user:1:message','message2')


#rpush key value1 value2 ... O(N)
#lpush key value1 value2 ... O(N)
# lrange key start end

#cache.linsert('user:1:message','BEFORE','message2','666') # where: BEFORE（前）或AFTER（后）

#cache.lpop('user:1:message')
#cache.rpop('user:1:message')
#print(cache.lrange('user:1:message',0,-1))


#删除元素

#cache.lrem('user:1:message',0,'message2')
# count > 0 从左到右，删除count个 value
# count < 0 从右到左，删除count个 value
# count = 0 删除全部


#cache.rpush('user:1:message','message1')

#ltrim 列表修剪
#cache.ltrim('user:1:message',1,3)

#lset key index nwevalue#设置列表指定索引值为newValue
#print(cache.lrange('user:1:info',0,-1))

#微博 关注用户帖子
#weibo1 = {'id':'xxx1','title':'title1','content':"content1"}
#weibo2 = {'id':'xxx2','title':'title2','content':"content2"}
#weibo3 = {'id':'xxx3','title':'title3','content':"content3"}
#cache.lpush('user:123:TimeLine',str(weibo1))
#cache.lpush('user:123:TimeLine',str(weibo2))
#cache.lpush('user:123:TimeLine',str(weibo3))




"""
blpop key timeout #阻塞弹出 生产者消费者时很有用
brpop key timeout #xx
有值之后就弹出
"""

# TIPS:
# LPUSH + LPOP = Stack/
# LPUSH + RPOP = Queue
# LPUSH + LTRIM = CAPPED Collection
# LPUSH + BRPOP = MESSAGE Queye

with cache.pipeline() as f:
    for x in range(10):
        cache.lpush('articles','title %s'%x)