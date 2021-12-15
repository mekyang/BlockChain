import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.114', 2000))
#self.send(b'ALIVE:{};'.format(self.host_ip))
#self.node_list.append(port)