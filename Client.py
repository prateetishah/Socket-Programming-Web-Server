import sys
from socket import *


def tcp_client_socket_prog(server_host, server_port, filename):
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    REQUEST = "GET /" + filename + " HTTP/1.1\r\nHost: " + server_host + "\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36\r\nAccept-Language: en-US\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nSec-GPC: 1\r\nSec-Fetch-Site: none\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\nSec-Fetch-Dest: document\r\nAccept-Encoding: gzip, deflate, br\r\n\r\n"
    client_socket.sendall(REQUEST.encode())
    server_response = client_socket.recv(1024)
    print("From Server: ", server_response)
    while server_response:
        print(server_response.decode())
        server_response = client_socket.recv(1024 * 10**6)
    client_socket.close()

arguments = sys.argv
tcp_client_socket_prog(arguments[1], int(arguments[2]), arguments[3])