# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 20:50:42 2018

@author: happen
"""

import numpy as np
import math
import string
import math

#matrix

def gcd(a,b):
    if a<b:
        a,b=b,a
    while b:
        a,b=b,a%b
    return abs(a)


#逆元求解（欧几里得算法）
def modreverse(a,m):
    if gcd(a,m)!=1:
        return None
    u1,u2,u3 = 1,0,a
    v1,v2,v3 = 0,1,m
    while v3!=0:
        q = u3//v3
        v1,v2,v3,u1,u2,u3 = (u1-q*v1),(u2-q*v2),(u3-q*v3),v1,v2,v3
    return u1%m

#加密算法
def encode(encry_key,hill_n,plaintext_content):
    #分割、整理明文
    plains=[]
    for plaintext in plaintext_content:
        if plaintext in string.ascii_uppercase:
            plain=(ord(plaintext)-ord('A'))%26
            plains.append(plain)
    num=len(plains)
    plains_np=np.array(plains)
    plains_np.resize(math.ceil(num/hill_n),hill_n)    #""" #num//c?????? """
    #进行运算
    ciphers_np=plains_np.dot(encry_key)
    ciphers=ciphers_np.reshape(ciphers_np.size)[:num].tolist()
    #转换为字母
    ciphertext_content=''
    for cipher in ciphers:
        cipher=cipher%26
        ciphertext_content=ciphertext_content+string.ascii_uppercase[cipher]
    print('加密结果为：'.rjust(20),ciphertext_content)
    return ciphertext_content

def encry_decry(encry_key):
    det=int(np.linalg.det(encry_key))
    inv=modreverse(det,26)
    adjoint=np.linalg.inv(encry_key)*det
    decry_key=(adjoint*inv)%26
    return decry_key 



#解密算法
def decode(decry_key,hill_n,ciphertext_content):
    #分割、整理明文
    ciphers=[]
    for ciphertext in ciphertext_content:
        if ciphertext in string.ascii_uppercase:
            cipher=(ord(ciphertext)-ord('A'))%26
            ciphers.append(cipher)
    num=len(ciphers)
    ciphers_np=np.array(ciphers)
    ciphers_np.resize(math.ceil(num/hill_n),hill_n)
    #进行解密
    plains_np=ciphers_np.dot(decry_key)
    plains=plains_np.reshape(plains_np.size)[:num].tolist()
    #转换为字母
    plaintext_content=''
    for plain in plains:
        plain=int(plain%26)
        plaintext_content=plaintext_content+string.ascii_uppercase[plain]
    print('解密结果为:'.rjust(20),plaintext_content)
    return plaintext_content

#破解算法
def crack():
    encrys=[]
    decrys=[]
    try:
        encry=input("请输入你已知的明文：")
        decry=input("请输入你已知明文的密文：")
        encry=encry.split(' ')
        decry=decry.split(' ')
        for encry_text in encry:
            if encry_text in string.ascii_uppercase:
                encry_text=(ord(encry_text)-ord('A'))%26
                encrys.append(encry_text)
        for decry_text in decry:
            if decry_text in string.ascii_uppercase:
                decry_text=(ord(decry_text)-ord('A'))%26
                decrys.append(decry_text)   
    except:
        print("输入有误！\n")
    else:
        encry_np=np.array(encrys).reshape(2,2)
        decry_np=np.array(decrys).reshape(2,2)
        #求已知明文的模逆矩阵
        det=int(np.linalg.det(encry_np))
        if gcd(det,26)==1:
            inv=modreverse(det,26)
            adjoint=np.linalg.inv(encry_np)*det
            adjoint=adjoint.astype(int)
            decry_key1=(adjoint*inv)%26
            #已知明文的模逆矩阵 与相对应密文的点乘
            print("破解得到的解密:\n",(decry_key1@decry_np)%26)
            #输出加密的密钥
        else:
            print("线性相关,无法解密")

try:
    #key=input("请输入密钥(不同行用分号)：")
    #b=np.matrix(key)

    key=input("请输入密钥(数字以空格分开)：")
    b=np.array(list(key.split()))
    hill_n=int(math.sqrt(len(b)))
    encry_key=b.reshape(hill_n,hill_n).astype(int)
    decry_key=encry_decry(encry_key)
    print("解密密钥:\n",decry_key)
except:
    print('输入密钥不符合要求')
else:
     #密文输入   
     plaintext_files_location=input('请输入明文的位置:')
     try:
         plaintext_files=open(plaintext_files_location,'r')
     except:
         print('打开明文文件失败！\n')
     else:
         plaintext_content=plaintext_files.read()
         print('输入明文为：'.rjust(20),plaintext_content)
         ciphertext_content=encode(encry_key,hill_n,plaintext_content)
         plaintext_content=decode(decry_key,hill_n,ciphertext_content)
         crack()

    
"""
测试密钥：1 2 0 3

测试已知明文 D D S L
测试已知密文 D P S R
"""


     
"""
测试解密算法
decry_key=np.array([[1,8],[0,9]])
hill_n=2
ciphertext_content='DPSRSMOEJYJUOEXWUQSFDEDB'
decode(decry_key,hill_n,ciphertext_content)

"""



    





