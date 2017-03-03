#!/usr/bin/python
#coding:utf-8

import re
import os
import psutil

with open("/proc/cpuinfo","rb") as f:
        content = f.readlines() #以行为单位，读取整个文件
result_dict = {} #实例化一个空字典
for line in content: # 循环每一行
        data = [i.strip() for i in line.split(":")] #以冒号分割，去除元素两端的空格
        if len(data) == 2:
                key,value = data #进行序列解包赋值
                result_dict[key] = value #形成最后的格式
        else:
                print(data)

print(result_dict)
print(result_dict["model name"])
