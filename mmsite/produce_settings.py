#!/usr/bin/env python
# -*- encoding:utf-8 -*-
"""
File Name: produce_settings
Author: shangxc
Created Time: 2019-06-27 21:55
"""
# 导入公共配置
from .settings import *

# 生产环境关闭DEBUG模式
DEBUG = False

# 生产环境关闭跨域
CORS_ORIGIN_ALLOW_ALL = False

if __name__ == '__main__':
    pass
