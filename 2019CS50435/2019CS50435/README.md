1. Why do you see a difference in webpage fetch times with short and large router buffers?
    
    q20: Average : 0.503067
    Standard deviation : 0.208058
    
    q100 : Average : 1.140750
    Standard deviation : 0.323908

    The variance in webpage fetch times between short and large router buffers can be attributed to their influence on congestion detection and TCP behavior. Smaller buffers fill up rapidly, prompting quicker congestion recognition and more responsive adjustments in TCP's sending rate, leading to shorter webpage fetch times. Conversely, larger buffers delay congestion acknowledgment, causing longer buffer filling times, delayed TCP responses, and ultimately longer webpage fetch times. This underscores the significance of buffer size in influencing network congestion dynamics and TCP's ability to adapt efficiently.

2. Bufferbloat can occur in other places such as your network interface card (NIC). Check the output of ifconfig eth0 on your VirtualBox VM. What is the (maximum) transmit queue length on the network interface reported by ifconfig? For this queue size, if you assume the queue drains at 100Mb/s, what is the maximum time a packet might wait in the queue before it leaves the NIC?

  time = (1000 packets x 1500 bytes x 8 bits)/(100Mbps) = 0.12s

3. How does the RTT reported by ping vary with the queue size? Write a symbolic equation to describe the relation between the two (ignore computation overheads in ping that might affect the final result).

    The reported round-trip time (RTT) from a ping test exhibits a direct correlation with the queue size. Symbolically, the relationship can be expressed as RTT = Queue_Size * Packet_Delay(0.5s < 1.0s), indicating that the RTT is proportional to the queue size. This means that with a larger queue size, the RTT value increases since the queue can accommodate more packets, leading to a direct amplification of the total RTT per packet delay. In essence, the RTT reported by the ping test reflects this relationship by showcasing how a larger queue size results in extended RTT values due to the increased buffering capacity for incoming packets. It's important to note that this analysis disregards potential computational overhead in the ping process that might influence the final reported RTT.

4. Identify and describe two ways to mitigate the bufferbloat problem.

    Bufferbloat, the problem of excessive buffering in network routers, can be addressed by reducing maximum buffer sizes, thereby decreasing waiting times as demonstrated in the data from q100 to q20. Another effective strategy is the implementation of Active Queue Management (AQM), which uses probabilistic packet dropping to prevent issues associated with traditional drop tail queues, such as bursty flows and global synchronization between flows. By adopting these measures, bufferbloat can be mitigated, leading to improved network responsiveness, reduced latency, and smoother data transmission.

5. Describe how and why your results change when you re-run the emulation.

    Re-running an emulation with bufferbloat introduces changes to results by increasing latency and delays due to excessive packet buffering in routers. This results in higher round-trip times (RTT), more variable response times, potential throughput fluctuations, and a compromised user experience for applications sensitive to latency. The accumulation of packets in buffers leads to congestion and longer queues, impacting network performance and causing disruptions in data transmission dynamics.
