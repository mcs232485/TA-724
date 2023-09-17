1. Why do you see a difference in webpage fetch times with short and large router buffers?

  when q20 buffer is used 
           Average: 0.333933
           Standard Deviation: 0.071679

  when q100 buffer is used
                Average: 0.959500
                Standard Deviation: 0.360695


  From the above observation, we saw that fetching time is longer for larger router buffers than for shorter router buffers.

  This is because if the incoming rate in the router is greater than the outgoing bandwidth then we know that congestion is going to happen very near. But until the buffer is full router can not send about the congestion. For filling all the buffers the larger buffer takes a lot of time that's why the webpage fetch time is longer compared to the shorter buffer size router. The shorter router quickly fills the buffer and sends the congestion news to the sender to reduce the bandwidth rate of sending.
  

2. Bufferbloat can occur in other places such as your network interface card (NIC). Check the output of ifconfig eth0 on your VirtualBox VM. What is the (maximum) transmit queue length on the network interface reported by ifconfig? For this queue size, if you assume the queue drains at 100Mb/s, what is the maximum time a packet might wait in the queue before it leaves the NIC?

   After calling the command for ifconfig for eth0 we found the Maximum Transmission Unit(MTU) as 1500 Bytes, and the queue length is a maximum of 1000 packets.

The formula for finding time to wait in a queue before leaving is calculated as (maximum packets)*MTU/outgoing speed(queue drains)

(1000 packets x 1500 Bytes x 8 bits)/(100Mbps) = 0.12s.
 We need to convert the Bytes into bits.

Therefore a packet has to wait 0.12 seconds before leaving the queue.

3. How does the RTT reported by ping vary with the queue size? Write a symbolic equation to describe the relation between the two (ignore computation overheads in ping that might affect the final result).

  The RTT is directly proportional to the packet delay and queue size. If the queue size is more then the latency also increases, which automatically increases the round trip time of a packet.

We can state it formally as:
RTT = (packet_delay)*(queue_size)


4. Identify and describe two ways to mitigate the bufferbloat problem.

 There are two solutions for the problem of buffer bloat:

   1) Use shorter buffers:

     By using the shorter buffers we can reduce RTT per packet and reduce the delay, which is far better than using larger buffers. Make sure that the buffer size is not too small because it always makes the network congested so the buffer size is such a way that it is not too small and not large.

 when q20 buffer is used 
           Average: 0.333933
           Standard Deviation: 0.071679

  when q100 buffer is used
                Average: 0.959500
                Standard Deviation: 0.360695


  2) Random Early Detection:

   Instead of using the passive buffers which means dropping the packets after the buffer is full, use active buffers which means it early detects the congestion. We have a threshold value of buffer filling if it reaches it sends a message to the sender early feedback as that congestion is going to happen so decrease your your sending rate. This method is called as Active Queue management technique. 


 
5. Describe how and why your results change when you re-run the emulation.

If we re-run the emulation again then the output results also change like average and standard deviation of fetch time. Network configuration is unpredictable it even changes every second to second if we re-run again, even with a minute change in the network configuration the output differs a lot. An also network make have noise that will affect our simulation. 

The RTT, cwnd, and q-length graphs are changing in the result some of which decrease and may increase in the RTT of the packet. The overall delay also changes from the previous.
 
 