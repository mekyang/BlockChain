from core.Error import *

def util_method(data):

    try:
        lines = data.split(';')
        method_dic = {}
        for line in lines:
            if line == '':
                break
            line_ = line.split('-')
            method_dic[line_[0]] = line_[1]
    
        method = list(method_dic.keys())[0]
        method1_value = method_dic.pop(method)
        return (f"{method}", f"{method1_value}", method_dic)

    except:
        raise CanNotUtilError(data)

def a():
    pass
