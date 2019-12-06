# coding:utf-8
from django.core.cache import cache

from utils.constants import Constants


class CacheManager(object):
    def __init__(self):
        pass

    @classmethod
    def get(cls, key):
        """
        获取图形验证码
        :return:
        """
        return cache.get(key)
    @classmethod
    def save(cls, key, obj):
        """
        保存图形验证码
        :return:
        """
        cache.set(key, obj)
        cache.expire(key, Constants.REDIS_EXPIRE_TIME)

    @classmethod
    def delete(cls, key):
        """
        删除缓存
        :return:
        """



    def deleteAll(cls):
        """
        删除所有缓存
        :return:
        """
        pass