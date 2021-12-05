import pickle
import re
from core.Error import *


class Node(object):

    #只负责本地持久化，运行时临时数据都保存在chain里，结束后统一通过node写入
    def __init__(self, address):

        #校验地址合法性
        if re.match(r'^[a-zA-Z]:(((\\(?! )[^/:*?<>\""|\\]+)+\\?)|(\\)?)\s*$', address):
            self.data_address = address
        else:
            raise AddressError(address)

    def calculateHash(self, nonce, time_stamp, block_data, pre_block):

        block_inf = (
            pre_block       + 
            str(time_stamp) + 
            block_data      +
            str(nonce)
            ).encode("utf8")

        return sha256(block_inf).hexdigest()
    
    def load_block_inf():

        #读取后传给chain
        #文件存在或权限问题(IOerror)可能被抛出
        with open('rb', self.data_address) as f:
            block_chain = f.read()
            return pickle.loads(block_chain)

    def save_block(self, block):
        
        #进程结束后由chain返回最后链
        with open(address, 'wb'):
                pickle.dumps(self.block_chain)

    def broadcast():
        #向网络广播信息
        pass

    def get_chain_from_other(self):
        #从其他节点上获取链
        pass

    def mine():

        pass
