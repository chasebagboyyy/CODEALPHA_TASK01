# CODEALPHA_TASK01
BASIC NETWORK SNIFFER Build a network sniffer in Python that captures and analyzes network traffic. This project will help you understand how data flows on a network and how network packets are structured.
# NETWORK SNIFFER 

This is a simple network sniffer I built in Python to capture and analyze network traffic. It’s a small project to help understand how network packets work and how data moves across a network.

**WHAT IT DOES**

Captures network packets in real-time (yeah, the ones flying around!).

Decodes the IP headers to show stuff like:

Protocol version (IPv4, etc.)

Header size

TTL (how long the packet "lives")

Source and Destination IP addresses

Also spits out the raw packet data in a readable way (cool for debugging or just learning).


**HOW TO USE IT**

1. Download the script (or copy it, whatever works).

2. Open a terminal and go to the folder where you saved the script.

3. Run this command (requires admin rights):

bash

sudo python3 network_sniffer.py

4. All incoming packets will be shown. 

**SOFTWARE REQUIRED AND PROCESS**

1. Python 3 needed to be installed.
   
2. This works best on Linux because it uses raw sockets. On Windows, you might need to tweak the code (hint: replace socket.IPPROTO_IP with socket.IPPROTO_TCP).
