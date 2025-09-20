import socket
import struct
import os

recv_ip = "10.0.0.2"
recv_port = 20002
buffer_limit = 1024  # 1 KB
output_file = "recFile.jpg"  


udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((recv_ip, recv_port))

print("Receiver UDP socket active...")


with open(output_file, "wb") as f:
    while True:
        packet, sender_info = udp_socket.recvfrom(buffer_limit + 3)  
        seq_num, eof_flag, data = struct.unpack("!HB1021s", packet)
        
        print("Received Seq:{} | EOF:{}".format(seq_num, bool(eof_flag)))
        
        
        if eof_flag:
            f.write(data.rstrip(b'\x00'))  
        else:
            f.write(data)  

        
        response = "Ack:{}".format(seq_num).encode()
        udp_socket.sendto(response, sender_info)

        
        if eof_flag:
            print("End of file received. File saved as {}".format(output_file))
            break