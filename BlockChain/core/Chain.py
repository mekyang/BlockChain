from hashlib import sha256
from core.Error import *

def calculateHash(previous, timestamp, data, nonce):

        block_inf = (
            previous       + 
            str(timestamp) + 
            data           +
            str(nonce)
            ).encode("utf8")

        return sha256(block_inf).hexdigest()

def verification(block_chain, node_call = 0):
    #检验本地链的完整性
    #检验是否是在Node中调用
    if not node_call:
        pre_hash = block_chain[-1]['hash']
        #顶部的块没有前一个块，不存在不连续链的可能性

        for block in block_chain[::-1]:
            hash_current = calculateHash(
                        block['previous hash'],
                        block['time stamp'],
                        block['block data'],
                        block['nonce']) 

            if hash_current != block['hash']:
                #检验块hash
                raise HashCheckError()

            elif hash_current != pre_hash:
                #校验块hash与上一个块记录的哈希，检查链是否连续
                raise FalseChainError()
            
            pre_hash = block['previous hash']

        print('块校验通过')

    else:
        pre_hash = block_chain[-1]['hash']

        for block in block_chain[::-1]:
            hash_current = calculateHash(
                        block['previous hash'],
                        block['time stamp'],
                        block['block data'],
                        block['nonce'])
            if hash_current != block['hash'] or hash_current != pre_hash:
                return False

        return True

class Chain(object):
    #只处理链相关的问题

    def __init__(self):

        #通过node读取后传入
        self.block_chain = []

    def get_block_ID(self):
        #取块的id
        return int(self.block_chain[-1]['block ID']) + 1

    def get_previous_hash(self):

        return self.block_chain[-1]['hash']

    def append_block(self, block):

        self.block_chain.append(block)
    
    def UTXO(self):
        #临时的UTXO信息

        pass

    def return_chain_status(self):

        #退出时把所有的更新状态返回给node写入本地
        return (self.block_chain, 0) #0占位utxo




