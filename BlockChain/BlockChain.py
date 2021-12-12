import configparser
from instrucion import *

print('********************************************************************************************')

#加载ini
config = configparser.ConfigParser()
path = 'config.ini'
config.read(path)
#以下是帮助信息（当new为true时运行则会直接弹出帮助）
version = config['select']['version']
help_config = '''
输入设置名称以显示该设置值
设置名称=值 以更改设置
finish结束设置

请输入address=xx以设置存储地址
'''

new = eval(config['select']['new'])
ABNORMAL = 0
#检测是否非正常退出，若非正常退出，则下次检测是abnormal为1
if int(config['select']['abnormal']):
    ABNORMAL = 1
#正常退出quit中会更改
config.set('select', 'abnormal', '1')
config.write(open(path, 'r+', encoding='utf-8'))
chain_path = config['select']['address']
chain_file = chain_path + config['select']['chain_file']
node_file = chain_path + config['select']['node_file']

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
                    f = open(chain_file, 'wb')
                    f.close()
                    print('完毕')
            except:
                print('错误指令')
        else:
            try:
                print(f"{command}={config['select'][command]}")
            except:
                print('错误指令')

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
        start(chain_path, chain_file, node_file, version)
        break

    else:
        print('未知命令')

while True:
  
    command = input('>')
    instrucion_set.get(command, not_find)()
    #退出并取消非正常退出标志
    if command == 'quit':
        config.set('select', 'abnormal', '0')
        config.write(open(path, 'r+', encoding='utf-8'))
        print('*************************************GOODBEY*************************************')
        exit(0)
