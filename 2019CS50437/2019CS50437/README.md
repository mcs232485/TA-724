1. Why do you see a difference in webpage fetch times with short and large router buffers?

Differences in web page retrieval durations between routers with small and large buffers can be ascribed to their impact on congestion detection and TCP performance. When buffer sizes are smaller, they tend to fill up more quickly. This triggers faster identification of congestion, prompting TCP to promptly adjust its sending rate for more responsive actions. Consequently, this leads to quicker completion of webpage fetches. On the contrary, routers with larger buffers introduce delays in recognizing congestion issues. This results in longer durations for buffer filling, delayed TCP responses, and ultimately extended time for web page retrieval. This underscores the critical role of buffer size in shaping network congestion dynamics and influencing TCP's ability to adapt effectively.


2. Bufferbloat can occur in other places such as your network interface card (NIC). Check the output of ifconfig eth0 on your VirtualBox VM. What is the (maximum) transmit queue length on the network interface reported by ifconfig? For this queue size, if you assume the queue drains at 100Mb/s, what is the maximum time a packet might wait in the queue before it leaves the NIC?

  time = (number of packets) x (packet size in bytes) x (number of bits in a byte) / (network speed in bits per second)

In this context, if we perform the calculation using the given values, the resulting time is approximately 0.12 seconds.

3. How does the RTT reported by ping vary with the queue size? Write a symbolic equation to describe the relation between the two (ignore computation overheads in ping that might affect the final result).

The round-trip time (RTT) obtained from a ping test demonstrates a clear link to the size of the queue where packets are stored. This connection can be symbolically represented as RTT = Queue_Size * Packet_Delay(0.5s < 1.0s), signifying a direct correlation between RTT and queue size. This implies that as the queue size grows, so does the RTT value. This is because a larger queue has the capacity to hold more packets, resulting in a proportional increase in the overall RTT due to packet delays. This relationship is evident in the ping test's RTT readings, which showcase that a larger queue size leads to longer RTT values because of the expanded buffer room for incoming packets. It's important to acknowledge that this analysis doesn't account for potential computational overhead in the ping process, which could potentially impact the final reported RTT.


4. Identify and describe two ways to mitigate the bufferbloat problem.

Bufferbloat, an issue characterized by overly large buffers in network routers, can be resolved by minimizing the maximum buffer capacities. This approach results in shorter waiting times, as evidenced by the results transitioning from q100 to q20 in the data. Another effective tactic involves the deployment of Active Queue Management (AQM). AQM employs probabilistic packet discarding to counter the problems linked with conventional drop tail queues. These issues encompass irregular bursts of traffic and synchronization problems among various flows. Embracing these strategies can effectively counter bufferbloat, leading to enhanced network responsiveness, diminished latency, and smoother transmission of data.

5. Describe how and why your results change when you re-run the emulation.

Conducting a new emulation with bufferbloat brings about alterations in outcomes, primarily by elevating latency and introducing delays. These changes stem from the excessive storage of packets within routers, leading to heightened round-trip times (RTT), greater variability in response times, possible fluctuations in throughput, and a less satisfactory user experience for latency-sensitive applications. The accumulation of packets within buffers leads to congestion and elongated queues, ultimately affecting the efficiency of the network and causing interruptions in the flow of data transmission.

