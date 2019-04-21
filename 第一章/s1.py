#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/19 16:41

# Redis: 开源，基于键值对的存储服务系统 ， 多种数据结构 ，高性能，功能丰富

#数据结构
# string hash list set sortedsets

#速度快  10w ops 每秒10W次读写
#数据存内存中，  C语言实现
#线程模型   单线程


# 持久化 （断电不丢数据）
# 对数据更新异步保存到磁盘 （RDB,AOF）

# （本质字符串）
# BitMaps:位图
#HyperLogLog: 超小内存唯一值计数 （12K） 比如算DAU

#GEO：地理信息定位  （算经度纬度等）


#支持多种客户端语言
# php java lua nodejs ruby python等


#功能丰富
# 发布订阅
# Lua脚本
# 事务
# pipeline





















