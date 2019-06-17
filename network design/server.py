import hashlib
import sys,os
# from PIL import Image, ImageFont, ImageDraw, ImageFilter
# import random
import socket, threading
import json
import re
import socketserver
import codecs
clients = {}    #提供 用户名->socket 映射
# file_path = os.path.join(os.path.abspath('.'),'file')
def add_onlist(dic,hostport):
    username = dic['username'] #input('输入你的用户名\n')
    # user_file = open('account.txt','r')  # 打开读取用户文件
    user_file = open('Usernow', 'r+')
    # temp_file = open('Usernow','w') # 将在线用户写入一个表
    jsuser = user_file.read()
    dict_userold = json.loads(jsuser) # 导入旧表
    # dict.update(dict2) # 这个函数可以更新字典
    user_file.close()
    dict_add = {
        username:hostport
        }
    dict_userold.update(dict_add)
    jsuser_add = json.dumps(dict_userold)
    user_file2 = open('Usernow', 'r+') 
    user_file2.write(jsuser_add)
    user_file2.close()
def del_onlist(username):
    user_file = open('Usernow', 'r+')
    jsuser = user_file.read()
    dict_userold = json.loads(jsuser) # 导入旧表
    user_file.close()
    del dict_userold[str(username)]
    jsuser_add = json.dumps(dict_userold)
    user_file2 = open('Usernow', 'w+') 
    user_file2.write(jsuser_add)
    user_file2.close()
def onlinedict():
    pass
    file = open('Usernow', 'r') 
    js = file.read()
    dicnow = json.loads(js)
    file.close()
    return dicnow

def relist_all():
    # 总表
    file = open('Userform', 'r') 
    js = file.read()
    dic = json.loads(js)
    dicn = {}
    for i in range(len(dic)):
        dicte = {
            dic['user'+ str(i)]['name']:str(i)
        }
        dicn.update(dicte)
    L1 = list(dicn.keys())
    # 在线表
    file = open('Usernow', 'r') 
    js = file.read()
    dicnow = json.loads(js)

    L1 = list(dicn.keys())
    L2 = list(dicnow.keys())
    dict_back = {}
    dict_back['Head'] = 'UserNameList'
    dict_back['type'] = 'GET'
    dict_back['ActiveUserList'] = str(L2)
    dict_back['WholeUserList'] = str(L1)
    # return L1,L2
    return dict_back

def verify(db,hostport):
    print(db)    
    name = db['username'] 
    passwd = db['password']
    # user_file = open('account.txt','r')  # 打开读取用户文件
    user_file = open('Userform', 'r')
    # temp_file = open('Usernow','a+') # 将登陆用户写入一个表
    jsuser = user_file.read()
    dict_userold = json.loads(jsuser) # 导入旧表
    dict_passverify = {}
    dict_passverify['Head'] = 'login'
    dict_passverify['type'] = 'GET' 
    print(len(dict_userold))
    flag = len(dict_userold)
    for i in range(len(dict_userold)):
        # print(dict_userold['user'+ str(i)]['name'])
        if name == dict_userold['user'+ str(i)]['name'] and passwd == dict_userold['user'+ str(i)]['password']:                      
            if name in onlinedict():
                flag = 0
                break  
            dict_passverify['Flag'] = 1
            dict_passverify['content'] = 'welcome'
            #send_back(dict_passverify)
            print('welcome')
            add_onlist(db,hostport)
            break
        else:
            flag -= 1
            continue
    if flag == 0:
            dict_passverify['Flag'] = 0
            dict_passverify['content'] = 'user-or-password-error'
            #send_back(dict_passverify)
            print('user-or-password-error')
    return dict_passverify

