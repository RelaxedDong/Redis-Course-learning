#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/20 16:05

# geoadd longitude(经度) latitude(纬度) member

import redis,time
pool = redis.ConnectionPool(host='47.107.66.196', port=6379,password='donghao',encoding='utf-8',decode_responses=True)
r = redis.Redis(connection_pool=pool)

r.geoadd('cities:locations',"116.28","39.55",'Beijing')
# 。。。。。。
#http://redisdoc.com/geo/geoadd.html






