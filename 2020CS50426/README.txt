COL724 - Assignment 1 

Submitted by :- GURARMAAN SINGH PANJETA

To run, simply ensure dependency libraries(Ubuntu 16, python 2, pip 9, termcolor and matplotlib) and execute "sudo ./run.sh"
Executed on Baadal VM, Ubuntu 16


Kindly look into "report.pdf" submitted alongside for more detailed and pictorial answers of the following questions


Report Questions 
___________________________________________________

Q1. Why is there a difference between fetch times?

The fetch times for Buffer size = 20 average around 0.27 seconds, but the ones for Buffer size = 100 shoot up  to around 0.73 second, which is an increase of around 3 times!

This happens because the long-term TCP and the pings fill up the queues in both the cases, but since the 100 sized queue is larger, it takes longer for a packet in that queue to be serviced, and hence the fetch time increased!


___________________________________________________

Q2. Bufferbloat in NIC and other places

Using ifconfig on Baadal VM, I get the statistics (BaadalVM has ens3 instead of eth0) that the maximum transmit queue length is a 1000 and the MTU is 1500 Bytes. The maximum time a packet has to wait is when the queue is full, that is, there are a 1000 packets ahead. These are 1000 * 1500 B in size, and the (assumed) queue drain of 100Mb/sec means it takes (1000 * 1500B * 8) / 100 * 10^6 b/sec  = 0.12 seconds. Thus, the maximum waiting time in the queue is 0.12 seconds. 

____________________________________________________

Q3. RTT vs Queue size - Observation and Explanation

While The Q = 20 RTT remains rather uniformly scattered around a lower value (around 35 ms), the Q = 100 RTT shows the classic TCP Reno type curves and higher values, periodically from 100 to 200 ms and then a steep fall. The latter happens because the delayed RTT time makes the sender believe the network is congested b y delaying acks, and hence cuts down it's window to half. Further , the RTT times are larger in the Q = 100 case because it takes a larger time for a packet to be serviced because it gets admitted to a longer queue. Broadly, RTT is proportional to the Queue Size.

____________________________________________________

Q4. Mitigate Bufferbloat

Reduce Buffer sizes :- The very origin of bufferbloat is the buffer sizes of routers and switches being too large. This leads to packets having to wait to be serviced, hence leading to delays. Thus, reducing the buffer sizes to a lower value will help in reducing latency, though care should be taken to not lower the value too much and rish under-utilisation.

Active Queue Management (AQM)  :- In order to keep queue length control, we can also actively manage the queue of packets waiting for transmission. We monitor the queue's delay and drop packets when necessary to prevent the buffer from filling up. Some popular AQM algorithms are  RED(Random Early Detection),  PIE (Proportional Integral Controller Enhanced) etc.

_____________________________________________________

Q5. Changes upon Re-Running

The generated graphs and data follow similar trends upon re-runs, albeit there may be a little fluctuation. These micro differences arise because the three flows are operating consecutively, and in different runs of the emulation, may send packets in different orders with respect to each other. This may create subtle differences in the flow pattern, but the overall structure and conclusions remain the same.




