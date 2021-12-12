import socket

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
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        for port in range(65536):
            try:
                print(self.host_ip)
                s.connect(('0.0.0.0', port))
                self.send_inf(f'ALIVE:{self.host_ip}')
                self.node_list.append(port)
            except:
                pass
            finally:
                s.close()
        
        print(f'已发现{len(self.node_list)}个节点')
        #返回list给node
        return self.node_list
        
    def send_inf(self, data):

        for s in self.node_list:
            try:
                s.send(b'{}'.format(data))
            finally:
                s.close()

upnp = UPnP()
upnp.discovery_node()
