import socket
import struct


receiverIP = "10.0.0.2"
receiverPort = 20002
bufferSize = 1024
output_file = "recFile.jpg"


socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_udp.bind((receiverIP, receiverPort))
print("Receiver UDP socket is listening...")


expected_seq_num = 0  


with open(output_file, "wb") as file:
    while True:
        
        packet, sender_address = socket_udp.recvfrom(bufferSize)
        
        
        seq_num, eof_flag = struct.unpack("!HB", packet[:3])  # 2 bytes for sequence number, 1 for EOF flag
        data = packet[3:]  # Remaining bytes are data

        
        if seq_num == expected_seq_num:
            
            file.write(data)
            print("Received packet Seq:", seq_num)

            
            ack_packet = struct.pack("!H", seq_num)
            socket_udp.sendto(ack_packet, sender_address)
            print("Sent ACK for Seq:", seq_num)

            
            expected_seq_num += 1

            
            if eof_flag == 1:
                print("File transfer completed.Saved to recFile.jpg")
                break
        else:
            
            last_ack_packet = struct.pack("!H", expected_seq_num - 1)
            socket_udp.sendto(last_ack_packet, sender_address)
            print("Out-of-order packet discarded, resent ACK for Seq:", expected_seq_num - 1)

socket_udp.close()