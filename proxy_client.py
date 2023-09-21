import socket

BYTES_TO_READ = 4096

def get(host, port):
    request = b"GET / HPPT/1.1\nHost: www.google.com\n\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #AF_NET => IPv4, SOCK_STREAM => TCP
        s.connect((host,port))
        s.send(request)
        s.shutdown(socket.SHUT_WR) # socket can write # socket can read # so we shut down the write side, and then get
        chunk = s.recv(BYTES_TO_READ)
        result = b''+ chunk
        
        while(len(chunk)>0):
            chunk = s.recv(BYTES_TO_READ)
            result += chunk
        s.close() # the empty bytestring was sent
        return result
    
print(get("127.0.0.1", 8080))