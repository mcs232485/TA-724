For q = 100,
Average Fetch Time: 1.098567
Standard Deviation: 0.429649

For q = 20,
Average Fetch Time: 0.643583
Standard Deviation: 0.479194

Q1: Why do you see a difference in webpage fetch times with short and large router buffers?
A1: When the router has a larger buffer, the TCP will keep doubling the congestion window in every RTT and send more packets. This can cause the packets being sent to have a larger fetch time when the queue size becomes large (large queuing delay). On the other hand, when the router buffer is short, the fetch time is comparitively less since the queue size is less and hence packets will have less queing delay.


Q2: Bufferbloat can occur in other places such as your network interface card (NIC). Check the output of ifconfig eth0 on your VirtualBox VM. What is the (maximum) transmit queue length on the network interface reported by ifconfig? For this queue size, if you assume the queue drains at 100Mb/s, what is the maximum time a packet might wait in the queue before it leaves the NIC? 
A2: Maximum queue length reported for my network interface is 1000. If each packet is of 1500 bytes, then in total we can have 1000 * 1500 = 1.5 * 10^6 bytes of data in the queue. Now since the queue drains at 100 Mb/s = 12.5 MB/s = 12.5 * 10^6 B/s 
we can say the maximum time a packet might have to wait in the queue before it leaves will be 1.5 / 12.5 = 0.12 seconds


Q3: How does the RTT reported by ping vary with the queue size? Describe the relation between the two.
A3: We can observe from the plotted graphs that with an increase in queue size, the RTT also increases. This can be attributed to larger queing delays at the router. We can say that the round trip time (RTT) is directly proportional to the queue size.


Q4: Identify and describe two ways to mitigate the bufferbloat problem.
A4: Bufferbloat is a cause of high latency in packet-switched networks caused by excess buffering of packets. In order to mitigate this problem, we can reduce the max queue sizes as we can see that with a lower queue size, the packets have a lesser latency. Another way can be active queue management mechanisms like Random Early Discard, where the router randomly drops packet at certain stages, before the queue is full, with a certain probability.


Q5: Describe how and why your results change when you re-run the emulation.
A5: The possible reasaons why the results change when we re-run the emulation could be due to System load and OS overheads. Since the mininet environment is software based, it is subject to overheads introduced by the OS and due to other background or parallel tasks running in the system. These overheads can vary across different runs, thus causing different results.