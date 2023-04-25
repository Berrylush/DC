import socket
multicast_group=('224.0.0.1',10000)

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL,1)  #time to live(ttl) is set to 1

message="hello"
s.sendto(message.encode(),multicast_group)
#first run client

#Unicast
# import socket
#
# HOST = '192.168.0.103' #netstat
# # HOST = socket.gethostname()  #netstat -a
# PORT = 49648
#
# client_socket=socket.socket()
# client_socket.connect((HOST,PORT))
# while True:
#     print("Enter the message")
#     message=input()
#     client_socket.sendall(message.encode())