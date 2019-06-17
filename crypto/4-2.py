# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 15:40:15 2018

@author: happen
"""

#进行异或运算

plaintext_files_location=input('请输入需要异或编码的位置:')
#加载明文加解密
try:
    plaintext_files=open(plaintext_files_location,'r')
except:
    print('打开明文文件失败！\n')
else:
    plaintext_content=plaintext_files.readlines()
    plaintext_files.close()
    a=[]
    for plaintext in plaintext_content:
        a.append(plaintext)
        print('输入的明文为：'.rjust(25),plaintext,end='\n')
    c=int(a[0],16)^int(a[1],16)
    c=hex(c)
    print("异或后的结果:".rjust(25),c)
