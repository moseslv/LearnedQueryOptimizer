# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     utils
   Description :
   Author :       ALv
   date：          2020/6/8
-------------------------------------------------
   Change Activity:
                   2020/6/8:
-------------------------------------------------
"""
__author__ = 'ALv'


import  os

def file_name_listdir(file_dir):
    filelist = []
    for files in os.listdir(file_dir):  # 不仅仅是文件，当前目录下的文件夹也会被认为遍历到
        filelist.append(files)
    return filelist