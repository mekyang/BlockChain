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
        return 'ReadDataError:读取数据文件时出现问题'

class CanNotUtilError(Exception):

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f'CanNotUtilError:{self.data}无法处理'

class DisunderstandMethodError(Exception):

    def __init__(self, method):
        self.method = method

    def __str__(self):
        return f'DisunderstandMethodError:{self.method}无法识别命令'