def register(db):
    # print(db)    
    name = db['username'] 
    passwd = db['password']
    username = name #input('输入你的用户名\n')
    # user_file = open('account.txt','r')  # 打开读取用户文件
    user_file = open('Userform', 'r')
    # temp_file = open('Usernow','w') # 将在线用户写入一个表
    jsuser = user_file.read()
    dict_userold = json.loads(jsuser) # 导入旧表
    # dict.update(dict2) # 这个函数可以更新字典
    user_file.close()
    dict_register = {}
    dict_register['Head'] = 'register'
    dict_register['type'] = 'GET'
    flag = 0
    for i in range(len(dict_userold)):
        if dict_userold['user'+ str(i)]['name'] == username:            
            dict_register['Flag'] = 0
            dict_register['content'] = '用户已存在'
            #send_back(dict_register)
            print('用户名已存在')
            break
        elif dict_userold['user'+ str(len(dict_userold)-1)]['name'] != username:
            flag = 1
            break
        else:
            continue
    if flag:
        secret = passwd # input('输入你的密码:\n')
        dicta = {'number': 0, 'lower': 0, 'upper': 0, 'other': 0}
        for item in secret:
            if item.isdigit():
                dicta['number'] += 1
            elif item.islower():
                dicta['lower'] += 1
            elif item.isupper():
                dicta['upper'] += 1
            else:
                dicta['other'] += 1
        if dicta['number'] + dicta['lower'] + dicta['upper'] + dicta['other'] < 4:
            dict_register['Flag'] = 0
            dict_register['content'] = '密码至少大于四位'
            #send_back(dict_register)
            print('密码至少大于四位')
        elif dicta['lower'] < 1 or dicta['number'] < 1 : # or dicta['upper'] < 1 or dicta['other'] < 1: 
            dict_register['Flag'] = 0
            dict_register['content'] = '密码至少要有一个小写字母以及一个数字'
            #send_back(dict_register)
            print('密码至少要有一个小写字母以及一个数字')
        else:
            dict_register['Flag'] = 1
            dict_register['content'] = '注册成功'
            #send_back(dict_register)
            print('注册成功')
            # 存入表单
            dict_add = {
                'user'+str(len(dict_userold)):{
                        'name': username,
                        'password': secret
                        }
                }
            dict_userold.update(dict_add)
            jsuser_add = json.dumps(dict_userold)
            user_file2 = open('Userform', 'w') 
            user_file2.write(jsuser_add)
            user_file2.close()
    return dict_register

def ftpserv(Data):

    #Data = eval((sk.recv(1024)).decode('utf-8'))
    print(Data)
    # 上传暂存服务器
    dict_fileback = {}
    dict_fileback['Head'] = 'file'
    dict_fileback['type'] = 'GET'
    #dict_fileback['Flag']=1/0/2
    #dict_fileback['filename']=file
    #dict_fileback['offset']=offset
    dict_fileback['filename'] = Data['filename']
    dict_fileback['Src_name'] = Data['Src_name']
    dict_fileback['Dst_name'] = Data['Dst_name']
    #file_path = "D:/Network-Design/Testcode"
    file_path='E:/'
    filename = '/'.join((file_path, os.path.basename(Data['filename'])))
    log = "%s.%s" % (filename.split('.')[0],'log')#指定记录偏移日志文件名
    #logname = os.path.join(file_path,log)   #定义日志路径
    #print('a')
    offset=0
    flag = -1
    if os.path.exists(filename):
        if os.path.getsize(filename) == Data['filesize']:
            #sk.send('已完整存在')   
            dict_fileback['Flag'] = 1
            flag =1
            # 可以转发
        elif os.path.getsize(filename) < Data['filesize']:#需要断点续传
            with open(log) as f:
                offset = f.read().strip()   #读取偏移量
                print(offset,' 12www')
                # 发送offset
            dict_fileback['offset'] = offset
            dict_fileback['Flag'] = 2
            flag = 2
            total_len = int(offset)
            recv_data = Data['content']
            #recv_data = Data['content']
            total_len += 128
            dict_fileback['offset'] = total_len
            print(type(recv_data))
            if recv_data:
                print('sasasa')
                with open(filename,'ab') as fd:    #以追加的方式写入文件
                    print('asssss')
                    #fd.write(bytes(recv_data,encoding='utf-8'))
                    fd.write(eval(recv_data))
                    print(type(recv_data))
            with open(log,'w') as f:   #把已接收到的数据长度写入日志
                f.write(str(total_len))
        else:
            print('filerror')
    else:
        offset = 128
        print('10')
        #dict_fileback['offset'] = offset
        #sk.send()    
        total_len = 0
        dict_fileback['Flag'] = 0
        flag = 0 # 0 需要完整发送
        recv_data = Data['content']
        print(recv_data)
        #recv_data = Data['content']
        total_len = total_len+128
        dict_fileback['offset'] = total_len
        print(type(recv_data))
        print('3')
        with open(filename,'w') as fd:    #以追加的方式写入文件
            fd.write(recv_data)
            print(type(recv_data))
        print('1')
        with open(log,'w') as f:   #把已接收到的数据长度写入日志
            f.write(str(total_len))
        print('2')
    clients[Data['Src_name']].send(str(dict_fileback).encode("utf-8"))
    print('100')
     # 计算偏移量大小 即从这个位置传输或者接收
    #if flag == 1:
    #    os.remove(log)# 文件完整或者完成删除log
    #    tosend = 1
    print(dict_fileback)
    print('fileBack')
    #clients[Data['Src_name']].send(str(dict_fileback).encode("utf-8"))
    # 转发到目的地址
    
    # clients[Data['Src_name']].send(str(dict_fileback).encode("utf-8") )
