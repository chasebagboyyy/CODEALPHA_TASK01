import socket
import struct
import textwrap

def main():
    # Create a raw socket to capture all packets
    conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    
    # Bind the socket to the local host
    conn.bind(('0.0.0.0', 0))
    
    # Include IP headers in the captured packets
    conn.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    print("Listening for incoming packets...")
    
    while True:
        # Receive a packet
        raw_data, addr = conn.recvfrom(65536)
        print(f"Packet received from {addr}")
        process_packet(raw_data)

def process_packet(raw_data):
    # Unpack the IP header from the raw data
    ip_header = raw_data[:20]
    unpacked = struct.unpack('!BBHHHBBH4s4s', ip_header)

    version_ihl = unpacked[0]
    version = version_ihl >> 4
    ihl = (version_ihl & 0xF) * 4
    ttl = unpacked[5]
    proto = unpacked[6]
    src = socket.inet_ntoa(unpacked[8])
    target = socket.inet_ntoa(unpacked[9])

    print(f"IP Header:")
    print(f"  Version: {version}")
    print(f"  Header Length: {ihl} bytes")
    print(f"  TTL: {ttl}")
    print(f"  Protocol: {proto}")
    print(f"  Source IP: {src}")
    print(f"  Destination IP: {target}")

    # Format and display the raw data payload
    data = raw_data[ihl:]
    print(f"Data:")
    print(format_multi_line(data))
    print("\n")

def format_multi_line(data, width=80):
    # Split binary data into readable lines
    if isinstance(data, bytes):
        data = ' '.join(f"{byte:02x}" for byte in data)
    return '\n'.join(textwrap.wrap(data, width))

if __name__ == "__main__":
    main()
