1. In the larger queue we had double the mean latency. This happened because tcp keeps on increasing the window until it fills up the larger buffer. Since the buffer is large, TCP will not know of dropped packets, so it will send at very high rates. Additionaly the buffer is so large that the latency required to empty it is also really . In the smaller buffer, TCP congestion avoidence packets are drop more quickly so TCP keeps sending packets at a reasonable rate.Thatswhy we can see bufferbloat is happening here.

2. The maximum transmit queue length on the network interface reported in ifconfig is 1000 packets. If the queue drains
at 100 Mb/s, then if we assume that in the TCP layer, a packet is about 1500 bytes, then we can multiply 1000*1500 to
get 1,500,000‬ bytes, or 12,000,000 bits. The maximum time for a packet to leave the queue is the time for the 1000th
packet to leave the queue (FIFO system). So we get 12,000,000 / 1e+8 bits/second = 0.12 seconds as the maximum
time that a packet would wait in the queue before it leaves the Network interface card(NIC).

3.Queue_Length = (RTT - Propagation_Delay - Packetization_Delay)/Packetization_Delay
If queue size increases RTT reported by ping increases accordingly.Because given a larger queue, we can see that there can be more packets on in the queue, causing the packet to have a longer queue delay. Longer queue delay causes longer RTT, which is shown in the graph. 
The symbolic equation to find Queue Length given RTT is as follows


4. we can do the following:-
 a. use multiple smaller queues to replace the larger queue.
 b.use smaller buffer .
 c.Implement QOS (Quality of service) in router.

5. By re-run the emulation
 a. Some noise my be added in the network.
 b. Network configuration changed.
 c. Which might be result in changing the graph.




