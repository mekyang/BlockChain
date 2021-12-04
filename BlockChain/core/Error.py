class AddressError(Exception):
   
    def __init__(self, address):
        self.address = address

    def __str__(self):
        return f'{self.address}不是合法的地址'

class HashCheckError(Exception):

    def __str__(self):
        return '块哈希不匹配'   

class FalseChainError(Exception):

    def __str__(self):
        return '链无法连接'

