import pickle
import re
from core.Error import *


class Node(object):

    def __init__(self, address, block_chain):

        self.block_chain = block_chain
        self.block_chain  = load_block_inf()
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

    def verification():
        #检验完整性

        pre_hash = True    
        #顶部的块没有前一个块，不存在不连续链的可能性

        for block in self.block_chain:
            hash_current = calculateHash(
                        block['nonce'],
                        block['time stamp'],
                        block['block data'],
                        block['previous hash']) 

            if hash_current != block['hash']:
                #检验块hash
                raise HashCheckError()

            elif hash_current != pre_hash:
                #校验块hash与上一个块记录的哈希，检查链是否连续
                raise FalseChainError()
            
            pre_hash = block['previous hash']
 
    def broadcast():
        #向网络广播信息
        pass

    def get_chain_from_other(self):
        #从其他节点上获取链
        pass

