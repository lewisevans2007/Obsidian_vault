## How does a TCP handshake work?
The [[TCP]] handshake is a three-step process that establishes a connection between two devices in a TCP/IP network. Here's how it works:

1. [[SYN]]: The initiating device (often called the client) sends a TCP segment with the SYN (synchronize) flag set to the receiving device (often called the server). This segment contains a random sequence number to initiate the connection.

2. [[SYN-ACK]]: Upon receiving the SYN segment, the receiving device responds with a TCP segment that has both the SYN and ACK (acknowledge) flags set. The ACK flag acknowledges the client's initial sequence number, and the SYN flag indicates the server's own initial sequence number.

3. [[ACK]]: Finally, the client acknowledges the receipt of the SYN-ACK segment by sending an ACK segment. This segment has the ACK flag set and contains an incremented sequence number. At this point, the connection is established, and both devices can start exchanging data.

The TCP handshake ensures that both devices agree on initial sequence numbers, establishes synchronization, and verifies that the connection is bi-directional. It's a vital process for reliable communication in TCP/IP networks.

## What data is sent during a TCP handshake?
### Summary
During a TCP handshake, the following data is sent between the client and server:

1. Client sends a TCP segment with the SYN flag set, which includes:
   - Source and destination port numbers (identifying the communication endpoints)
   - Initial sequence number (a random value to initiate the connection)
   - TCP control flags, including the SYN flag

2. Server responds with a TCP segment containing the SYN and ACK flags set, which includes:
   - Source and destination port numbers
   - Acknowledgment number (acknowledging the client's initial sequence number)
   - Initial sequence number for the server
   - TCP control flags (SYN and ACK)

3. Client acknowledges the server's response with a TCP segment containing the ACK flag set, which includes:
   - Source and destination port numbers
   - Acknowledgment number (acknowledging the server's initial sequence number)
   - TCP control flags (ACK)

The data exchanged during the TCP handshake primarily consists of control information rather than actual application data. It establishes the initial parameters for the TCP connection, including sequence numbers and acknowledgment numbers, enabling reliable data transmission between the client and server.

## What are all the flags in TCP handshakes?
-  [[SYN]] (Synchronize): Used to initiate a TCP connection. It indicates the desire to establish a connection and includes an initial sequence number.  
-  [[ACK]] (Acknowledgment): Indicates that the acknowledgment number field is valid. It acknowledges the receipt of data and indicates the next sequence number expected.  
- [[FIN]] (Finish): Marks the end of a TCP connection. It signifies that the sender has no more data to send.
- [[RST]] (Reset): Resets a TCP connection. It is used to terminate an invalid or disrupted connection or to reject an improperly formed segment.  
- [[RST]] (Push): Requests immediate delivery of data to the receiving application, without waiting for further data accumulation. 
- [[URG]] (Urgent): Indicates the presence of urgent data in the TCP segment.