from core.Block import Block, block_inf
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
version = config['select']['version']
help_config = 0
help = 0
new = eval(config['select']['new'])
abnormal = 0
#检测是否非正常退出，若非正常退出，则下次检测是abnormal为1
if int(config['select']['abnormal']):
    abnormal = 1
#正常退出quit中会更改
config.set('select', 'abnormal', '1')
config.write(open(path, 'r+', encoding='utf-8'))

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
                #去掉空格，防止ini中二次写入
                command = command.replace(' ', '')
                config.set('select', command.split('=')[0], command.split('=')[1].replace('\\', '/'))
                config.write(open(path, 'r+', encoding='utf-8'))
                if 'address' in command:
                    print('正在生成数据容器......')
                    f = open(config['select']['address'], 'wb')
                    f.close()
                    print('完毕')
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

    data = input('T(data):')

    previous = chain.get_previous_hash()
    block_ID = chain.get_block_ID()
    block = Block(previous, data, version, block_ID)
    block.mine()
    print(block)
    block = block.save_as_dic()
    chain.append_block(block)
    print('---FINISH---')

def _queryheight():

    print(f'block height : {len(chain.block_chain)}')

def _queryblock():

    block_ID = input('Q:')
    blocks = eval(f'chain.block_chain[{block_ID}]')
    if isinstance(blocks, dict):
        blocks = [blocks]
    for block in blocks:
        print(block_inf.format(block['block version'],
                               block['block ID'],
                               block['time'],
                               block['previous hash'],
                               block['block data'],
                               block['hash'],
                               block['nonce']))

def _quit():

    block_chain = chain.return_chain_status()
    try:
        node.save_block(chain.block_chain)
        print(1)
    except OSError:
        print('文件不存在或无权访问')
    #设置正常退出标志
    config.set('select', 'abnormal', '0')
    config.write(open(path, 'r+', encoding='utf-8'))
    print('*************************************GOODBEY*************************************')
    exit(0)

new = eval(config['select']['new'])
address = config['select']['address']

while True:
    #预开启，可以进行设置,查看介绍和开始加载
    if new:
        
        print('请先完善设置')
        set_config()

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
        #生成创世块
        if not chain.block_chain:
            block = Block('0', 'FIRST', version, '0')
            block.mine()
            print(block)
            print('创世块已经生成')
            block = block.save_as_dic()
            chain.append_block(block)

        break

    else:
        print('未知命令')

#命令集，用以快速执行命令
instrucion_set = {
    'tran'   : _transaction,
    'quit'   : _quit,
    'help'   : _help,
    'height' : _queryheight,
    'query'  : _queryblock
    }

while True:
  
    command = input('>')
    instrucion_set.get(command, not_find)()
