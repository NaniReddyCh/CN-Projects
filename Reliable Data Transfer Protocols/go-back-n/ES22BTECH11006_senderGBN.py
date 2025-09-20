import socket
import struct
import time
import os


window_size = int(input("Enter the window size (e.g., 1, 2, 4, 8): "))
timeout_ms = int(input("Enter the timeout (in milliseconds): "))
timeout = timeout_ms / 1000  


senderIP = "10.0.0.1"
senderPort = 20001
receiverAddressPort = ("10.0.0.2", 20002)
bufferSize = 1024


socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_udp.settimeout(timeout)


file_path = "testFile.jpg"
file_size = os.path.getsize(file_path)
start_time = time.time()

with open(file_path, "rb") as file:
    base = 0
    next_seq = 0
    packets = []

    
    while True:
        data = file.read(bufferSize - 4)
        if not data:
            break
        eof_flag = 1 if len(data) < (bufferSize - 4) else 0
        header = struct.pack("!HB", next_seq, eof_flag)  # 2 bytes for sequence, 1 for EOF
        packets.append(header + data)
        next_seq += 1

   
    next_seq = 0
    while base < len(packets):
        
        while next_seq < base + window_size and next_seq < len(packets):
            socket_udp.sendto(packets[next_seq], receiverAddressPort)
            print("Sent packet Seq:", next_seq)
            next_seq += 1

        
        try:
            ack_packet, _ = socket_udp.recvfrom(bufferSize)
            ack_num = struct.unpack("!H", ack_packet)[0]  # Unpack ACK sequence number
            print("Received ACK for Seq:", ack_num)
            base = ack_num + 1
        except socket.timeout:
            print("Timeout, retransmitting from base Seq:", base)
            next_seq = base  # Retransmit from the base of the window

end_time = time.time()
total_time = end_time - start_time
throughput = file_size / total_time / 1024
print("File transfer completed.")
print("Throughput: %.2f KB/s" % throughput)
socket_udp.close()