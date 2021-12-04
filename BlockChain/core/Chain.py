import pickle
import re

class Chain(object):

    def __init__(self, address):

        #校验地址合法性
        if re.match(r'^[a-zA-Z]:(((\\(?! )[^/:*?<>\""|\\]+)+\\?)|(\\)?)\s*$', address):
            self.data_address = address
        else:
            raise AddressError(address)

        self.block_chain = self.load_block_inf()

    def load_block_inf():

        #文件存在或权限问题(IOerror)可能被抛出
        with open('rb', self.data_address) as f:
            block_chain = f.read()
            return pickle.loads(block_chain)

    def save_block(self, block, local = False):
        
        if not local:
            self.block_chain.append(block)
        else:
            with open(address, 'wb'):
                pickle.dumps(self.block_chain)

    def UTXO(self):
        #维护的UTXO信息

        pass

    def get_block_chain(self):
        #从其他节点上获取链

        pass


