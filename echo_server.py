import socket
from threading import Thread

BYTES_TO_READ = 4096

HOST = "127.0.0.1" # IP # LOCAL HOST
PORT = 8080

def handle_connection(conn, addr):
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(BYTES_TO_READ) # wait for a request, and when you get it, you receive it
            if not data: # if an empty byte string is received ==> b''
                break
            print(data)
            conn.sendall(data) # send it back to the client

# Start single threaded echo server
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # initialize the socket
        s.bind((HOST,PORT)) # bind to ip and port
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # for reusing the same socket
        s.listen() # listen for incoming connections
        conn, addr = s.accept() # conn = socket referring to the client, addr => address of the client [ip, port]
        handle_connection(conn, addr) # send ita response


# Start multithreaded echo server
def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen(2) # allow backlog of up to 2 connections ==> queue [waiting conn1, waiting conn2]
        while True:
            conn, addr = s.accept()
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()


start_server()
# start_threadd_server()