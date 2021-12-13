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

#只处理链相关的问题

block_chain = []

def get_block_ID():
    #取块的id
    return int(block_chain[-1]['block ID']) + 1

def get_previous_hash():

    return block_chain[-1]['hash']

def append_block(block):

    block_chain.append(block)
    print(block_chain)
    
def verification():
    #检验本地链的完整性

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
    
#def UTXO(self):
#    #临时的UTXO信息

#    pass

def return_chain_status():

    #退出时把所有的更新状态返回给node写入本地
    return (block_chain, 0) #0占位utxo




