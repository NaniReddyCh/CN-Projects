import socket
import struct
import time

file_path = "testFile.jpg"  
recv_address = ("10.0.0.2", 20002)
buffer_limit = 1024
gap_ms = 0.05  # 10 ms delay

# Set up UDP socket for sender
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

with open(file_path, "rb") as f:
    seq_num = 0
    while True:
        data = f.read(buffer_limit - 3)  # Reserve space for 3-byte header
        eof_flag = 1 if not data else 0
        packet = struct.pack("!HB1021s", seq_num, eof_flag, data)
        udp_socket.sendto(packet, recv_address)
        
        time.sleep(gap_ms)
        seq_num += 1
        if eof_flag:
            print("File transmission completed.")
            break