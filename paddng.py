##
##
### PAD THE DATA

def padit(packet_data, desired_length, padding_char=b'\x00'):
    if len(packet_data) >= desired_length:
        return packet_data ## IS GOOD
    
    padding_length = desired_length - len(packet_data)
    padded_packet = packet_data + padding_char * padding_length
    return padded_packet


if __name__ =="__main__":
    padit()

packet_data = b'PADDED DATA INCOMING, CHECK YOUR SETTINGS'
desired_length = 4

padded_packet = padit(packet_data, desired_length)
print(padded_packet)