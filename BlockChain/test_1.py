def send_inf(data):

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.1.114', 2222))
        s.send(('{}'.format(data)).encode())
    finally:
        s.close()

def broadcast():
    #向网络广播信息
    send_inf(f"MINE 1;BLOCK {1:1,2:1}".encode())

broadcast()