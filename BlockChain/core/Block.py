from hashlib import sha256
from time import time, asctime, localtime

class Block(object):

    def __str__(self):

        print('----------------------Block Information------------------------------------------------------')
        print('bloackchain version:    v1.0.0')
        print(f'block calculated time:  {self.time_format}')
        print(f'previous block hash:    {self.previous}') 
        print(f'block data:             {self.block_data}')
        print(f'block hash:             {self.block_hash}')
        print(f'nonce:                  {self.nonce}')
        print('---------------------------------------------------------------------------------------------')

        return ''

    def __init__(self, pre_hash, bk_data, version):

        self.version     = version
        self.nonce       = 0
        self.previous    = pre_hash
        self.block_data  = bk_data
        self.time_stamp  = time()
        self.time_format = asctime(localtime(time()))
        
        self.block_hash = self.calculateHash()

    def save_as_dic(self):

        block_dic = {
            'hash'          : self.block_hash,
            'block version' : self.version,
            'nonce'         : self.nonce,
            'previous hash' : self.previous,
            'block data'    : self.block_data,
            'time'          : self.time_format,
            'time stamp'    : self.time_stamp
            }
        #作为数据本地化的容器
        return block_dic

    def calculateHash(self):

        block_inf = (
            self.previous        + 
            str(self.time_stamp) + 
            self.block_data      +
            str(self.nonce)
            ).encode("utf8")

        return sha256(block_inf).hexdigest()

    def mine(self, difficulty = 5):

        target = '0' * difficulty

        while self.block_hash[:difficulty] != target:
            self.nonce += 1
            self.block_hash = self.calculateHash()

        print(f'Mined Block!(nonce={self.nonce})')