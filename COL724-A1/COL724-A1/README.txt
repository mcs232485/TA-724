1. Why do you see a difference in webpage fetch times with short and large router buffers?

  	Due to the buffer's size . The packets sent between h1 and h2 fill the buffer, and packet loss is not noticed until the buffer is full. As a result, times will always be greater with a larger buffer size 	because it takes longer to fill these buffers.
  	TCP congestion control, which takes periodic packet loss into account, is made simpler by smaller buffers.

2. Bufferbloat can occur in other places such as your network interface card (NIC). Check the output of ifconfig eth0 on your VirtualBox VM. What is the (maximum) transmit queue length on the network interface reported by ifconfig? For this queue size, if you assume the queue drains at 100Mb/s, what is the maximum time a packet might wait in the queue before it leaves the NIC?

  	(1000 packets x 1500 bytes x 8 bits)/(100Mbps) = 0.12s

3. How does the RTT reported by ping vary with the queue size? Write a symbolic equation to describe the relation between the two.

	Queue_Size and RTT given by ping are Proportional(linearly). More packets can be pushed into a larger queue, the overall RTT per Packet_Delay increases.  
	RTT = Queue_Size * Packet_Delay

4. Identify and describe two ways to mitigate the bufferbloat problem.

	A. probabilistically dropping packets, we may reduce buffer bloat and prevent problems with drop tail queues like bursty flows.  
	B. we can decrease the maximum buffer size. Wait will be shorter as a result.
	C. multiple smaller queues to replace the larger queue and then schedualing the queues with different priorities for different queues

5. Describe how and why your results change when you re-run the emulation. 
	The state of buffer is not same as initial and thus the behaviour is different.