import socket
import threading

class UPnP(object):
    """未开放，目前仅使用内网不同端口模拟网络
       目前所有代码都将被废弃
       类名只是代表未来功能，与目前类中功能无关
    """
    def __init__(self):

        self.host_ip   = self.get_host_ip()
        gate = self.host_ip.split('.')
        #gate[3] = '0'
        #self.host_gateway = gate.join('.')
        self.node_list = []

    def get_host_ip(self):
        #获取本机IP
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        except:
            print('无法获取IP')
        finally:
            s.close()

        return ip

    def discovery_node(self):
        #采用不同端口模拟不同设备
        #未来将实现从其他节点获取节点列表，测试存活并更新自己的列表
        thread_list = []

        for port in range(2000, 3000):
            def run(port):
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((self.host_ip, port))
                    s.send(f'ALIVE:{self.host_ip};'.encode())
                    self.node_list.append(port)
                except:
                    pass
                finally:
                    s.close()
            thread_list.append(threading.Thread(target=run, args=(port,)))
        for thread in thread_list:
            thread.start()
        for thread in thread_list:
            thread.join()

        print(f'已发现{len(self.node_list)}个节点')
        print(self.node_list)
        #返回list给node
        return self.node_list
