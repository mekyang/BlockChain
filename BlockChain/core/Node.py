import pickle
import re
from os.path import getsize
from core.Error import *
import socket
from core.Method import *
from core.Chain import Chain

class Node(object):

    #只负责本地持久化，运行时临时数据都保存在chain里，结束后统一通过node写入
    def __init__(self, address, chain_file, node_file):

        #校验地址合法性
        self.node_list = []
        self.block_chain = []
        if re.match(r'^[a-zA-Z]:(((/(?! )[^/:*?<>\""|/]+)+/?)|(/)?)\s*$', address):
            self.data_address = chain_file
            self.node_address = node_file
        else:
            raise AddressError(address)


    def load_block_inf(self):

        #读取后传给chain
        #文件存在或权限问题(IOerror)可能被抛出
        #判断文件中有无内容
        if getsize(self.data_address) != 0:
            try:
                with open(self.data_address, 'rb') as f:
                    block_chain = f.read()
                    return pickle.loads(block_chain)
            except:
                raise ReadDataError
        else:
            return []

    def load_node_list(self):
        #后续实现
        pass

    def save_block(self, block_chain):
        #进程结束后由chain返回最后链
        with open(self.data_address, 'wb') as bc:
                pickle.dump(block_chain, bc)
    
    def save_node_list(self):
        #保存node集
        with open(self.node_address, 'wb') as bcn:
            pickle.dump(self.node_list, bcn)
    
    def node_listen(self, host, port):
        #监听并执行
        serve = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serve.bind((host, port))
        serve.listen(5)

        while True:
            cs,addr = serve.accept()      
            self.node_list.append(addr[1])
            buffer = []
            while True:
                data = cs.recv(1024)
                buffer.append(data)
                if not data:
                    break
            #执行远程命令
            res = self.util_method(data)
            eval(f'self.method_{res[0]}({res[1]}, {res[2]}')
    
    def send_inf(self, data):

        for s in self.node_list:
            try:
                s.send(b'{}'.format(data))
            finally:
                s.close()

    def broadcast(self, block):
        #向网络广播信息
        self.send_inf(f"MINE:{block['block ID']};BLOCK:{block}")

    def get_chain_from_other(self):
        #从其他节点上获取链
        self.send_inf(f'GETNODE:get;')

    def method_ALIVE(self, value, body):
        self.node_list.append(value)

    def method_GETNODE(self, value, body):
        #body为get则为其他节点请求，为post则为自己向节点发送请求收到的回应
        if value == 'get':
            self.send_inf(f'GETNODE:post;CHAIN:{self.block_chain}')
        elif value == 'post':
            if Chain.verification(self.block_chain):
                self.block_chain = body['CHAIN']

    def method_MINE(self, value, body):
        #加入新区块
        if value == self.block_chain[-1]['block ID'] + 1:
            self.block_chain.append(body['BLOCK'])