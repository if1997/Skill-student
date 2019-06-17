from time import ctime
import string
import binascii
import binhex


e={
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}
d=[]
class read_file(object):
    def __init__(self):
        self.plaintext_files_location=input('请输入需要解密的文件的位置:')
        try:
            self.plaintext_files=open(self.plaintext_files_location,'r')
        except:
            print('打开明文文件失败！\n')
        else:
            self.plaintext_content=self.plaintext_files.read()
            #print('输入的明文为：'.rjust(25),self.plaintext_content,end='\n')
            self.plaintext_files.close()

class fun(object):
    def __init__(self):
        print(ctime())
        self.string=read_file().plaintext_content
        self.lst=[]
        self.divide()
        self.an=sorted(self.lst,key=lambda s:s[1],reverse=True)
        print(self.an[0])
        print(ctime())

    #遍历文件内容
    def divide(self):
        for i in range(0,len(self.string),2):
            self.fun(self.string[i:i+60])

    #异或运算
    def fun(self,lst):
        self.s={}    
        for i in range(128):
            c=''
            for j in range(int(len(lst)/2)):
                ch1=chr(int(lst[2*j:2*j+2],16)^i)
                c=c+ch1
            self.s[c]=self.number(c)
        self.lst.append(sorted(self.s.items(),key=lambda s:s[1],reverse=True)[0])
    
    #计算频率
    def number(self,lst):
        num=0
        for word in lst.lower():
            if word in e.keys():
                num=num+e[word]
            else:
                break
        return num


if __name__ == "__main__":
    fun()