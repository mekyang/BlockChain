from core.Block import Block, block_inf
from core.Chain import *
from core.Node import Node
from core.UPnP import UPnP
from core.Error import *

help = 0

def listen(port):
    node.node_listen(upnp.host_ip, port)

#def time_server():

def start(path, chain_file, node_file, _version):
    global node
    global upnp
    global version
    global block_chain
    version = _version

    try:
        node  = Node(path, chain_file, node_file)
        node.block_chain = node.load_block_inf()
        block_chain = node.block_chain
        upnp  = UPnP()
        node.node_list = upnp.discovery_node()
    except AddressError:
        print(AddressError(path))
    except OSError:
        print('文件不存在或无权访问')
    except ReadDataError:
        print(ReadDataError())
        print('****************************************START*******************************************')
    #生成创世块
    if not block_chain:
        block = Block('0', 'FIRST', _version, '0')
        block.mine()
        print(block)
        print('创世块已经生成')
        block = block.save_as_dic()
        append_block(block)

def not_find():

    print('未知命令')

def _help():

    print(help)

def _transaction():

    data = input('T(data):')

    previous = get_previous_hash()
    block_ID = get_block_ID()
    block = Block(previous, data, version, block_ID)
    block.mine()
    print(block)
    block = block.save_as_dic()
    append_block(block)
    print('---FINISH---')

def _queryheight():

    print(f'block height : {len(block_chain)}')

def _queryblock():

    block_ID = input('Q:')
    blocks = eval(f'block_chain[{block_ID}]')
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

    block_chain = return_chain_status()
    try:
        node.save_block(block_chain)
        node.save_node_list()

    except OSError:
        print('文件不存在或无权访问')

def _verification():

    try:
        verification()
    except Exception as e:
        print(e)

def _debug():

    while True:
        debug = input('D:')
        if debug == 'quit':
            break
        eval(debug)

#命令集，用以快速执行命令
instrucion_set = {
    'tran'   : _transaction,
    'quit'   : _quit,
    'help'   : _help,
    'height' : _queryheight,
    'query'  : _queryblock,
    'verf'   : _verification,
    'debug'  : _debug
    }