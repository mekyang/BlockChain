from core.Error import *

def util_method(data):

    try:
        lines = data.split(';')
        method_dic = {}
        for line in lines:
            method_dic[line.split(':')[0]] = line.split(':')[1]
        
        method1_value = method_dic.pop(method_dic.keys()[0])
        return (method_dic.keys()[0], method1_value, method_dic)

    except:
        raise CanNotUtilError(data)
