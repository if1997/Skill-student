# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 16:00:36 2018

@author: happen
"""

import string
import binascii
import binhex

#一个字典频率的求解
#word_count[word]=word_count.get(word,0)+1
#字典排序
#e=sorted(e.items(),key=lambda s:s[1],reverse=True)

plaintext_files_location=input('请输入需要解密的文件的位置:')
try:
    plaintext_files=open(plaintext_files_location,'r')
except:
    print('打开明文文件失败！\n')
else:
    plaintext_content=plaintext_files.read()
    print('输入的明文为：'.rjust(25),plaintext_content,end='\n')
    plaintext_files.close()
    for i in range(128):
        c=''
        test=0
        for j in range(int(len(plaintext_content)/2)):
            ch1=chr(int(plaintext_content[2*j:2*j+2],16)^i)
            c=c+ch1
        print(i,c)