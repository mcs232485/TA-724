- Why do you see a difference in webpage fetch times with short and large router
buffers?

-- When the waiting line for sending data is long, TCP keeps increasing how much it sends without waiting as much. This can cause longer delays because each piece of data takes 6 milliseconds to reach its destination. But when the waiting line is short, TCP reduces how much it sends when it's needed, so webpage requests can be sent more quickly.


- Bufferbloat can occur in other places such as your network interface card (NIC).Check the output of ifconfig eth0 on your VirtualBox VM. What is the (maximum) transmit queue length on the network interface reported by ifconfig? For
this queue size, if you assume the queue drains at 100Mb/s, what is the maximumtime a packet might wait in the queue before it leaves the NIC?

--In my mininet setup, the "txqueuelen" is set to 1000, allowing a buffer for 1000 packets. If each packet is 1500 bytes, the total buffered data would be 1.5 * 10^6 bytes. With a data transfer rate of 100 megabits per second (1.25 * 10^7 bytes per second), the buffering would take approximately 0.12 seconds.


-How does the RTT reported by ping vary with the queue size? Describe the relation between the two.
--When the size of the queue grows, the round-trip time (RTT) follows suit. This relationship is defined by the equation: RTT = queue size × propagation delay. Given that the propagation delay remains fixed, a larger queue size directly results in an extended RTT.


-Identify and describe two ways to mitigate the bufferbloat problem
-- There are two approaches to address this. First, adjusting the maximum queue size helps by keeping the buffer size manageable within a network with restricted bandwidth. This adjustment can lead to a reduction in RTT. Second, implementing active queue management techniques like RED offers another solution. This involves dropping packets at an early stage using a probability parameter, which helps control the queue size and mitigate RTT issues.




-Describe how and why your results change when you re-run the emulation.
-- These are the factors that could cause the changes when we re-run the evaluation : 
1. Unpredictability in Simulation
Certain elements of network emulation, such as packet delays and queues, might incorporate random or probabilistic mechanisms. As a result, each simulation run could yield diverse outcomes, causing fluctuations in observed metrics like latency and queue sizes.

2. System Burden : 
The computer system hosting the Mininet emulation can experience different degrees of workload stemming from other programs or tasks.
This workload has the potential to influence the emulation's performance and add extra unpredictability to outcomes.
When your system is handling other responsibilities, it could compromise the precision of the measurements you obtain.


3. Network Situations:

Even within a simulated network, diverse elements could lead to result variations.
External factors such as network utilization, packet loss, and latency can impact outcomes and introduce variability across multiple simulation runs.