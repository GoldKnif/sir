#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import logging.handlers

maxBytes = 1 << 20  # 1M


def get_logger(name='my_logger', filename='test.log'):
    # 创建日志记录器
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # 创建控制台处理程序
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # 创建文件处理程序
    file_handler = logging.handlers.RotatingFileHandler(filename, maxBytes=maxBytes, backupCount=7)
    file_handler.setLevel(logging.INFO)

    # 创建格式器
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # 将格式器添加到处理程序中
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # 将处理程序添加到日志记录器中
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger
