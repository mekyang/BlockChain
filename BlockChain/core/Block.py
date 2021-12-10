from hashlib import sha256
from time import time, asctime, localtime

block_inf = '''
        ----------------------Block Information------------------------------------------------------
        bloackchain version:    {}
        block ID:               {}  
        block calculated time:  {}
        previous block hash:    {}
        block data:             {}
        block hash:             {}
        nonce:                  {}
        ---------------------------------------------------------------------------------------------
        '''

class Block(object):

    def __str__(self):

        return block_inf.format(self.version,
                                self.block_ID,
                                self.time_format,
                                self.previous,
                                self.block_data,
                                self.block_hash,
                                self.nonce)

    def __init__(self, pre_hash, bk_data, version, block_ID):

        self.version     = version
        self.block_ID    = int(block_ID)
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
            'block ID'      : self.block_ID,
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

    def mine(self, difficulty = 3):

        target = '0' * difficulty

        while self.block_hash[:difficulty] != target:
            self.nonce += 1
            self.block_hash = self.calculateHash()

        print(f'Mined Block!(nonce={self.nonce})')