# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 19:23:46 2018

@author: happen
"""
import numpy as np
import math
import string
import math

#matrix

def gcd(a,b):
    #if a<b:
    #    a,b=b,a
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
def encode(encry_key,encry_key_B,hill_n,plaintext_content):
    #分割、整理明文
    plains=[]
    #flag=0
    for plaintext in plaintext_content:
        if plaintext in string.ascii_uppercase:
            plain=(ord(plaintext)-ord('A'))%26
            plains.append(plain)
    num=len(plains)
    plains_np=np.array(plains)
    plains_np.resize(math.ceil(num/hill_n),hill_n)    #""" #num//c?????? """
    #进行运算
    ciphers_np=plains_np.dot(encry_key)+encry_key_B
    ciphers=ciphers_np.reshape(ciphers_np.size)[:num].tolist()
    #转换为字母
    ciphertext_content=''
    for cipher in ciphers:
        cipher=cipher%26
        ciphertext_content=ciphertext_content+string.ascii_uppercase[cipher]
    print('加密结果为：'.rjust(25),ciphertext_content)
    return ciphertext_content

    



#解密算法
def decode(decry_key,encry_key_B,hill_n,ciphertext_content):
    #flag=0
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
    plains_np=(ciphers_np-encry_key_B).dot(decry_key)
    plains=plains_np.reshape(plains_np.size)[:num].tolist()
    #转换为字母
    plaintext_content=''
    for plain in plains:
        plain=int(plain%26)
        plaintext_content=plaintext_content+string.ascii_uppercase[plain]
    print('解密结果为'.rjust(25),plaintext_content)
    return plaintext_content

#生成密钥
def key():
    key=input("请输入hill密码的阶数：")
    hill_n=int(key)
    eye_n=np.eye(hill_n,dtype=int)
    encry_key_B=np.random.randint(0,26,hill_n).reshape(hill_n)
    while 1:
        encry_key=np.random.randint(0,26,hill_n**2).reshape(hill_n,hill_n)
        det=int(np.linalg.det(encry_key))
        if gcd(det,26)==1 and det:
            inv=modreverse(det,26)
            #逆元求解
            adjoint=np.linalg.inv(encry_key)*det
            #伴随矩阵
            adjoint=adjoint.astype(int)
            decry_key=(adjoint*inv)%26
            #模逆矩阵
            if (((decry_key@encry_key)%26)==eye_n).all():
                break
    print('解密密钥A-1是：\n',decry_key)
    print('加密密钥A是：\n',encry_key)
    print('密钥B是:',encry_key_B)
    return decry_key,encry_key,encry_key_B


if __name__ == "__main__":
    decry_key,encry_key,encry_key_B=key()
    plaintext_files_location=input('请输入明文的位置:')
    hill_n=np.shape(encry_key_B)[0]
    #加载明文加解密
    try:
        plaintext_files=open(plaintext_files_location,'r')
    except:
        print('打开明文文件失败！\n')
    else:
        plaintext_content=plaintext_files.read()
        plaintext_files.close()
        print('输入的明文为：'.rjust(25),plaintext_content)
        ciphertext_content=encode(encry_key,encry_key_B,hill_n,plaintext_content)
        plaintext_content=decode(decry_key,encry_key_B,hill_n,ciphertext_content)
 
    
#长度改变错误？？？？？



"""
#全文测试
try:
    #key=input("请输入密钥(不同行用分号)：")
    #b=np.matrix(key)

    key=input("请输入密钥(数字以空格分开)：")
    b=np.array(list(key.split()))
    hill_n=int(math.sqrt(len(b)))
    encry_key=b.reshape(hill_n,hill_n).astype(int)
    decry_key=encry_decry(encry_key)
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
         print('输入的明文为：'.rjust(25),plaintext_content)
         
         #ciphertext_content=encode(b,2,plaintext_content)
         #plaintext_content=decode(b,2,ciphertext_content)
        
         ciphertext_content=encode(encry_key,hill_n,plaintext_content)
         plaintext_content=decode(decry_key,hill_n,ciphertext_content)
"""
"""

#密钥计算
def encry_decry(encry_key):
    det=int(np.linalg.det(encry_key))
    inv=modreverse(det,26)
    adjoint=np.linalg.inv(encry_key)*det
    decry_key=(adjoint*inv)%26
    return decry_key
"""
     
"""
测试解密算法
decry_key=np.array([[1,8],[0,9]])
hill_n=2
ciphertext_content='DPSRSMOEJYJUOEXWUQSFDEDB'
decode(decry_key,hill_n,ciphertext_content)

"""