'''    if tosend:
        with open(filename,'rb') as fd:
            read_lenght=0
            while True:
                send_data=fd.read(512)
                #当当前文件已读的长度等于偏移量
                if send_data and read_lenght==int(offset):
                    send_message=require_data_type().file_message_type(file,os.path.getsize(file),Src_name,Dst_name,send_data)
                    network_send_message(service_socket,send_message)
                    print(send_message)
                    read_lenght=+len(send_data)
                    break
                else:
                    continue'''


'''
        def file_message_type(self,file,size,Src_name,Dst_name):
        self.dict['Head']='file'
        self.dict['type']='POST'
        self.dict['Src_name']=Src_name
        self.dict['Dst_name']=Dst_name
        self.dict['filename']=file
        self.dict['filesize']=size
        return self.dict

        needback        

        self.dict['Head']='file'
        self.dict['type']='POST'
        self.dict['Flag']=1/0/2
        self.dict['filename']=file
        self.dict['offset']=offset

'''
def run(mysocket,addr):
    while True:
        recvmsg = mysocket.recv(1024)
        #把接收到的数据进行解码 
        print(recvmsg.decode('utf-8'))
        dicData = recvmsg.decode('utf-8')
        dicData=eval(dicData)
        # receive = input()
        print(dicData)

        if dicData['Head'] == 'UserNameList':
            a = relist_all()
            mysocket.send(str(a).encode('utf-8'))
            print(a)
        elif dicData['Head']=='message':
            #community(mysocket)
            recvData = eval(recvmsg.decode('utf-8'))
            sendto = {
                'Head':'message',
                'type':'GET',
                'Src_name':recvData['Src_name'],
                'Dst_name':recvData['Dst_name'],
                'Size':recvData['Size'],
                'msg':recvData['msg']            
            }
            print(sendto)
            if recvData['Dst_name'] in clients.keys():   
                clients[recvData['Dst_name']].send(str(sendto).encode("utf-8"))
        elif dicData['Head']=='file':
            #ftpserv(dicData)
            if dicData['Dst_name'] in clients.keys():   
                clients[dicData['Dst_name']].send(recvmsg)
            
            #ft = threading.Thread(target=ftpserv, args=(dicData))
            #ft.start()
        elif dicData['Head']=='quit':
            print('2')
            print(dicData['Src_name'])
            del_onlist(dicData['Src_name'])
            mysocket.send(str(dicData).encode('utf-8'))
            mysocket.close()
            print('%s logout' % dicData['Src_name'])
            break
        elif recvmsg <= 0:
            del_onlist(dicData['Src_name'])
            mysocket.send(str(dicData).encode('utf-8'))
            mysocket.close()
            print('%s logout' % dicData['Src_name'])
            break            
        else:
            print('error')
        # mysocket.send(str(a).encode('utf-8'))

def start():
    #创建服务端的socket对象socketserver
    socketserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port =28956
    #绑定地址（包括ip地址会端口号）
    socketserver.bind((host, port))
    #设置监听
    socketserver.listen(10)
    #等待客户端的连接
    #注意：accept()函数会返回一个元组
    #元素1为客户端的socket对象，元素2为客户端的地址(ip地址，端口号)
    #mysocket,addr = socketserver.accept()
    while True:# 总父线程
        mysocket,addr = socketserver.accept()
        #接收客户端的请求
        recvmsg = mysocket.recv(1024)
        #把接收到的数据进行解码 
        dicData = eval(recvmsg.decode('utf-8'))

        if dicData['Head'] == 'register':
            print('yes')
            a=register(dicData)
            print(a)
            mysocket.send(str(a).encode('utf-8'))            
        elif dicData['Head'] == 'login':
            a=verify(dicData,addr)
            mysocket.send(str(a).encode('utf-8'))
            print(a)
            if a['Flag'] == 1:
                username = dicData['username']
                clients[username] = mysocket
                t = threading.Thread(target=run, args=(mysocket,addr))
                t.start()
        else:
            pass
    socketserver.close()


def start_S():
    s = threading.Thread(target=start)#启用一个线程开启服务器
    s.start()#开启线程
    #start()    
if __name__ == '__main__':
    start_S()