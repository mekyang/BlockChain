from core.Block import Block
from core.Chain import Chain
from core.Node import Node
from core.Error import *
import configparser

print('********************************************************************************************')

#加载ini
config = configparser.ConfigParser()
path = 'config.ini'
config.read(path)
#以下是帮助信息（当new为true时运行则会直接弹出帮助）
help_config = 0
help = 0
new = eval(config['select']['new'])

def set_config():
    #对ini的操作
    if new:
        print(help_config)
    config['select']['new'] = 'False'
    while True:
        command = input('S:')

        if command == 'help':
            print(help)
        elif command == 'finish':
            return
        elif '=' in command:
            try:
                config.set('select', command.split('=')[0], command.split('=')[1].replace('\\', '/'))
                config.write(open(path, 'r+', encoding='utf-8'))
            except:
                print('错误指令')
        else:
            try:
                print(f"{command}={config['select'][command]}")
            except:
                print('错误指令')

def not_find():

    print('未知命令')

def _help():

    print(help)

def _transaction():

    previous = chain.get_previous_hash()
    block = Block(previous, data, version)
    block.mine()
    print(block)
    block = block.save_as_dic()
    chain.append_block(block)
    print('---FINISH---')

def _quit():

    block_chain = chain.return_chain_status()
    try:
        node.save_block()
    except OSError:
        return '文件不存在或无权访问'

    print('*************************************GOODBEY*************************************')

new = eval(config['select']['new'])
address = config['select']['address']

while True:
    #预开启，可以进行设置,查看介绍和开始加载
    if new:
        
        print('请先完善设置')
        set_config()
        print('正在生成数据容器......')
        f = open(config['select']['address'], 'wb')
        f.close()
        print('完毕')

    command = input('P:')

    if command == 'config':
        set_config()

    #加载
    elif command == 'start':
        try:
            node  = Node(config['select']['address'])
            chain = Chain(node.load_block_inf())
        except AddressError:
            print(AddressError(address))
        except OSError:
            print('文件不存在或无权访问')
        except ReadDataError:
            print(ReadDataError())
        print('****************************************START*******************************************')

    else:
        print('未知命令')

#命令集，用以快速执行命令
instrucion_set = {
    'tran' : _transaction,
    'quit' : _quit(),
    'help' : _help()
    }

while True:
  
    command = input('>')
    instrucion_set.get(command, not_find)()




