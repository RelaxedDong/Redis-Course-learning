#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/20 11:45

"""pipeline流水线"""
import redis,time
pool = redis.ConnectionPool(host='47.107.66.196', port=6379,password='donghao',encoding='utf-8',decode_responses=True)
cache = redis.Redis(connection_pool=pool)

def PipeLine():
    with cache.pipeline(transaction=True) as p:
        start = time.time()
        for x in range(100):
            p.lpush("user:xx:message", 'message:%s' % x).rpush('user:yy:message','haha%s'%x)
        p.execute()
        end = time.time()
        print('耗时%0.2fs' % (end - start))  #耗时 0.25s

def raw():
    start = time.time()
    for x in range(100):
        cache.lpush("user:xx:message", 'message:%s'%x)
        cache.rpush('user:yy:message','haha%s'%x)
    end = time.time()
    print('耗时%0.2fs' % (end - start))


def main():
    PipeLine() #耗时 0.25s
    #raw()       #耗时8.35s

if __name__ == '__main__':
    main()