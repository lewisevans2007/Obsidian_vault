#linux 
The `ping` command is a widely used [[network]]troubleshooting tool that is available on [[Linux]] operating systems.

The `ping` command sends out a [[IMCP]] Echo Reply packet to the destination host and waits for a [[IMCP]] Echo Reply packets in response. This helps determine the availability and latency of the [[network]]connection.

## Usage

```
ping [options] <destination>
```

## Options
- `-c count`: Specifies the number of ICMP Echo Request packets to send before stopping.
- `-s packetsize`: Sets the size of the ICMP Echo Request packets.
- `-i interval`: Defines the time interval between sending each packet.
- `-t ttl`: Sets the Time-to-Live value for the packets, which determines how many [[network]]hops the packets can traverse.
- `-w deadline`: Specifies the timeout (in seconds) to wait for a response before considering the packet lost.
- `-q`: Quiet mode, which suppresses output except for summary statistics.
- `-v`: Verbose mode, which increases the verbosity of output.

## Examples
1. Basic usage: `ping example.com` This sends ICMP Echo Request packets to "example.com" and waits for ICMP Echo Reply packets to measure the response time.
2. Specifying the packet count: `ping -c 5 example.com` This sends 5 ICMP Echo Request packets to "example.com" and stops after receiving the corresponding ICMP Echo Reply packets.
3. Setting packet size: `ping -s 1000 example.com` This sends ICMP Echo Request packets with a size of 1000 bytes to "example.com". Useful for testing fragmentation and large packet handling.
4. Changing the interval: `ping -i 2 example.com` This sends ICMP Echo Request packets to "example.com" with a 2-second interval between each packet.
5. Modifying the Time-to-Live value: `ping -t 64 example.com` This sets the Time-to-Live value to 64 for the ICMP Echo Request packets. Useful for determining the number of [[network]]hops.
6. Setting a deadline: `ping -w 10 example.com` This sets a deadline of 10 seconds for each ICMP Echo Request packet. If no response is received within the specified time, the packet is considered lost.
7. Quiet mode: `ping -q example.com` This suppresses normal output and only displays the summary statistics at the end.
8. Verbose mode: `ping -v example.com` This increases the verbosity of the output, providing more detailed information about each ICMP Echo Reply packet received.