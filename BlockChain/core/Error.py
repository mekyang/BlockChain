class AddressError(Exception):
   
    def __init__(self, address):
        self.address = address

    def __str__(self):
        return f' AddressError:{self.address}不是合法的地址'

class HashCheckError(Exception):

    def __str__(self):
        return 'HashCheckError:块哈希不匹配'   

class FalseChainError(Exception):

    def __str__(self):
        return 'FalseChainError:链无法连接'

class ReadDataError(Exception):

    def __str__(self):
        return '读取数据文件时出现问题'