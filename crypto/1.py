import os
import string

#求最大公约数
def gcd(a,b):
    if a<b:
        a,b=b,a
    while b:
        a,b=b,a%b
    return a

def gcd1(a,b):
    if b:
        return gcd1(b,a%b)
    else:
        return a

#加密算法
def encode(a,b,plaintext_content):
    ciphertext_content=''
    for plaintext in plaintext_content:
        if plaintext in string.ascii_uppercase:
            ciphertext=((ord(plaintext)-ord('A'))*a+b)%26
            ciphertext_content=ciphertext_content+string.ascii_uppercase[ciphertext]
    print('加密结果为：'.rjust(12),ciphertext_content)
    return ciphertext_content


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
   

#解密算法
def decode(aaa,b,ciphertext_content):
    plaintext_content=''
    for ciphertext in ciphertext_content:
        if ciphertext in string.ascii_uppercase:
            plaintext=(aaa*(ord(ciphertext)-ord('A')-b))%26
            plaintext_content=plaintext_content+string.ascii_uppercase[plaintext]
    print('揭秘结果为：'.rjust(12),plaintext_content)
    return plaintext_content

try:
    #参数选取
    while 1:
        a=input('请输入a的值：')
        b=input('请输入b的值：')
        a,b=int(a),int(b)
        if a in range(26) and b in range(26) and gcd(a,26)==1:
            aaa=modreverse(a,26)
            print('解密密钥为:',aaa)
            break
        else:
            print('参数不符合条件，请重新输入\n')
except:
        pass
else:
    #密文输入   
    plaintext_files_location=input('请输入明文的位置:')
    try:
        plaintext_files=open(plaintext_files_location,'r')
    except:
        print('打开明文文件失败！\n')
    else:
        plaintext_content=plaintext_files.read()
        print('输入的明文为：'.rjust(12),plaintext_content)
        ciphertext_content=encode(a,b,plaintext_content)
        plaintext_content=decode(aaa,b,ciphertext_content)