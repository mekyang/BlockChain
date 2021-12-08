import pickle
import re
from os.path import getsize
from core.Error import *


class Node(object):

    #只负责本地持久化，运行时临时数据都保存在chain里，结束后统一通过node写入
    def __init__(self, address):

        #校验地址合法性
        if re.match(r'^[a-zA-Z]:(((/(?! )[^/:*?<>\""|/]+)+/?)|(/)?)\s*$', address):
            self.data_address = address
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

    def save_block(self, block_chain):
        
        #进程结束后由chain返回最后链
        with open(self.data_address, 'wb'):
                pickle.dumps(block_chain)

    def broadcast():
        #向网络广播信息
        pass

    def get_chain_from_other(self):
        #从其他节点上获取链
        pass
