# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 11:31:20 2018

@author: happen
"""
#base64加密
import base64

plaintext_files_location=input('请输入需要base64编码的位置:')
#加载明文加解密
try:
    plaintext_files=open(plaintext_files_location,'r')
except:
    print('打开明文文件失败！\n')
else:
    plaintext_content=plaintext_files.read()
    plaintext_files.close()
    print('输入的明文为：\n',plaintext_content)
    plaintext_contents=bytes(plaintext_content,encoding='utf-8')
    en_base_content=base64.b64encode(plaintext_contents)
    print("base64编码后的结果:\n",en_base_content)
    de_base_content=base64.b64decode(en_base_content)
    print("base64解码的结果:\n",de_base_content)