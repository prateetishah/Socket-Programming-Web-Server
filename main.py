# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# from socket import *
# from http import HTTPStatus
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
# def tcp_Server_Socket_Prog():
#     # import socket module
#     # from socket import *
#     import sys  # In order to terminate the program
#
#     server_socket = socket(AF_INET, SOCK_STREAM)
#     # Prepare a server socket
#     server_socket.bind(('127.0.0.1', 80))
#     server_socket.listen()
#
#     print('The server is ready to receive.')
#
#     while True:
#     # Establish the connection
#         print('Ready to serve...')
#         connectionSocket, addr = server_socket.accept()
#         try:
#             message = connectionSocket.recv(1024)
#             filename = message.split()[1]
#             f = open(filename[1:])
#             outputdata = f.read()
#             # print(outputdata)
#             # Send one HTTP header line into socket
#             # Fill in start
#             # Fill in end
#             connectionSocket.send(("200 OK").encode())
#             # # Send the content of the requested file to the client
#             for i in range(0, len(outputdata)):
#                 connectionSocket.send(outputdata[i].encode())
#             connectionSocket.send("\r\n".encode())
#             connectionSocket.close()
#
#         except IOError as error:
#             # Send response message for file not found
#             print(error)
#             # Fill in start
#             # Fill in end
#             # Close client socket
#
#             # Fill in start
#             # Fill in end
#             server_socket.close()
#             sys.exit()  # Terminate the program after sending the corresponding data
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#     tcp_Server_Socket_Prog()
#
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
from socket import *
import sys

HOST = "127.0.0.1"
PORT = 80


def tcp_server_socket_prog():
    server_socket = socket(AF_INET, SOCK_STREAM)
    # Prepare a server socket
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    while True:
        # Establish the connection
        print('Ready to serve...')
        connection_socket, addr = server_socket.accept()
        try:
            message = connection_socket.recv(1024000)
            filename = message.split()[1]
            f = open(filename[1:])
            output_data = f.read()
            # Send one HTTP header line into socket
            connection_socket.send(b'200 OK')
            # connection_socket.sendall(output_data.encode())
            # Send the content of the requested file to the client
            for i in range(0, len(output_data)):
                connection_socket.send(output_data[i].encode())
            connection_socket.send("\r\n".encode())
            connection_socket.close()

        except IOError:
            # Send response message for file not found
            connection_socket.send(b'404 File not found')
            connection_socket.close()
            # Close client socket
            server_socket.close()


if __name__ == '__main__':
    tcp_server_socket_prog()