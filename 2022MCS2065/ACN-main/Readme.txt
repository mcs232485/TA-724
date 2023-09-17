Answers- 
1) Why do you see a difference in webpage fetch times with short and large router buffers? 

Ans- We see a difference in webpage fetch times because of the following reasons- When the queue size is large, TCP will continue to double its congestion window, sending more and more packets. This is because TCP uses a congestion control algorithm that tries to increase the sending rate until it encounters congestion. However, if the queue size is large, there is no congestion, so TCP will continue to send packets, even though they are not being processed. This can lead to a buildup of packets in the queue, which can increase the latency of the webpage fetch request.
On the other hand, when the queue size is small, TCP will have to halve its congestion window every time a timeout occurs. This is because TCP uses a timeout mechanism to detect congestion. If the queue size is small, then a timeout is more likely to occur, which will cause TCP to halve its congestion window. This can lead to a decrease in the sending rate, which can improve the latency of the webpage fetch request.

2) Bufferbloat can occur in other places such as your network interface card (NIC). Check the output of ifconfig eth0 on your VirtualBox VM. What is the (maximum) transmit queue length on the network interface reported by ifconfig? For this queue size, if you assume the queue drains at 100Mb/s, what is the maximum time a packet might wait in the queue before it leaves the NIC? 

Ans-

3) How does the RTT reported by ping vary with the queue size? Describe the relation
between the two.

Ans- The Round-Trip Time (RTT) reported by the ping command can be affected by queue size as- As the queue size increases, the likelihood of network congestion also increases, which can lead to longer RTTs.
RTT = queue_size * propogation_delay.

4) Identify and describe two ways to mitigate the bufferbloat problem. 

Ans-i) Active Queue Management (AQM):AQM techniques are designed to actively manage the length of network queues by dropping or marking packets in a controlled manner. Rather than allowing the buffer to fill up and cause high latency, AQM mechanisms ensure that the buffer occupancy remains within acceptable limits.
ii) Configure routers and switches with smaller buffer sizes. This will help to reduce the amount of time that packets spend in the queue. However, it is important to note that reducing the buffer size too much can also lead to packet loss.

5) Describe how and why your results change when you re-run the emulation. 
Ans- The result changes when the bandwidth and delay of the links. The bandwidth and delay of the links can also affect the amount of bufferbloat that occurs, The queue size of the routers and switches,  a bursty traffic pattern is more likely to cause bufferbloat than a steady-state traffic pattern.