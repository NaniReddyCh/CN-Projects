import socket
import struct
import time
import os

file_path = "testFile.jpg"  
recv_address = ("10.0.0.2", 20002)
buffer_limit = 1024
timeout_ms = int(input("Enter the retransmission timeout (in milliseconds): "))
timeout = timeout_ms / 1000
 
sequence_number = 0  
retransmission_count = 0


udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.settimeout(timeout)  

file_size_kb = os.path.getsize(file_path) / 1024  
start_time = time.time()  

with open(file_path, "rb") as f:
    while True:
        data = f.read(buffer_limit - 3)  
        eof_flag = 1 if not data else 0  

        
        packet = struct.pack("!BB1021s", sequence_number, eof_flag, data)
        
        while True:
            
            udp_socket.sendto(packet, recv_address)

            try:
                
                ack_packet, _ = udp_socket.recvfrom(1024)
                ack_seq = struct.unpack("!B", ack_packet)[0]

                
                if ack_seq == sequence_number:
                    print("ACK received for Seq:", sequence_number)
                    sequence_number = 1 - sequence_number  
                    break  
            except socket.timeout:
                print("Timeout, retransmitting Seq:", sequence_number)
                retransmission_count += 1

        
        if eof_flag:
            break

end_time = time.time()  
transfer_time = end_time - start_time
throughput_kbps = file_size_kb / transfer_time
print("Average Throughput: {:.2f} KB/s".format(throughput_kbps))
print("Total retransmissions:", retransmission_count)