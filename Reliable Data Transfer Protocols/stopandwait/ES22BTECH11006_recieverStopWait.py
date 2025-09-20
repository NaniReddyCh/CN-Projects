import socket
import struct

recv_ip = "10.0.0.2"
recv_port = 20002
buffer_limit = 1024  
output_file = "recFile.jpg"
expected_sequence = 0  


udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((recv_ip, recv_port))

print("Receiver UDP socket active...")


with open(output_file, "wb") as f:
    while True:
        packet, sender_info = udp_socket.recvfrom(buffer_limit + 3)  
        seq_num, eof_flag, data = struct.unpack("!BB1021s", packet)

        if seq_num == expected_sequence:
            
            if data:
                if eof_flag:
                    f.write(data.rstrip(b'\x00'))
                else:
                    f.write(data)  


            print("Received Seq:", seq_num)
            expected_sequence = 1 - expected_sequence  
        else:
            print("Duplicate packet discarded:", seq_num)

        
        ack_packet = struct.pack("!B", seq_num)
        udp_socket.sendto(ack_packet, sender_info)

        
        if eof_flag:
            print("End of file received. File saved as {}".format(output_file))
            break